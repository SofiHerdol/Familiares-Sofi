

from django.contrib import admin
from django.urls import path
from entregable_familiares.views import *
from app_familiares.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("template/", vista_con_template),

    path("create-familiar/", create_familiar),
    path("family-list/", family_list),
    path("index/", saludo_inicio)
]
