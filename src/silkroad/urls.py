"""silkroad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view, about_view
from accounts import views as accounts_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from item.views import item_detail_view, item_create_view, item_edit_view, item_delete_view

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view),
    path("admin/", admin.site.urls),
    # My App
    path("item/", include("item.urls")),
    path("", include("accounts.urls")),
    path("", include("contacts.urls")),
    path("", include('django.contrib.auth.urls'))
    
    # Account App
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    
