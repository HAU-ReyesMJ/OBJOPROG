from django.shortcuts import render
from django.template.context import RequestContext

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
    return render(request, "chatbox/chatbox.html", context_instance=RequestContext(request))
    # return render_to_response("index.html", context_instance=RequestContext(request))