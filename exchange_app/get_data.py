import requests


def get_data():
    response = requests.get(
            url='https://api.exchangerate-api.com/v4/latest/USD'
            ).json()
    currencies = [(value, key) for key, value in response.get('rates').items()]
    return currencies
