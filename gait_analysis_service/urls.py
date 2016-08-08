"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from gait_analysis_service.gait_analysis.urls import *
from gait_analysis_service.user_management import views

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^data/', include('gait_analysis_service.gait_analysis.urls')),
)


urlpatterns += patterns(
    '',
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns(
    '',
    url(r'^$', views.index),
    url(r'^homepage/', include('gait_analysis_service.user_management.urls')),
    url(r'^analysis/', include('gait_analysis_service.gait_analysis.urls')),
)
