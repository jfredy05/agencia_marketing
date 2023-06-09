from django.urls import path

from .views import *


urlpatterns = [
    path('list', BlogListView.as_view()),
    path('categories', ListCategoriesView.as_view())
]
