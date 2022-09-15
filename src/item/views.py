from django.shortcuts import render

from .models import Item
# Create your views here.
def item_detail_view(request):
    obj = Item.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price,
        'name': obj.name
    }
    return render(request, "item/detail.html", context)