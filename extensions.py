import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class ConverterCurrency:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'\nНе удалось обработать валюту {quote}.\nУточните правильное наименование валюты по команде /values.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'\nНе удалось обработать валюту {base}.\nУточните правильное наименование валюты по команде /values.')

        try:
            if float(amount) < 0:
                raise ConvertionException(f'Вы ввели отрицательное значение: "{amount}"')
            else:
                amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        total_base = json.loads(r.content)[keys[base]]

        return total_base

