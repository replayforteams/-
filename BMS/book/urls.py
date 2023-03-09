# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path("admin/", admin.site.urls),

    path(r'test/', views.test)

]
