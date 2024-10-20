from django.shortcuts import render
from django.views.generic import View,CreateView
from django.urls import reverse_lazy

from do.forms import TaskForm
from do.models import Task

class TasksView(View):
    def get(self,*args, **kwargs):
        tasks = Task.objects.all().order_by('-done')
        return render(self.request,'index.html',{'tasks':tasks})

    def post(self,*args, **kwargs):
        task_id = self.request.POST.get('id')
        task = Task.objects.get(id=task_id)
        if(not task.done):
            task.done = True
        else:
            task.done = False
        task.save()
        tasks = Task.objects.all().order_by('-done')
        return render(self.request,'index.html',{'tasks':tasks})

    

class AddTask(CreateView):
    model = Task
    template_name = 'index.html'
    success_url = reverse_lazy('tasks')
    form_class = TaskForm