from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

CUR_CHOICES = [
    ('USD', 'US dollar (USD)'),
    ('JPY', 'Japanese yen (JPY)'),
    ('BGN', 'Bulgarian lev (BGN)'),
    ('CZK', 'Czech koruna (CZK)'),
    ('DKK', 'Danish krone (DKK)'),
    ('EEK', 'Estonian kroon (EEK)'),
    ('GBP', 'Pound sterling (GBP)'),
    ('HUF', 'Hungarian forint (HUF)'),
    ('PLN', 'Polish zloty (PLN)'),
    ('RON', 'Romanian leu (RON)'),
    ('SEK', 'Swedish krona (SEK)'),
    ('CHF', 'Swiss franc (CHF)'),
    ('ISK', 'Icelandic krona (ISK)'),
    ('NOK', 'Norwegian krone (NOK)'),
    ('HRK', 'Croatian kuna (HRK)'),
    ('RUB', 'Russian rouble (RUB)'),
    ('TRY', 'Turkish lira (TRY)'),
    ('AUD', 'Australian dollar (AUD)'),
    ('BRL', 'Brasilian real (BRL)'),
    ('CAD', 'Canadian dollar (CAD)'),
    ('CNY', 'Chinese yuan renminbi (CNY)'),
    ('HKD', 'Hong Kong dollar (HKD)'),
    ('IDR', 'Indonesian rupiah (IDR)'),
    ('INR', 'Indian rupee (INR)'),
    ('KRW', 'South Korean won (KRW)'),
    ('MXN', 'Mexican peso (MXN)'),
    ('MYR', 'Malaysian ringgit (MYR)'),
    ('NZD', 'New Zealand dollar (NZD)'),
    ('PHP', 'Philippine peso (PHP)'),
    ('SGD', 'Singapore dollar (SGD)'),
    ('THB', 'Thai baht (THB)'),
    ('ZAR', 'South African rand (ZAR)'),

]


class Currency(models.Model):
    name = models.CharField(max_length=3, choices=CUR_CHOICES)
    rate = models.FloatField(max_length=10)
    from_date = models.DateField()
    history = HistoricalRecords()
    user = models.ManyToManyField(User, through='UserCurrency', related_name='currencies')

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name


class UserCurrency(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=False)
