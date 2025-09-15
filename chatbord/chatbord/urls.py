from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
 
urlpatterns = [
    path('', RedirectView.as_view(url='/board/')),
    path('index.html', RedirectView.as_view(url='/board/')),
    path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
]