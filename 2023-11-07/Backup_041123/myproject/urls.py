"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
  # path('', views.home, name="home"), #Sep 15th
  # path('newhome/', views.newhome, name='newhome'),
  # path('oldhome/', views.home, name='home'),
   path('admin/', admin.site.urls),
   re_path(r'^signup/$', accounts_views.signup, name='signup'),
   re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
   re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #July 9th
   re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),   
   #re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
   re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
   #re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
   re_path(r'^reset/$',    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'),name='password_reset'),
    re_path(r'^reset/done/$',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
    re_path(r'^reset/complete/$',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'), #July 14th
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'), # Aug 19th   

   re_path(r'^$', views.BoardListView.as_view(), name='home'), # Aug 25th
    re_path(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'), # Sep 1st
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    re_path(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'), # Sep 15th

]
