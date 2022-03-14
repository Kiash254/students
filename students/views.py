from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render,reverse,get_object_or_404
from matplotlib.style import context
# from django.http import HttpResponseRedirect
from students.models import Student
from .forms import Studentform
# Create your views here.

def home(request):
    students=Student.objects.all()

    data={
        "students":students,
    }
    return render (request,"home.html",data)

    #crud oparations now


    #create
def Create(request):
    form=Studentform()
    if request.method=="POST":
        form=Studentform(data=request.POST or None)

        if form.is_valid:
            form.instance.created_by=request.user
            form.save()
            return HttpResponseRedirect(reverse("students:home"))
    context={
                "form":form
            }
    return render (request,"forms.html",context)


    #update
def Detail(request,pk):
        students=Student.objects.get(id=pk)
        context={
            "students":students
        }
        return render (request,"detail.html",context)
def updateview(request,pk):
    students=get_object_or_404(Student ,id=pk)

    form=Studentform(instance=students)

    if request.method=="POST":
        form=Studentform(request.POST,instance=students)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('students:detail',kwargs={'pk':students.id}))
    context={
        "form":form
    }
    return render (request,"forms.html",context)

    #delete
def Deleteview(request ,pk):
    students=get_object_or_404(Student,id=pk)
    if request.method=="POST":
        students.delete()
        return HttpResponseRedirect(reverse('students:detail'))
    context={
            "students":students
        }
    return render(request,"delete.html" ,context)