from django.shortcuts import render

from custom_model_field_app.forms import PersonForm

# Create your views here.

def customview(request):
    form = PersonForm()
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
   
    return render(request,'custom.html',{'form':form})