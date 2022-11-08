from django import forms
import requests


class ExchangeForm(forms.Form):
    response = requests.get(
        url='https://api.exchangerate-api.com/v4/latest/USD'
        ).json()
    currencies = [(value, key) for key, value in response.get('rates').items()]
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
