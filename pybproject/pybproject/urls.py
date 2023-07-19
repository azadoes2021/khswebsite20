from django.contrib import admin
from django.urls import path, include
from members.views import RegisterView, LoginView, log_out
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),


    #ckeditor 사용하기 위함
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include('base.urls')),
    path('', include('blog.urls')),
    path('register/', RegisterView.as_view(), name='customregi'),
    path('login/', LoginView.as_view(), name='customlogin'),
    path("logout/", log_out, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static 함수에 첫 번째 인자로 Media file URL을, 키워드 인자 document_root로 Media file이 위치한 경로를 전달

# urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT) 첫번째 인자에 url을 그대로 쓰기도함.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler500 = 'base.views.error_500'
handler404 = 'base.views.error_404'














