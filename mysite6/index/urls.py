from django.conf.urls import url
from . import views

#file:sports/urls.py
urlpatterns = [
    #http://127.0.0.1:8000/index/set_cookies
    url(r'^set_cookies',views.set_cookies),
    #http://127.0.0.1:8000/index/get_cookies
    url(r'^get_cookies',views.get_cookies),
    #http://127.0.0.1:8000/index/set_session
    url(r'^set_session',views.set_session),
    #http://127.0.0.1:8000/index/get_session
    url(r'^get_session',views.get_session),
    #http://127.0.0.1:8000/index/test_cache
    url(r'^test_cache',views.test_cache),

    url(r'^test_csrf',views.test_csrf)
]