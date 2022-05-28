import os
import dotenv
import time
import schedule
import src.Exchange.Client as exchange
import src.Telegram.Client as TEC


dotenv.load_dotenv(dotenv.find_dotenv())
CHAT_ID = os.getenv("CHAT_ID")
TELE_TOKEN = os.getenv("TELE_TOKEN")

def main():
    #Create a exchange client
    exc_client = exchange.ExchangeClient()

    #Create Telegram bot
    telegram_bot = TEC.Client(TELE_TOKEN,CHAT_ID)

    #request the exchanges
    request_exc = exc_client.requisition()

    #send the cotations
    message = telegram_bot.send_message(request_exc)

schedule.every().day.at('08:00').do(main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)