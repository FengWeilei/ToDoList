from django.conf.urls import url

from . import views # . current folder

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^add',views.add, name='add'),
	url(r'^details/(?P<id>\w{0,50})/$',views.details),
]