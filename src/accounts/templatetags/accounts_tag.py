from django import template
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

from accounts.models import Profile

register = template.Library()


def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get("_auth_user_id", None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)


@register.inclusion_tag("accounts\contacts copy.html", takes_context=True)
def render_logged_in_userx_list(context):
    request = context["request"]
    profile = Profile.objects.get(user=request.user)
    print(profile.get_friends())
    # print("this is the request" + request)
    print(get_all_logged_in_users())
    return {
        "users": get_all_logged_in_users(),
        "friends": profile.get_friends_profile(),
    }


@register.simple_tag(takes_context=True)
def get_logged_in_user_profile_img(context):
    request = context["request"]
    profile = Profile.objects.get(user=request.user)
    print(profile.get_friends())
    print(get_all_logged_in_users())
    return profile.image.url


# qs = Profile.objects.get_all_profiles(user)
