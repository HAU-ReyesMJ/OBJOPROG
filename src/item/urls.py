from django.urls import path
from .views import item_detail_view, item_create_view, item_edit_view, item_delete_view

app_name = "item"
urlpatterns = [
    path("view/", item_detail_view, name="item_view"),
    path("<int:id>/view", item_detail_view, name="item_view"),
    path("new/", item_create_view, name="item_create"),
    path("edit/", item_edit_view, name="item_edit"),
    path("<int:id>/edit", item_edit_view, name="item_edit"),
    path("delete/", item_delete_view, name="item_delete"),
    path("<int:id>/delete", item_delete_view, name="item_delete_by_id"),
]
