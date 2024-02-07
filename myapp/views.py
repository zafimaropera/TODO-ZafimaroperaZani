from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from myapp.forms import TodoListForm 
from myapp.models import Status, TodoList

# Create your views here.
def create_item(request):
    todo = TodoList.objects.all() # Requête avec tous les objets de la liste
    status_list = Status.objects.all()
    if request.method == "POST": # pour POST
        form = TodoListForm(request.POST)  
        if form.is_valid():
            form.save() # sauvegarde l'information
            return redirect('/')
        
    form = TodoListForm() # Formulaire
    context = {"form" : form, 'todo': todo, 'status_list': status_list}
    return render(request, 'index.html', context)


def delete_item(request):
    todo_id  = request.GET.get('todo_id') # ID de la liste
    todo = TodoList.objects.get(id=todo_id) # Obtient l'objet
    todo.delete() # Supprimer
    data = {'status':'delete'}
    return JsonResponse(data)


def update_item(request):  
    data_id  = request.GET.get('data_id') # ID de la liste
    title = request.GET.get('title') # ID du statut
    print(data_id, title)

    todo = get_object_or_404(TodoList,id=data_id) # Obtient l'objet liste
    todo.title = title # Le statut reçoit une nouvelle valeur "ID du statut"
    todo.save() # sauver  

    data = {'status':'update-item', 'title':title}
    return JsonResponse(data) # renvoie


def update_status(request):  
    data_id  = request.GET.get('data_id') # ID de la liste
    status_id = request.GET.get('status_id') # ID du statut 
    
    status = Status.objects.get(id=status_id) # Obtient l'objet statut 

    todo = get_object_or_404(TodoList,id=data_id) # Obtient l'objet liste
    todo.status = status # Le statut reçoit une nouvelle valeur "ID du statut"
    todo.save() # sauver  
    
    data = {'status':status_id}
    return JsonResponse(data)