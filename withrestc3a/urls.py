

from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.index_view),
path('api/', views.EmployeeListCreateModelMixin.as_view()),
path('api/<int:pk>/', views.EmployeeRetrieveUpdateDestroy.as_view()),
]
