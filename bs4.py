import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.url = "https://bank.gov.ua/ua/markets/exchangerates?date="
        self.dollar_rate = self.get_dollar_rate()

    def get_dollar_rate(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find_all("table")[0]
        trs = table.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            if len(tds) > 0 and "Долар США" in tds[0].text:
                rate = tds[2].text.replace(",", ".")
                return float(rate)
        return None

    def convert_to_usd(self, amount):
        return round(amount / self.dollar_rate, 2)

if __name__ == "__main__":
    converter = CurrencyConverter()
    amount = float(input("Введіть кількість гривень, які потрібно конвертувати до доларів США: "))
    usd_amount = converter.convert_to_usd(amount)
    print(f"{amount} грн = {usd_amount} USD")