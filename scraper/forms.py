from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from scraper.models import UserCurrency, Currency


class UserForm(forms.ModelForm):
    currency = forms.ModelMultipleChoiceField(queryset=Currency.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def clean_currency(self):
        currency = self.cleaned_data.get('currency').first()
        u = UserCurrency.objects.filter(currency=currency, user=self.instance)
        if not u:
            user_currency = UserCurrency(user=self.instance, currency=currency)
            user_currency.save()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
