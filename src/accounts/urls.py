from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy
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
    change_password,
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
    path("change-password", change_password, name="change_password"),
    path("send-invite/", send_invitation, name="send-invite"),
    path("remove-friend/", remove_from_friends, name="remove-friend"),
    path("my-invites/accept/", accept_invitation, name="accept-invite"),
    path("my-invites/reject/", reject_invitation, name="reject-invite"),
    path("u/<slug>/", ProfileDetailView.as_view(), name="profile-detail-view"),
    # new code
    # path('password_reset/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name='password_reset_done'),
    # path('password/reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name='password_reset_complete'),
    #  path('reset_password/',
    #      auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
    #      name="reset_password"),
    #     path('reset_password_sent/',
    #         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
    #         name="password_reset_done"),
    #     path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
    #      name="password_reset_confirm"),
    #     path('reset_password_complete/',
    #         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
    #         name="password_reset_complete"),
    # path('reset_password/',
    #  auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
    #  name="reset_password"),
    # path('reset_password_sent/',
    #     auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
    #     name="password_reset_done"),
    # path('reset/<uidb64>/<token>/',
    #  auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
    #  name="password_reset_confirm"),
    # path('reset_password_complete/',
    #     auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
    #     name="password_reset_complete"),
    # path("u/<slug>/", profile_view, name="profile-view"),
    # path("", include("django.contrib.auth.urls")),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # copy
    # path('reset_password/', auth_views.PasswordResetView.as_view(
    #     template_name='accounts/password_reset.html',
    #     # email_template_name='accounts/password_reset_email.html',
    #     # subject_template_name='accounts/password_reset_subject.txt',
    #     success_url=reverse_lazy('accounts:password_reset_done')
    # ), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='accounts/password_reset_done.html'
    # ), name='reset_password_sent'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='accounts/password_reset_confirm.html',
    #     success_url=reverse_lazy('accounts:password_reset_complete')
    # ), name='reset_password_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='accounts/password_reset_complete.html'
    # ), name='reset_password_complete'),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            #  email_template_name = 'accounts/reset_password_email.txt',
            success_url=reverse_lazy("accounts:reset_password_sent"),
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_sent.html"
        ),
        name="reset_password_sent",
    ),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_form.html",
            success_url=reverse_lazy("accounts:password_reset_confirm"),
        ),
        name="reset_password_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="reset_password_done",
    ),
]
