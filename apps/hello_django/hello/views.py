# Create your views here.
from .utility.response import api_response
from django.shortcuts import render
from django.utils import timezone
from .models import Tasks


def home(request):
    if request.method != "GET":
        return api_response(data=None, message="Invalid request method", status_code=405)
    context = {
        "title": "Debugging Python applications like a Pro",
        "date": timezone.now(),
        "location": "Hyderabad",
        "description": "A hands-on Python workshop covering advanced topics and best practices.",
    }
    return render(request, "landing_page.html", context=context)


def get_tasks(request):
    if request.method != "GET":
        return api_response(data=None, message="Invalid request method", status_code=405)
    # TODO: Fix tasks objects filter
    task = Tasks.objects.filter(is_active=False)
    task = {"tasks": task}
    return render(request, "tasks.html", context=task)


def create_task(request):
    if request.method == "GET":
        return render(request, "create_tasks.html")
    elif request.method == "POST":
        task_name = request.POST.get("task_name")
        task_description = request.POST.get("description")
        task_db_object = Tasks(title=task_name, description=task_description)
        # TODO: Fix the below line to save the task object
        task_db_object.refresh_from_db()
        operation = {"operation": "created"}
        return render(request, "task_created.html", context=operation)


def update_task_status(request):
    # Using GET to update is not idea but just for the sake of simplicity since this is just a demo.
    if request.method == "GET":
        task_id = request.GET.get("task_id")
        task = Tasks.objects.get(id=task_id)
        task.status = request.GET.get("status")
        task.save()
        operation = {"operation": "updated"}
        return render(request, "task_created.html", context=operation)
    else:
        return api_response(data=None, message="Invalid request method", status_code=405)
