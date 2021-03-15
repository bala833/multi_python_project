from django.urls import path
from django.conf.urls import url
from text.views import imagetotext,success,delete_text,typing_test,login_,success_login,logout_view
 
from django.conf.urls.static import static
from django.conf import  settings


urlpatterns = [
    
	url(r'^login/$', login_, name='login'),
	url(r'^logout_view/$', logout_view, name='logout_view'),
	url(r'^success_login/$', success_login, name='success_login'),
	url(r'^imagetotext/$', imagetotext, name='imagetotext'),
	url(r'^success/$', success, name='success'),
	url(r'^delete_text/(?P<id>\d+)$', delete_text, name='delete_text'),
	url(r'^typing_test/$', typing_test, name='typing_test'),

 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)