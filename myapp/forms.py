from django import forms 
from .models import TodoList

class TodoListForm(forms.ModelForm):  
     
    class Meta:
        model = TodoList
        fields = ('title',)
        exclude = ('status',)
    
    def __init__(self, *args, **kwargs): # Ajouter 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'