from django import template
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404

from bitza.common_functions import is_in_group, GROUPS, get_menu_items
from rent.forms import PaymentModelForm
from rent.models import ExpectedPayments, Payment, Room, Contract


def summary(request):
    user = request.user
    if not is_in_group(user, group=GROUPS['owners']):
        raise Http404()
    summary = ExpectedPayments.objects.all()
    menu = get_menu_items('owners')
    context = {'summary': summary, 'menu': menu}
    print(f'menu: {menu}')
    return render(
        request,
        'rent/summary.html',
        context=context
    )


def payments(request):
    user = request.user
    payments_obj = Payment
    if not is_in_group(user, group=GROUPS['owners']):
        raise Http404()
    if request.POST:
        form = PaymentModelForm(request.POST)
        if form.is_valid():
            payment_obj = Payment()
            print(f'cleaned data: {form.cleaned_data}')
            payment_obj.date = form.cleaned_data['date']
            # payment.room = f'{form.cleaned_data("room1")}.{form.clened_data("room2")}'
            payment_obj.room = get_object_or_404(Room, pk=form.cleaned_data['room'])
            payment_obj.amount = form.cleaned_data['amount']
            payment_obj.discount = form.cleaned_data['discount']
            payment_obj.total = form.cleaned_data['total']
            payment_obj.bank_account = form.cleaned_data['bank_account']
            payment_obj.type = 'Alq'
            payment_obj.book_account = 'Приход'
            payment_obj.contract = Contract.get_active_contract_by_room(form.cleaned_data['room'])
            payment_obj.user = request.user
            payment_obj.save()
            print('saved')
        else:
            print(f'form not valid {form.errors}')
    else:
        form = PaymentModelForm()
    result = Payment.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 30)
    try:
        list_payments = paginator.page(page)
    except PageNotAnInteger:
        list_payments = paginator.page(1)
    except EmptyPage:
        list_payments = paginator.page(paginator.num_pages)
    rooms_list = Contract.get_active_rooms_for_js()
    menu = get_menu_items('owners')
    labels = ['Дата', 'Комната', 'Сумма', 'Оплачено', 'Назначение', 'Счёт']
    years = Payment.list_years(payments_obj)
    context = {
        'payments': list_payments,
        'menu': menu,
        'labels': labels,
        'years': years,
        'form': form,
        'rooms_list': rooms_list
    }

    return render(
        request,
        'rent/payments.html',
        context=context,
    )


def room2(request):
    for param in request.POST:
        print(f"{param} = {request.POST.get(param)}")
    r1 = request.POST.get('r1')
    result = Room.r2(r1=r1)
    return JsonResponse(result)


def contracts(request):
    pass


def clients(request):
    pass


# def check_and_create_clients_group(group_name='Клиенты'):
#     group = None
#     try:
#         group = Group.objects.get(name=group_name)
#     except Group.DoesNotExist:
#         group = Group.objects.create_group()
#
#
# def add_user(login, name, email):
#     if User.objects.filter(email=email).exists():
#         return
#
#     password = User.objects.make_random_password()
#     user = User.objects.create_user(login, email, password)
#     user.first_name = name
#     group = Group.objects.get(name='Клиенты')
#     user.groups.add(group) # Добавляем клиента в группу
#     user.save()

