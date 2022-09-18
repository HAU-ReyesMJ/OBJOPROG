from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ContactsForm
from .models import Contacts

# Create your views here.
def contacts_view(request):
    
    obj = Contacts.objects.all()
    context = { 'obj': obj }

    
    return render(request, "contacts/contacts.html", context)