from django.contrib import admin
from django.urls import path,include


from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
admin.site.site_header  =  "Banc ABC hackathon team savanna geeks"  
admin.site.site_title  =  "Banc ABC hackathon team savanna geeksAdmin Panel"
admin.site.index_title  =  "Banc ABC hackathon team savanna geeks"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('inbound.urls')),

]