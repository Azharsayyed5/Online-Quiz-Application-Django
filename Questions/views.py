from django.shortcuts import render,HttpResponse, redirect
from Questions.models import QuestionMaster,Subject, UserInfo, webimages


# Create your views here.
def test(request):
    return  render(request,'test.html',{})


def selectSubject(request):
    #del request.session["qids"]
    #del request.session["count"]
    #del request.session["total"]
    #del request.session["qans"]
    subjects = Subject.objects.all()
    img = webimages.objects.all()
    return render(request,'SelectSubject.html',{'subjects':subjects, 'img':img})


def playQuiz(request):
     quids = []
     cans = []
     total = 0
     count = 0
     if("qids" not in request.session):          
          subject = Subject.objects.get(id=request.POST['subid'])
          questions = QuestionMaster.objects.filter(subject = subject)
          for question in questions:
               quids.append(question.id)
               cans.append(question.cans)
               #store the list in session
          request.session["qids"] = quids
          request.session["count"] = count
          request.session["total"] = total
          request.session["cans"] = cans
          question = QuestionMaster.objects.get(id=quids[count])          
          return render(request,'playQuiz.html',{'question':question })
     else:                
          quids = request.session["qids"]
          count = request.session["count"]
          total = request.session["total"]
          data = request.POST[str(quids[count])]
          cans = request.session["cans"]
          if(data == cans[count]):
               print("match  ",total)
               total = total+1
               request.session["total"]  = total
          
          count = count+1
          if(count < len(quids)):                         
               request.session["count"]=count
               question = QuestionMaster.objects.get(id=quids[count])     
               print(question.cans)  
               return render(request,'playQuiz.html',{'question':question })
          else:
               return HttpResponse(request.session["total"])

def register(request):
     if(request.method == "GET"):
            return render(request,"signup.html",{})
     else:
        uname = request.POST["username"]
        emailadd = request.POST["email"]
        passw = request.POST["psw"]
        passwr = request.POST["pswrepeat"]
        r1 = UserInfo()
        r1.Usern = uname
        r1.emailadd = emailadd
        r1.passw = passw
        r1.passwr = passwr
        r1.save()
        return redirect(login)

def login(request):
     return render(request,"login.html",{})

def validate(request):
     uname = request.POST["username"]
     passw = request.POST["psw"]
     try:
          u = UserInfo.objects.get(Usern=uname,passw=passw)
          return redirect(selectSubject)
     except:
          return redirect(register)
          #return render(request,"login.html",{})
        
          
     