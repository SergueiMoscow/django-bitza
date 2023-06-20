from django.contrib.auth.models import User

GROUPS = {
    'owners': 'Хозяева',
    'administrators': 'Администраторы',
    'workers': 'Сотрудники'
}


def is_in_group(user: User, group: str):
    return user.groups.filter(name=group).exists()


def get_menu_items(group: str) -> dict:
    """Receives group name (string)
    Returns dict with Label -> url_name (urls.py)"""
    menu = {}
    print(f'get_menu_items group: {group}')
    if group == 'owners':
        menu['Сводка'] = 'summary'
        menu['Договора'] = 'contracts'
        menu['Платежи'] = 'payments'
        menu['Клиенты'] = 'clients'
    elif group == GROUPS['administrators']:
        menu['Сводка'] = 'resume'
    return menu

