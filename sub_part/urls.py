from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('new',views.new,name='new'),
    path('new1',views.new1,name='new1'),
    path('newedit/<int:id>',views.newedit,name='newedit'),
    path('newupdate/<int:id>',views.newupdate,name='newupdate'),
    path('newdelete/<int:id>',views.newdelete,name='newdelete'),


    path('expensetype',views.expensetype,name='expensetype'),
    path('expensetype1',views.expensetype1,name='expensetype1'),
    path('expensetypeedit/<int:id>',views.expensetypeedit,name='expensetypeedit'),
    path('expensetypeupdate/<int:id>',views.expensetypeupdate,name='expensetypeupdate'),
    path('expensetypedelete/<int:id>',views.expensetypedelete,name='expensetypedelete'),

    path('dept',views.dept,name='dept'),
    path('dept1',views.dept1,name='dept1'),
    path('deptedit/<int:id>',views.deptedit,name='deptedit'),
    path('deptupdate/<int:id>',views.deptupdate,name='deptupdate'),
    path('deptdelete/<int:id>',views.deptdelete,name='deptdelete'),

    path('itemexpense',views.itemexpense,name='itemexpense'),
    path('itemexpense1',views.itemexpense1,name='itemexpense1'),
    path('itemexpenseedit/<int:id>',views.itemexpenseedit,name='itemexpenseedit'),
    path('itemexpenseupdate/<int:id>',views.itemexpenseupdate,name='itemexpenseupdate'),
    path('itemexpensedelete/<int:id>',views.itemexpensedelete,name='itemexpensedelete'),

    path('hrexpense',views.hrexpense,name='hrexpense'),
    path('hrexpense1',views.hrexpense1,name='hrexpense1'),
    path('hrexpenseedit/<int:id>',views.hrexpenseedit,name='hrexpenseedit'),
    path('hrexpenseupdate/<int:id>',views.hrexpenseupdate,name='hrexpenseupdate'),
    path('hrexpensedelete/<int:id>',views.hrexpensedelete,name='hrexpensedelete'),


    path('miscexpense',views.miscexpense,name='miscexpense'),
    path('miscexpense1',views.miscexpense1,name='miscexpense1'),
    path('miscexpenseedit/<int:id>',views.miscexpenseedit,name='miscexpenseedit'),
    path('miscexpenseupdate/<int:id>',views.miscexpenseupdate,name='miscexpenseupdate'),
    path('miscexpensedelete/<int:id>',views.miscexpensedelete,name='miscexpensedelete'),

    path('home',views.index,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),

    path('table',views.table,name='table'),
    path('table1',views.table1,name='table1'),


]