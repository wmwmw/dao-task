from django.contrib import admin
from django.urls import path

from fetch.views import ParseURLAjax, GetData, IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view()),
    path("fetch/", ParseURLAjax.as_view()),
    path("data/", GetData.as_view(), name="data"),
]
