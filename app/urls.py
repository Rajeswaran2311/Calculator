from django.urls import path
from . import views
urlpatterns = [
    path('calc/',views.cal,name='calc' ),
    path('todo/',views.todo,name='todo' ),
    path('todoadd/', views.add,name='todoadd'),
    path('delete/', views.delete,name='todoadd'),
    path('delete/<int:id>', views.delete,name='todoadd'),
    
]
