import logging

from currencyapp.celery import app
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from scraper.models import Currency, CUR_CHOICES, UserCurrency
from scraper.utils import send_notification

logger = logging.getLogger("celery")


@app.task
def fetch_exchange_values():
    for cur in CUR_CHOICES:
        url = f'https://www.ecb.europa.eu/rss/fxref-{cur[0].lower()}.html'
        with urlopen(url) as xml_page:
            soup_page = bs(xml_page, 'xml')
        currency_list = soup_page.findAll("item")
        currency = currency_list[0]
        logger.error(currency.title.text)
        currency = currency.title.text.split(' ')
        name = currency[1]
        rate = float(currency[0])
        from_date = currency[5]
        logger.error(cur[0])
        c = Currency.objects.filter(name=cur[0]).first()
        if not c:
            c = Currency(name=name, rate=rate, from_date=from_date)
            c.save()
        elif c.rate != rate:
            c.from_date = from_date
            c.rate = rate
            c.save()
            users = UserCurrency.objects.filter(currency=c)
            users_emails = []
            for user in users:
                users_emails.append(user.user.email)
            send_notification(name, users_emails)
