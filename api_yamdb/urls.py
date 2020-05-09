from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

import reviews


urlpatterns = [
    path("admin/", admin.site.urls),
    path("redoc/", TemplateView.as_view(template_name="redoc.html"), name="redoc"),
    re_path("api/v1/titles/(?P<title_id>\d+)/reviews/", include("reviews.urls")),
    path("api/v1/api-auth/", include("rest_framework.urls")),
]
