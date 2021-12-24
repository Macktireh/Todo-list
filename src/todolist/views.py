from django.shortcuts import render, redirect, get_object_or_404
from todolist.forms import FormTask
from todolist.models import Task


def index(request):
	form = FormTask(request.POST or None)
	if form.is_valid():
		form.save()
	taches = Task.objects.all()
	context = {'form': form, 'taches': taches}
	return render(request, 'todolist/index.html', context)


def update(request, id_tache):
	obj = get_object_or_404(Task, id=id_tache)
	form = FormTask(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('/')
	context = {'form': form}
	return render(request, 'todolist/update.html', context)


def delete(request, id_tache):
	obj = get_object_or_404(Task, id=id_tache)
	obj.delete()
	return redirect('/')

