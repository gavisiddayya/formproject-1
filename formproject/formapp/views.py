from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from formapp.models import Movie,Song
from django.http import HttpResponse


@csrf_exempt
def index1(request):
	if request.method=='POST':

		fname=request.POST.get('name')
		city=request.POST.get('city')
		phone=request.POST.get('phone')
		uname=request.POST.get('Uname')
		password=request.POST.get('Password')

		context ={
           'name':fname,
           'city':city,
           'phone':phone,
           'Uname':uname,
           'Password':password
           

		}
		return render(request,"showdata.html",context)
	else:
		return render(request,"insert.html")


# Create your views here.
def Create(request):
    b=Movie(actor="jigna",actor_movie="xyzzz",genre="gdsgdf")
    b.save()
    res="data created"
    return HttpResponse(res)
def createsong(request):
    objects=Movie.objects.get(id=1) 
    s=Song(movie=objects,file_type="mp3",song_name="xyz")
    s.save()
    res="song created"
    return HttpResponse(res) 


  

def read(request):
     Objects=Movie.objects.all()
     res='printing all entries in the db:<br>'
     for elt in Objects:
      res+=elt.actor+" "+elt.actor_movie+" "+elt.genre+"<br>"
     return HttpResponse(res)

def Updete(request):
     Objects=Movie.Objects.all()
     res='updating all entries in the db:<br>'
     b=Movie.Objects.get(actor="jigna")
     b.actor='jigu'
     b.save
     for elt in Objects:
      res+=elt.actor+" "+elt.actor_movie+" "+elt.genre+"<br>"
     return HttpResponse(res)
def delete(request):
    Objects=Movie.Objects.all()
    res='deleting all entries in the db:<br>'
    Objects.delete()
    return HttpResponse(res)

     


 
