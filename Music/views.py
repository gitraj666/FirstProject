from django.views import generic
from .models import Album
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(generic.CreateView):
    models = Album
    fields = ['artist','album_title','genre','album_logo']


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #Display Blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            #Cleaned normalised Data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if authenticated
            user = authenticate(username=username,password=password)
            if user is not None :

                if user.is_active:
                    login(request,user)
                    albums = Album.objects.filter(user=request.user)
                    return render(request, 'music/index.html',{'albums':albums})


        return render(request,self.template_name,{'form':form})



