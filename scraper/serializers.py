from rest_framework import serializers

from scraper.models import Currency, HistoricalCurrency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'rate', 'from_date']


class HistoricalCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalCurrency
        fields = ['name', 'rate', 'from_date']
