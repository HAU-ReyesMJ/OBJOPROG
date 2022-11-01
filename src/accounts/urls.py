from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include, path
from accounts import views as accounts_views
from .views import (
    my_profile,
    invites_received_view,
    profiles_list_view,
    invite_profiles_list_view,
    ProfileListView,
    ProfileDetailView,
    send_invitation,
    remove_from_friends,
    accept_invitation,
    reject_invitation,
    profile_view,
)

app_name = "accounts"
urlpatterns = [
    path("", accounts_views.home, name="home"),
    path("register/", accounts_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path(
        "myprofile/",
        my_profile,
        name="my-profile-view",
    ),
    path(
        "my-invites/",
        invites_received_view,
        name="my-invites-view",
    ),
    path(
        "all-profiles/",
        ProfileListView.as_view(),
        name="all-profiles-view",
    ),
    path(
        "to-invite/",
        invite_profiles_list_view,
        name="invite-profiles-view",
    ),
    path("send-invite/", send_invitation, name="send-invite"),
    path("remove-friend/", remove_from_friends, name="remove-friend"),
    path("my-invites/accept/", accept_invitation, name="accept-invite"),
    path("my-invites/reject/", reject_invitation, name="reject-invite"),
    path("u/<slug>/", ProfileDetailView.as_view(), name="profile-detail-view"),
    # path("u/<slug>/", profile_view, name="profile-view"),
    path("", include("django.contrib.auth.urls")),
    path(
        "change-passwordx/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
]
