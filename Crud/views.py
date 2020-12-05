from collections import namedtuple
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.
from .models import User
from django.views.generic.base import RedirectView, TemplateView
from django.views import View


class UserAddShowView(TemplateView):
    template_name = 'crud/addandshow.html'
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(**kwargs)
            fm = StudentRegistration()
            stud = User.objects.all()
            context = {'stud':stud,'form':fm}
            return context
        
    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
        return HttpResponseRedirect('/')
            




#this function will add new item and show all items
# def add_show(request):
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             nm=fm.cleaned_data['name']
#             em=fm.cleaned_data['email']
#             pw=fm.cleaned_data['password']
#             reg = User(name=nm,email=em,password=pw)
#             reg.save()
#             messages.add_message(request,messages.SUCCESS,'Your data has been submitted')
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()
#     stud = User.objects.all()
#     return render(request, 'crud/addandshow.html', {'stud':stud,'form': fm})


class UserUpdateView(View):
    def get(self,request,id):
        pi =User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)        
        return render(request, 'crud/updatestudent.html',{'form':fm})
    def post(self,request,id):
        thank = False
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            thank=True
        return render(request, 'crud/updatestudent.html',{'form':fm,'thank':thank})    
        


#This function will update and Edit
# def update_data(request,id):
#     thank = False
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm=StudentRegistration(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#             thank=True
#     else:
#         pi =User.objects.get(pk=id)
#         fm=StudentRegistration(instance=pi)        
#     return render(request, 'crud/updatestudent.html',{'id':id,'form':fm,'thank':thank})




class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)



#this function will delete data

# def delete_data(request,id):
#     if request.method=="POST":
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')
