import requests


class Client:


    def __init__(self, TELE_TOKEN, CHAT_ID):
        self.token = TELE_TOKEN
        self.chat_id = CHAT_ID
        self.url_base = f'https://api.telegram.org/bot{self.token}'


    def send_message(self, response):

        for item in response.values():
            if item['code'] == 'USD':
                message = requests.post(
                    url=f'{self.url_base}/sendMessage',
                    data={'chat_id': self.chat_id, 'text': f'O câmbio do Dólar é de R$ {item["bid"]}'}).json
            else:
                message = requests.post(
                    url=f'{self.url_base}/sendMessage',
                    data={'chat_id': self.chat_id, 'text': f'O câmbio do Euro é de R$ {item["bid"]}'}).json


if __name__ == '__main__':
    main()
