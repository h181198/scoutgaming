from __future__ import division
import datetime
import requests


class CurrencyConverter:
    def __init__(self):
        self.uah_rate = 0
        self.today_date = datetime.datetime.now().date()
        self.last_api_call = datetime.datetime(2000, 1, 1, 00, 00).date()
        self.access_key = "95d493c19d80977ef239b40f3e42a90e"

    def get_rate(self, from_curr, to_curr):
        # converts currency using api for further information visit http://fixer.io/
        if self.today_date != self.last_api_call:
            self.last_api_call = self.today_date

            api = "http://data.fixer.io/api/latest?access_key=" + self.access_key
            data = requests.get(api)
            json_data = data.json()

            to_rate = float(json_data['rates'][to_curr])
            from_rate = float(json_data['rates'][from_curr])

            self.uah_rate = from_rate/to_rate

        return self.uah_rate

    def uah_to_nok(self, amount):
        # Convert UAH to NOK
        return self.get_rate("UAH", "NOK") * amount
