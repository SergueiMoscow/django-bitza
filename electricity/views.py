import json
from datetime import date

from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http import JsonResponse
from bitza.common_functions import is_in_group, GROUPS
from electricity.models import MeterReading
from electricity.repository import get_last_readings_by_room, get_first_room_for_input
from electricity.services import get_list_for_input_readings, get_readings_context, save_readings
from rent.repository import get_user_by_token


class InputCounterDataView(UserPassesTestMixin, TemplateView):
    template_name = 'electricity/input.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rooms = get_list_for_input_readings()
        # Проставить css классы для вывода
        current = None
        for room in rooms:
            if room.kwt_count is None:
                if current is None:
                    current = room
                    room.html_class = 'current'
                else:
                    room.html_class = 'has-no-readings'
            else:
                room.html_class = 'has-readings'
        # Подгрузить данные по текущей комнате
        # Да, current переопределяем.
        if current:
            current = get_readings_context(current.pk)
            context['current'] = current
        else:
            current = get_readings_context()
            context['current'] = None
        context['rooms'] = rooms
        return context

    def test_func(self):
        if self.request.GET.get('token'):
            token = self.request.GET.get('token')
            self.request.user = get_user_by_token(token)
            login(self.request, self.request.user)
        return is_in_group(self.request.user, group=GROUPS['electricity'])


@method_decorator(csrf_exempt, name='dispatch')
class MeterReadingView(View):
    def get(self, request, *args, **kwargs):
        room = kwargs.get("room")
        number_records = int(request.GET.get("last", 3))
        if room:
            current = get_readings_context(room)
            return JsonResponse(current, safe=False)
        else:
            return JsonResponse({'error': 'Missing room parameter'})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        room = kwargs.get('room')
        kwt_count = data.get('kwt_count')
        if room and kwt_count is not None:
            # reading = MeterReading(room_id=room, date=date.today(), kwt_count=kwt_count, user=request.user)
            # reading.save()
            try:
                save_readings(room, kwt_count, request.user)
            except ValueError as e:
                return JsonResponse({'error': e.args[0]})
        else:
            return JsonResponse({'error': 'Missing room or kwt_count'})
        next_room_id = get_first_room_for_input()
        if next_room_id is not None:
            current = get_readings_context(next_room_id)
            return JsonResponse(current, safe=False)
        else:
            readings_context = get_readings_context()
            return JsonResponse({'success': 'Сегодня всё заполнено', 'rooms': readings_context['rooms']})
