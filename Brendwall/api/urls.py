from django.urls import path

from api.views import TestGetView, TestPostView, TestListView

app_name = 'api'

urlpatterns = [
    path('test_get/', TestGetView.as_view(), name='test_get'),
    path('test_post/', TestPostView.as_view(), name='test_post'),
    path('tests/', TestListView.as_view(), name='test_list'),
]
