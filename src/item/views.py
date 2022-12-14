from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.shortcuts import reverse
from .forms import ItemForm
from .models import Item
from django.contrib.auth.decorators import login_required

from accounts.models import Profile

# Create your views here.
@login_required
def item_create_view(request):
    form = ItemForm(request.POST, request.FILES)
    form_class = ItemForm

    if form.is_valid():
        obj = form.save(commit=False)
        obj.seller = Profile.objects.get(user=request.user)
        obj.name = request.user.get_username()
        obj.save()

    context = {"form": form}
    return render(request, "item/item_create.html", context)


def item_detail_view(request, id=None):
    if id:
        obj = Item.objects.get(id=id)
        context = {"object": obj}
        return render(request, "item/item_detail_inidividual.html", context)
    elif "q" in request.GET:
        q = request.GET["q"]
        multiple_q = Q(
            Q(title__icontains=q)
            | Q(description__icontains=q)
            | Q(price__icontains=q)
            | Q(name__icontains=q)
        )
        data = Item.objects.filter(multiple_q)
    else:
        data = Item.objects.all().order_by("-id")
    context = {"object": data}
    return render(request, "item/item_detail.html", context)


@login_required
def item_edit_view(request, id=None):
    if id:
        item = Item.objects.get(id=id)
        form = ItemForm(request.POST or None, request.FILES or None, instance=item)
        confirm = False
        print("my id is: ", item.title)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                confirm = True
        context = {
            "item": item,
            "form": form,
            "confirm": confirm,
        }
        return render(request, "item/item_edit_individual.html", context)
    else:
        obj = Item.objects.all().order_by("-id")
        context = {"object": obj}
        return render(request, "item/item_edit.html", context)


@login_required
def item_delete_view(request, id=None):
    if id and request.method == "POST":
        objSingle = Item.objects.get(id=id)
        objSingle.delete()
        return redirect(reverse("item:item_view"))
    elif id:
        obj = Item.objects.get(id=id)
        print("")
        context = {"object": obj}
        return render(request, "item/item_delete_confirm.html", context)
    else:
        obj = Item.objects.all().order_by("-id")
        context = {"object": obj}
        return render(request, "item/item_delete.html", context)
