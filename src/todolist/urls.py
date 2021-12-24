from django.urls import path
from todolist.views import index, update, delete


urlpatterns = [
	path('', index, name='home'),
	path('update/<int:id_tache>/', update, name='update'),
	path('delete/<int:id_tache>/', delete, name='delete')
]