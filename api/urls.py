from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^back/add$', views.OperationCreateAPIView.as_view()),
    url(r'^back/update/(?P<id>\w{0,50})/$', views.GetUpdateAPIView.as_view()),
    url(r'^list$', views.ListAPIView.as_view()),
    url(r'^$', views.TasksList.as_view(), name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.TaskDetail.as_view()),
    url(r'^delete/(?P<id>\w{0,50})/$', views.TaskDelete.as_view()),
    url(r'^add/$', views.TaskCreate.as_view(),name='add'),
    url(r'^update/(?P<id>\w{0,50})/$', views.finish, name='update'),
]
