from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from scraper.forms import UserForm, SignUpForm
from scraper.models import UserCurrency, HistoricalCurrency, Currency
from scraper.serializers import CurrencySerializer, HistoricalCurrencySerializer


@login_required(login_url='/login/')
def edit_user(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        return render(request, 'home.html')
    else:
        form = UserForm(instance=user)
    return render(request, 'registration/edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='/login/')
def home(request):
    currencies = UserCurrency.objects.filter(user=request.user)
    current_rate = {}
    currency_history = {}
    for currency in currencies:
        rate_list = []
        current_rate[currency.currency.name] = currency.currency.rate
        h = HistoricalCurrency.objects.filter(name=currency.currency.name)
        for item in h:
            rate_list.append(item.rate)
        currency_history[currency.currency.name] = rate_list
    return render(request, 'home.html', {"rates": current_rate, "history": currency_history})


@csrf_exempt
def currency_rate(request, name):
    if request.method == 'GET':
        currency_rates = Currency.objects.get(name=name)
        serializer = CurrencySerializer(currency_rates)
        return JsonResponse(serializer.data)


@csrf_exempt
def historical_currency_rates(request, name):
    if request.method == 'GET':
        currency_rates = HistoricalCurrency.objects.filter(name=name.upper()).order_by('from_date')
        serializer = HistoricalCurrencySerializer(currency_rates, many=True)
        return JsonResponse(serializer.data, safe=False)
