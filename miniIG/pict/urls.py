from django.urls import path
from . import views
from miniIG.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name = 'home'),
	path('upload/', views.upload, name = 'upload-Pict'),
	path('update/<int:Pict_id>', views.update_Pict),
	path('delete/<int:Pict_id>', views.delete_Pict)
]


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)

