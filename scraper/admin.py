from django.contrib import admin

from scraper.models import Currency, UserCurrency


class CurrencyAdmin(admin.ModelAdmin):
    pass


class CurrenciesInline(admin.TabularInline):
    model = UserCurrency


admin.site.register(Currency, CurrencyAdmin)
