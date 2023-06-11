from datetime import date

from django import forms
from django.forms import SelectDateWidget

from rent.models import Payment, Room


class PaymentModelForm(forms.ModelForm):

    # r1_list = Room.r1()
    # room1 = forms.TypedChoiceField(
    #     label='Комната',
    #     choices=r1_list,
    #     coerce=int,
    #     widget=forms.Select(
    #         attrs={
    #             'id': 'room1',
    #             'onchange': "fillr2();"
    #         }
    #     )
    # )
    # room2 = forms.TypedChoiceField(
    #     label='',
    #     choices=tuple(),
    #     coerce=int,
    #     widget=forms.Select(
    #         attrs={'id': 'room2'}
    #     ),
    #     validators=[]
    # )

    class Meta:
        model = Payment
        fields = ['date', 'room', 'amount', 'discount', 'total', 'bank_account']
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'value': date.today()}),
            'room': forms.TextInput(attrs={'id': 'room'}),
            'amount': forms.TextInput(attrs={'id': 'amount'}),
            'discount': forms.TextInput(attrs={'id': 'discount'}),
            'total': forms.TextInput(attrs={'id': 'total'}),
            'bank_account': forms.Select()
        }

    # def clean_room2(self):
    #     print(f"Cleaned room2 {self.cleaned_data('room2')}")
    #     return self.cleaned_data('room2')
