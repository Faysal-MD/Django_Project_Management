from django.urls import path
from .views import ProjectListCreate, ProjectDetail, TaskListCreate, TaskDetail, CommentListCreate, CommentDetail

urlpatterns = [
    path('api/projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('api/projects/<int:project_id>/tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('api/tasks/<int:task_id>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('api/comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]