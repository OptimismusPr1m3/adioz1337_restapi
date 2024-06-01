
from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
