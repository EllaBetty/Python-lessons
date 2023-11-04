from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatters = [
 url(r'^$', views.home, name='home'),
 url(r'^admin/', admin.site.urls),

]
