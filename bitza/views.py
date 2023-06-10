from django.shortcuts import render
import rent.views as rent_views
from bitza.common_functions import is_in_group, GROUPS


def main(request):
    user = request.user
    context = {'current_user': 'Default'}
    if is_in_group(user, GROUPS['owners']):
        return rent_views.summary(request)
    return render(
        request,
        'main.html',
        context=context
    )


