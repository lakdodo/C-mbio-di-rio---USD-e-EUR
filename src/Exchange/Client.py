import requests

class ExchangeClient:
    def __init__(self):
        self.url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL'


    def requisition(self):

        url = self.url
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload).json()
        return response

if __name__ == '__main__':
    main()