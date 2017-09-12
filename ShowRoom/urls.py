from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^django/', admin.site.urls , name="django_admin"),
    url(r'^employee/', include('employee.urls')),
    url(r'^parts/',include('parts.urls')),
    url(r'^',include('main.urls')),
    url(r'^vehicle_models/', include('vehicle_models.urls')),
    url(r'^customer/',include('customer.urls')),
    url(r'^workshop/',include('workshop.urls')),
    url(r'^showrooms/',include('showrooms.urls')),
    url(r'^admin/', include('administrator.urls')),

]
