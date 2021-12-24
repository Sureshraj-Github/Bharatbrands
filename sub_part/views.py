from tkinter.constants import END
from django.shortcuts import render,redirect
from .models import expensetyp,create,deptt,tabl,itemexpen,ex8,miscexpen,reg1
from django.conf import settings
from django.core.mail import send_mail
import easygui

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def new(request):
    if request.method=="POST":
        create_dis=create(numm=request.POST['numm'],
                          name=request.POST['name'],
                          description=request.POST['description'],
                          atype=request.POST['atype'],
                          bal=request.POST['bal'],
                          cbal=request.POST['cbal'],
                         )
        create_dis.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat") 
        return redirect(new1)

    return render(request,'new.html')

def new1(request):
    var1=create.objects.all()
    return render(request,'new.html',{'var1':var1})

def newedit(request,id):
    stu=create.objects.get(id=id)
    return render(request,'newedit.html',{'stu':stu})

def newupdate(request,id):
    stu=create(id=id,numm=request.POST['numm'],
                          name=request.POST['name'],
                          description=request.POST['description'],
                          atype=request.POST['atype'],
                          bal=request.POST['bal'],
                          cbal=request.POST['cbal'],
                          )
    stu.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(new1) 

def newdelete(request,id):
    stu=create.objects.get(id=id)
    stu.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(new1)


def expensetype(request):
    if request.method=="POST":
        expensetyp_dis=expensetyp(name=request.POST['name'],
                                  description=request.POST['description'],
                                   )
        expensetyp_dis.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat") 
        return redirect(expensetype1)

    return render(request,'expensetype.html')
        

def expensetype1(request):
    var2=expensetyp.objects.all()
    return render(request,'expensetype.html',{'var2':var2})

def expensetypeedit(request,id):
    ed1=expensetyp.objects.get(id=id)
    return render(request,'expensetypeedit.html',{'ed1':ed1})

def expensetypeupdate(request,id):
    ed1=expensetyp(id=id,name=request.POST['name'],
                          description=request.POST['description'],
                          )
    ed1.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(expensetype1) 

def expensetypedelete(request,id):
    ed1=expensetyp.objects.get(id=id)
    ed1.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(expensetype1)

def itemexpense(request):
    if request.method=="POST":
        itemexpen_dis=itemexpen(tid=request.POST['tid'],
                                date=request.POST['date'],
                                etype=request.POST['etype'],
                                iname=request.POST['iname'],
                                quant=request.POST['quant'],
                                amt=request.POST['amt'],
                                pacc=request.POST['pacc'],
                                )
        itemexpen_dis.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat") 
        return redirect(itemexpense1)

    return render(request,'itemexpense.html')
        

def itemexpense1(request):
    var4=itemexpen.objects.all()
    return render(request,'itemexpense.html',{'var4':var4})

def itemexpenseedit(request,id):
    ed6=itemexpen.objects.get(id=id)
    return render(request,'itemexpenseedit.html',{'ed6':ed6})

def itemexpenseupdate(request,id):
    ed6=itemexpen(id=id,tid=request.POST['tid'],
                            date=request.POST['date'],
                            etype=request.POST['etype'],
                            iname=request.POST['iname'],
                            quant=request.POST['quant'],
                            amt=request.POST['amt'],
                            pacc=request.POST['pacc'],
                          )
    ed6.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(itemexpense1) 

def itemexpensedelete(request,id):
    ed6=itemexpen.objects.get(id=id)
    ed6.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(itemexpense1)



def hrexpense(request):
    if request.method=="POST":
        ex8_dis=ex8(tid=request.POST['tid'],
                    date=request.POST['date'],
                    etype=request.POST['etype'],
                    stname=request.POST['stname'],
                    purp=request.POST['purp'],
                    amt=request.POST['amt'],
                    pacc=request.POST['pacc'],
                    )
        ex8_dis.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat") 
        return redirect(hrexpense1)

    return render(request,'hrexpense.html')
        

def hrexpense1(request):
    var5=ex8.objects.all()
    return render(request,'hrexpense.html',{'var5':var5})

