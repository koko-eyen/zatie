from django.urls import include, path, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^chat/', include('chat.urls', namespace='chat')),
    re_path(r'^admin/', admin.site.urls),
]