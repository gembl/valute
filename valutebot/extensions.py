import json
import requests
from config import *


class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(
                f'Нельзя перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise ExchangeException(f'Не смог обработать количество {amount}')

        r = requests.get(
            f'http://api.exchangeratesapi.io/v1/latest?access_key=e0d38c2fed1370f97d4494031359cb62&base={base_ticker}&tsyms={quote_ticker}')
        print(r)
        total_base = float(json.loads(r.content)[keys[quote]])
        return total_base



