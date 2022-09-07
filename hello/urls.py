from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Anshu Ice Cream Admin"
admin.site.site_title = " Anshu Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Anshu Ice Cream Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]