from django.conf.urls import url, include
from mini_app_server.mini_app_api import views

urlpatterns = [
    url(r'^login/', views.APIView.as_view())
]
