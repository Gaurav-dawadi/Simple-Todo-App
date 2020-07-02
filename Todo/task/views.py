from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def addTask(request):

	task = Task.objects.all()
	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')		

	context = {'tasks': task, 'forms': form}
	return render(request, 'task/dashboard.html', context)
	
def updateTask(request, pk):

	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('/')		

	context = {'forms': form}
	return render(request, 'task/updateTask.html', context)

def deleteTask(request, pk):

	task = Task.objects.get(id=pk)
	
	if request.method == 'POST':
		task.delete()
		return redirect('/')		

	context = {'tasks': task}
	return render(request, 'task/deleteTask.html', context)

