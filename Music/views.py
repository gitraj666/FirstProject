from django.views import generic
from .models import Album,ArtistForm
from django.shortcuts import render
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
    template_name = 'music/album_form.html'

def artistcreate(request):
    if request.method == "GET":
        form = ArtistForm()
        return render(request,'music/album_form',{'form':form})
    elif request.method == "POST":
        form = ArtistForm(request.POST)
        form.save()
        return HttpResponseRedirect('/music/')
