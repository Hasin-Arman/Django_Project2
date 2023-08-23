from django.urls import path
from task.views import home
from . import views
urlpatterns = [
    path('',home,name='homepage'),
    path('add/',views.Add_Book_view.as_view(),name='addpage'),
    path('show/',views.show_book_view.as_view(),name='showpage'),
    path('edit_task/<int:pk>',views.edit_book_view.as_view(),name='edit'),
    path('del_task/<int:pk>',views.del_book_view.as_view(),name='dlt'),
    path('complete_task/<int:id>',views.complete_task_view.as_view(),name='complete'),
]