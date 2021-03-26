from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone
from .models import Task

# Create your views here.
def index (request):
    task_items = Task.objects.all().order_by("-date")
    return render (request, "index.html", {
        "task_items" : task_items
    })

def add_todo(request):
    taskName = request.POST['taskName']
    addDate = timezone.now()
    Task.objects.create(title= taskName, date=addDate)
    return HttpResponseRedirect ("/")

def delete_task(request, task_id):
    Task.objects.get(pk=task_id).delete()
    return HttpResponseRedirect ("/")

def fetch_tasks(request):
    if request.method == 'POST':
        task_items = Task.objects.all().order_by("-date").values()
        return JsonResponse({"task_items": list(task_items)})

def update_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.title = request.POST.get('title')
        task.save()
        task_items = Task.objects.all().order_by("-date").values()
        return JsonResponse({"task_title": task.title, "task_items": list(task_items)})