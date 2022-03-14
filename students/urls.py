from unicodedata import name
from django.urls import path
from students.views import home,Create,Detail,updateview,Deleteview
 

app_name="students"

urlpatterns=[
    path("",home,name="home"),
    path("create/",Create,name="create"),
    path("detail/<int:pk>/detail",Detail,name="detail"),
    path("update/<int:pk>/update",updateview,name="update"),
    path("students/<int:pk>/delete",Deleteview,name="delete")
]