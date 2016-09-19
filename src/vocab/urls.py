from django.conf.urls import url
from django.contrib import admin

from vocab.views import (
	word_name,
	word_detail,
	)

urlpatterns = [
	url(r'^$',word_name , name='word'),
    url(r'^(?P<slug>[\w-]+)/$', word_detail, name='detail'),
]

