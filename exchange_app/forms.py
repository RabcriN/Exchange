from django import forms
from .get_data import get_data


class ExchangeForm(forms.Form):
    currencies = get_data()
    amount = forms.FloatField(
        required=True,
        min_value=0,
        max_value=999999999999999,
        label='Сумма денеждых средств',
    )
    from_curr = forms.ChoiceField(
        label='Валюта которую меняем',
        choices=currencies,
    )
    to_curr = forms.ChoiceField(
        label='Валюта НА которую меняем',
        choices=currencies,
    )