def hrexpenseedit(request,id):
    hr5=ex8.objects.get(id=id)
    return render(request,'hrexpenseedit.html',{'hr5':hr5})

def hrexpenseupdate(request,id):
    hr5=ex8(id=id,tid=request.POST['tid'],
                    date=request.POST['date'],
                    etype=request.POST['etype'],
                    stname=request.POST['stname'],
                    purp=request.POST['purp'],
                    amt=request.POST['amt'],
                    pacc=request.POST['pacc'],
                          )
    hr5.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(hrexpense1) 

def hrexpensedelete(request,id):
    hr5=ex8.objects.get(id=id)
    hr5.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(hrexpense1)


def miscexpense(request):
    if request.method=="POST":
        miscexpen_dis=miscexpen(tid=request.POST['tid'],
                                date=request.POST['date'],
                                etype=request.POST['etype'],
                                purp=request.POST['purp'],
                                amt=request.POST['amt'],
                                pacc=request.POST['pacc'],
                                )
        miscexpen_dis.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat") 
        return redirect(miscexpense1)

    return render(request,'miscexpense.html')
        

def miscexpense1(request):
    var6=miscexpen.objects.all()
    return render(request,'miscexpense.html',{'var6':var6})

def miscexpenseedit(request,id):
    mis=miscexpen.objects.get(id=id)
    return render(request,'miscexpenseedit.html',{'mis':mis})

def miscexpenseupdate(request,id):
    mis=miscexpen(id=id,tid=request.POST['tid'],
                        date=request.POST['date'],
                        etype=request.POST['etype'],
                        purp=request.POST['purp'],
                        amt=request.POST['amt'],
                        pacc=request.POST['pacc'],
                          )
    mis.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(miscexpense1) 

def miscexpensedelete(request,id):
    mis=miscexpen.objects.get(id=id)
    mis.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(miscexpense1)

def dept(request):
    if request.method=="POST":
        deptt_dis=deptt(name=request.POST['name'],
                        description=request.POST['description'],
                        )
        deptt_dis.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat") 
        return redirect(dept1)

    return render(request,'dept.html')
        

def dept1(request):
    var3=deptt.objects.all()
    return render(request,'dept.html',{'var3':var3})

def deptedit(request,id):
    ed3=deptt.objects.get(id=id)
    return render(request,'deptedit.html',{'ed3':ed3})

def deptupdate(request,id):
    ed3=deptt(id=id,name=request.POST['name'],
                    description=request.POST['description'],
                     )
    ed3.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(dept1) 

def deptdelete(request,id):
    ed3=deptt.objects.get(id=id)
    ed3.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(dept1)

def login(request):
    if request.method=='POST':
        if reg1.objects.filter(userid=request.POST['userid'],
                                   enterpassword=request.POST['enterpassword'],
                                   ).exists():
            ex1=reg1.objects.get(userid=request.POST['userid'],
                                      enterpassword=request.POST['enterpassword'],
                                      )
            easygui.msgbox("your data has been stored successfully",title="Bharat")
            return redirect(new)
        else:
            context2={'msg':'Oops! you entered wrong details Check and Try again'}
            return render(request,'login.html',context2)
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        ex1=reg1(nameid=request.POST['nameid'],
                emailid=request.POST['emailid'],
                phone=request.POST['phone'],
                userid=request.POST['userid'],
                enterpassword=request.POST['enterpassword'],
                )
        ex1.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat")
        return redirect(login)
    return render(request,'register.html')


def table(request):
    if request.method=="POST":
        tabl_dis=tabl(et=request.POST['et'],
                      an=request.POST['an'],
                      d=request.POST['d'],
                      it=request.POST['it'],
                      fd=request.POST['fd'],
                      td=request.POST['td'],
                      )
        tabl_dis.save()
        easygui.msgbox("your data has been stored successfully",title="Bharat") 
        return redirect(table1)

    return render(request,'table.html')


def table1(request):
    var8=tabl.objects.all()
    return render(request,'table.html',{'var8':var8})


    


