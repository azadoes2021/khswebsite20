from django.urls import path
from . import views
from .views import HomeView, BaseDbBoardDetailView, AddBaseDbView, UpdateBaseDbView, DeleteBaseDbView
urlpatterns = [
    # 여섯번째 줄 새로만든 게시판 경로 및 html 파일명 수정할 것 
    path('basedbboard/', views.basedb, name="basedbboard"),# path('basedbboard/', views.posts, name="basedbboard"),
    # path('', HomeView.as_view(), name="home"),
    path('basedb/<int:pk>', BaseDbBoardDetailView.as_view(), name="basedbboard-detail"),


    # path('add_basedb/', AddBaseDbView.as_view(), name="add_basedb"),
    path('', AddBaseDbView.as_view(), name="home"),

    path('success/',views.success , name="success"),
    path('basedb/edit/<int:pk>', UpdateBaseDbView.as_view(), name="update_basedb"),
    path('basedb/<int:pk>/delete', DeleteBaseDbView.as_view(), name="delete_basedb"),

    # path('comment/delete/question/<int:comment_id>/', views.comment_delete, name="comment_delete"),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name="comment_delete"),



]





























































