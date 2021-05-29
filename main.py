import requests
import time
import smtplib
from datetime import datetime

MY_EMAIL = # Your email as a sender. You shouldn't reveal in public.
MY_PASSWORD = # Your password of the email. You shouldn't reveal in public.
RECIPIENT_EMAIL = # Recipient email


def is_volatile():
    if btc_24h_change <= -7.0 or bnb_24h_change <= -7 or eth_24h_change <= -7 or ada_24h_change <= -7 or \
            7 <= btc_24h_change or 7 <= bnb_24h_change or 7 <= eth_24h_change or 7 <= ada_24h_change:
        return True


while True:
    time_now = datetime.now().minute
    if time_now == 0:
        while True:
            response = requests.get(
                url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cbinancecoin%2Ccardano"
                    "&vs_currencies=usd&include_24hr_change=true")
            response.raise_for_status()
            data = response.json()
            btc_price = float(data["bitcoin"]["usd"])
            btc_24h_change = round(float(data["bitcoin"]["usd_24h_change"]), 2)
            bnb_price = float(data["binancecoin"]["usd"])
            bnb_24h_change = round(float(data["binancecoin"]["usd_24h_change"]), 2)
            eth_price = float(data["ethereum"]["usd"])
            eth_24h_change = round(float(data["ethereum"]["usd_24h_change"]), 2)
            ada_price = float(data["cardano"]["usd"])
            ada_24h_change = round(float(data["cardano"]["usd_24h_change"]), 2)
            if is_volatile():
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=RECIPIENT_EMAIL,
                    msg=f"Subject:Watch out!! The volatility is extremely high!"
                        f"\n\nBTC: {btc_price} USD\n\n24h_change: {btc_24h_change}%"
                        f"\n\nETH: {eth_price} USD\n\n24h_change: {eth_24h_change}%"
                        f"\n\nBNB: {bnb_price} USD\n\n24h_change: {bnb_24h_change}%"
                        f"\n\nADA: {ada_price} USD\n\n24h_change: {ada_24h_change}%"
                        f"\n\nChance to TP or SL?"
                )
            else:
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=RECIPIENT_EMAIL,
                    msg=f"Subject:Here's the hourly update of the cryptocurrency market."
                        f"\n\nBTC: {btc_price} USD\n\n24h_change: {btc_24h_change}%"
                        f"\n\nETH: {eth_price} USD\n\n24h_change: {eth_24h_change}%"
                        f"\n\nBNB: {bnb_price} USD\n\n24h_change: {bnb_24h_change}%"
                        f"\n\nADA: {ada_price} USD\n\n24h_change: {ada_24h_change}%"
                )
            time.sleep(3600)