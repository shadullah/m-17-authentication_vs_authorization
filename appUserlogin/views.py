from django.shortcuts import render
from . import forms 
# Create your views here.
def home(req):
    if req.method=='POST':
        reg_form = forms.RegisterForm(req.POST)
        if reg_form.is_valid():
            reg_form.save(commit=False)
    else:
        reg_form = forms.RegisterForm()
    return render(req, 'home.html', {'form': reg_form})