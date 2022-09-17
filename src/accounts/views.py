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


from .forms import ItemForm
from .models import Accounts
