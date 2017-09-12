from django.conf.urls import url
from . import views

app_name='administrator'
urlpatterns = [
    url(r'^$',views.dashboard,name='admin_home'),
    url(r'^charts/$',views.admin_charts,name='admin_charts'),
    url(r'^department/$',views.list_department.as_view(),name='department'),
    url(r'^users/$',views.list_users.as_view(),name='users'),
    url(r'^user_detail/(?P<pk>\d+)/$',views.detail_user.as_view(),name='user_detail'),
    url(r'^user_delete/(?P<pk>\d+)/$',views.delete_user.as_view(),name='user_delete'),
    url(r'^user_update/(?P<pk>\d+)$',views.update_user.as_view(),name='user_update'),
    url(r'^dep_detail/(?P<pk>\d+)/$',views.detail_dep.as_view(),name='dep_detail'),
    url(r'^user_update/$',views.create_user.as_view(),name='add_user'),

]


