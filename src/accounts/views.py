from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, ProfileModelForm
from .models import Profile, Relationship
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, "accounts/home.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            # obj.first_name = request.user.first_name
            # obj.last_name = request.user.first_name
            obj.save()
            messages.success(
                request, f"Your account has been created. You can log in now!"
            )
            return redirect("/")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(
        request.POST or None, request.FILES or None, instance=profile
    )
    confirm = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            confirm = True
    context = {
        "profile": profile,
        "form": form,
        "confirm": confirm,
    }
    return render(request, "accounts/myprofile.html", context)


def profile_view(request, slug=None):
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'name': obj.name
    # }
    if slug:
        obj = Profile.objects.get(user=User.objects.get(username__iexact=slug))
        context = {"object": obj}
        return render(request, "accounts/user_profile_page.html", context)
    # elif "q" in request.GET:
    #     q = request.GET["q"]
    #     # data = Data.objects.filter(last_name__icontains=q)
    #     multiple_q = Q(
    #         Q(title__icontains=q)
    #         | Q(description__icontains=q)
    #         | Q(price__icontains=q)
    #         | Q(name__icontains=q)
    #     )
    #     data = Profile.objects.filter(multiple_q)
    # else:
    #     data = Profile.objects.all()
    # context = {"object": data}
    # return render(request, "accounts/user_profile_page.html", context)


@login_required
def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)
    results = list(map(lambda x: x.sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty = True

    context = {
        "qs": results,
        "is_empty": is_empty,
    }

    return render(request, "accounts/my_invites.html", context)


def invite_profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)

    context = {
        "qs": qs,
    }
    return render(request, "accounts/to_invite_list.html", context)


def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)
    context = {
        "qs": qs,
    }
    return render(request, "accounts/profile_list.html", context)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "accounts/user_profile_page.html"

    # def get_object(self):
    #     slug = self.kwargs.get('slug')
    #     profile = Profile.objects.get(slug=slug)
    #     return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        # context["posts"] = self.get_object().get_all_authors_posts()
        context["len_posts"] = (
            # True if len(self.get_object().get_all_authors_posts()) > 0 else False
        )
        return context


class ProfileListView(ListView):
    model = Profile
    template_name = "accounts/profile_list.html"
    # context_object_name = "qs"

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context["is_empty"] = False
        if len(self.get_queryset()) == 0:
            context["is_empty"] = True

        return context


@login_required
def send_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.create(
            sender=sender, receiver=receiver, status="send"
        )

        return redirect(request.META.get("HTTP_REFERER"))
    return redirect("accounts:my-profile-view")


@login_required
def remove_from_friends(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver))
            | (Q(sender=receiver) & Q(receiver=sender))
        )
        rel.delete()
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect("accounts:my-profile-view")


@login_required
def accept_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == "send":
            rel.status = "accepted"
            rel.save()
    return redirect("accounts:my-invites-view")


@login_required
def reject_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        receiver = Profile.objects.get(user=request.user)
        sender = Profile.objects.get(pk=pk)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete()
    return redirect("accounts:my-invites-view")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("/")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/change_password.html", {"form": form})


# from .forms import AccountForm
# from .models import Account

# def register(request):
#     context = {}
#     return render(request, 'accounts/register.html', context)

# def login(request):
#     context = {}
#     return render(request, 'accounts/login.html', context)
