from django.urls import path

from apps.blog import views

app_name = 'apps.blog'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.PostDetail.as_view(), name='post_detail'),
]