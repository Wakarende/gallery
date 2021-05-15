from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('', views.home, name='home'),
  path('search/', views.search_results, name='search_results'),
  re_path('location/(?P<location_id>\d+)', views.location , name='location'),
  re_path('category/(?P<category_id>\d+)', views.category , name='category'),
  re_path('image/(?P<image_id>\d+)', views.one_image, name='image'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)