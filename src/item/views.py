from django.shortcuts import render

from .forms import ItemForm
from .models import Item
# Create your views here.
def item_create_view(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "item/item_create.html", context)

def item_detail_view(request):
    obj = Item.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'name': obj.name
    # }
    context = {
        'object': obj
    }
    return render(request, "item/item_detail.html", context)