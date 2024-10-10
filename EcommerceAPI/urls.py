from django.contrib import admin
from django.urls import path, include
from blog_app.views import home
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_app.urls')),
    path('', home, name='home'),
]



