from django.contrib import admin
from django.urls import include, path  # impor include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("posts.urls")),  # dialihkan ke posts/urls.py
]
