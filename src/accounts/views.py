from django.shortcuts import render

# from .forms import AccountsForm
# from .models import Accounts
# # Create your views here.
# def accounts_view(request):
#     form = AccountsForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context = {
#         'form': form
#     }
#     return render(request, "accounts/accounts.html", context)

from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account

def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)