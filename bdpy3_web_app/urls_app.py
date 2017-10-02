# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.views.generic import RedirectView
from bdpy3_web_app import views

urlpatterns = [

    url( r'^info/$',  views.hi, name='info_url' ),

    url( r'^$',  RedirectView.as_view(pattern_name='foo:info_url') ),

    ]