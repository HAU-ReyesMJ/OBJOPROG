from django.shortcuts import render

from .forms import ChatboxForm
from .models import Chatbox
# Create your views here.
def chatbox_view(request):
    form = ChatboxForm(request.POST)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "chatbox/chatbox_.html", context)
    