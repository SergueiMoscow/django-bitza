from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render

from bitza.common_functions import is_in_group, GROUPS, get_menu_items
from rent.models import ExpectedPayments, Payment


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
    result = Payment.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 30)
    try:
        list_payments = paginator.page(page)
    except PageNotAnInteger:
        list_payments = paginator.page(1)
    except EmptyPage:
        list_payments = paginator.page(paginator.num_pages)
    menu = get_menu_items('owners')
    labels = ['Дата', 'Комната', 'Сумма', 'Оплачено', 'Назначение', 'Счёт']
    years = Payment.list_years(payments_obj)
    context = {'payments': list_payments, 'menu': menu, 'labels': labels, 'years': years}

    return render(
        request,
        'rent/payments.html',
        context=context
    )


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

