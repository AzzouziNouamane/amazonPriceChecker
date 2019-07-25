import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sys


#URL = 'https://www.amazon.de/720%C2%B0DGREE-Trinkflasche-uberBottle-Wasserflasche-Auslaufsicher/dp/B07H7VGFSR?pf_rd_p=93ca5e1f-c180-59f3-a38f-564b8302b2de&pf_rd_r=TFG7VS6T3HD1SBN6EXMP&pd_rd_wg=mgYUE&ref_=pd_gw_ri&pd_rd_w=SNr3w&pd_rd_r=2f60cd90-3694-46aa-ac9b-262eeec28e58'

URL = sys.argv[1]
wished_price = sys.argv[2]
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:3])

    if(converted_price > float(wished_price)) :
        send_email()

    print(converted_price)
    print(title.strip())


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nouamaneazzouzi19@gmail.com', 'mntudmjngnyfamdj')
    subject = 'Price fell down !'
    body = 'Check the Amazon link : ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'nouamaneazzouzi19@gmail.com',
        'nouamaneazzouzi19@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60 * 24)