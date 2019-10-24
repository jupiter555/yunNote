from django.conf.urls import url
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/note/add
    url(r'^add$',views.add_view),
    #http://127.0.0.1:8000/note/
    url(r'^$',views.list_view),
    #http://127.0.0.1:8000/note/del/
    url(r'^del/(\d+)$',views.del_view),
    #http://127.0.0.1:8000/note/mod/
    url(r'^mod/(\d+)$',views.mod_view),
]