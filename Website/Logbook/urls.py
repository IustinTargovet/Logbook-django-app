from django.conf.urls import url
from . import views
app_name ='Logbook'
urlpatterns = [
    url(r'^', views.IndexView.as_view(), name = 'index'),
    url(r'^?P<log_id>[0-9]+)/$'), views.EntryView.as_view(), name = 'entry'),
]
