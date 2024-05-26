from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from .forms import ReviewForm

# Create your views here.
def index(request):
    return render(request,'index.html')


def movi(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'movie.html',context)

def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        description = request.POST.get('description',)
        trailer = request.POST.get('trailer')
        img = request.FILES['img']
        year = request.POST.get('year',)
        username = request.POST.get('username',)
        movie = Movie(name=name,description=description,trailer=trailer,img=img,username=username)
        movie.save()
        return redirect('/movi')
    return render(request,'add.html')

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def update(request,id):
    movie=Movie.objects.get(id=id)
    if request.user.is_authenticated:
      form=MovieForm(request.POST or None,request.FILES,instance=movie)
      if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
      if request.method=="POST":
          movie=Movie.objects.get(id=id)
          movie.delete()
          return redirect('/')
      return render(request,'delete.html')

def search(request):
  query = request.GET.get('query')
  movies = Movie.objects.filter(
    name__contains=query
  )
  return render(request, 'search.html', {'movies': movies})
