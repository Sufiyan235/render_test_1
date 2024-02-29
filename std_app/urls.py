from django.urls import path
from . import views

urlpatterns = [
    
    path('add_std/',views.add_std,name='add_std'),
    path('delete_std/<int:id>',views.delete_std,name='delete_std'),
    path('update_std/<int:id>',views.update_std,name='update_std'),
    path('do_update/<int:id>',views.do_update,name='do_update'),

]