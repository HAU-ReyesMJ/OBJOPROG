from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ItemForm
from .models import Item
# Create your views here.
def item_create_view(request):
    form = ItemForm(request.POST or None)
    form_class = ItemForm

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "item/item_create.html", context)

def item_detail_view(request, id=None):
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'name': obj.name
    # }
    if id:
        obj = Item.objects.get(id=id)
        context = { 'object': obj }
        return render(request, "item/item_detail_inidividual.html", context)
    else:
        obj = Item.objects.all()
        context = { 'object': obj }
        return render(request, "item/item_detail.html", context)

def item_edit_view(request, id=None):
    if id:
        obj = Item.objects.get(id=id)
        context = { 'object': obj }
        return render(request, "item/item_edit_individual.html", context)
    else:
        obj = Item.objects.all()
        context = { 'object': obj }
        return render(request, "item/item_edit.html", context)

def item_delete_view(request, id=None):
    if id and request.method == "POST":
        objSingle = Item.objects.get(id=id)
        objSingle.delete()
        return redirect('/../item/delete')
    elif id:
        obj = Item.objects.get(id=id)
        print('')
        context = { 'object': obj }
        return render(request, "item/item_delete_confirm.html", context)
    else:
        obj = Item.objects.all()
        context = { 'object': obj }
        return render(request, "item/item_delete.html", context)

# def item_delete_confirm_view(request, id):
#     obj = Item.objects.get(id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect('item_delete')
#     context = {
#         'object': obj
#     }
#     return render(request, "item/item_delete_confirm.html", context)