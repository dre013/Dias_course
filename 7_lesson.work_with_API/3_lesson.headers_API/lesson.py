import requests as rq
import pprint as pt
import json


import main


# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
# headers = {
#     "Accept": 'application/json',
#     "X-CMC_PRO_API_KEY": main.key
# }
# responce = rq.get(url, headers=headers)
# print(responce.json()['data'][0])


def fprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


class Crypto:
    def __init__(self, obj):
        self.api = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': obj}
        self.session = rq.Session()
        self.session.headers.update(self.headers)

    def getCrypto(self):
        url = self.api + '/v1/cryptocurrency/map'
        res = self.session.get(url)
        data = res.json()
        return data

    def getCryptoBySymbol(self, symbol):
        url = self.api + '/v2/cryptocurrency/quotes/latest'
        params = {'symbol': symbol}
        res = self.session.get(url, params=params)
        data = res.json()['data']
        return data

    def detCryptoId(self, symbol):
        url = self.api + '/v2/cryptocurrency/quotes/latest'
        params = {'id': symbol}
        res = self.session.get(url, params=params)
        data = res.json()['data']
        return data

    def detCryptoBy(self):
        url = self.api + '/v1/cryptocurrency/listings/latest'
        res = self.session.get(url)
        data = res.json()['data'][0]
        return data

    def getShowCrypto(self):
        text = json.dumps(self.getCrypto(), sort_keys=True, indent=4)
        return text

    def getShowCryptoId(self, id):
        text = json.dumps(self.detCryptoId(id), sort_keys=True, indent=4)
        return text

    def getShowCryptoBySymbol(self, char):
        text = json.dumps(self.getCryptoBySymbol(char),
                          sort_keys=True, indent=4)
        return text


Cr = Crypto(main.key)
print(Cr.getShowCryptoBySymbol('BTC'))
