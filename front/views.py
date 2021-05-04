from django.shortcuts import render,redirect
from .models import register,payment,student,paystatus
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
import random
from django.contrib import messages
from django.views.generic import View
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def index(request):
    return render(request,"index.html")

def registeruser(request):
   user= User.objects.get(username=request.user)
   details=register.objects.filter(user=user)
   if details:
      messages.warning(request,"You have already Registered yourself")
      return redirect('index')
   else:
        st=student.objects.get(user=user)
        print(st.number)
        if request.method=="POST" :
            d_name = request.POST['d_name'] 
            d_lname =  request.POST['d_lname'] 
            mobile = request.POST['mobile']  
            college =request.POST['college'] 
            degree= request.POST['degree']
            reg_no= random.randint(10000,99999)
            rdate = request.POST['rdate']
            l=str(mobile)
            m=str(st.number)
            print(l,m)
            if not d_name==st.f_name:
                messages.error(request,"Enter Correct  First  Name")
                return redirect('register')
            elif not d_lname==st.f_lname:
                messages.error(request,"Enter Correct Last Name")
                return redirect('register')
            elif not l==m:
                messages.error(request,"Enter Correct Contact Number")
                return redirect('payment')
            else:
                rreg = register(user=user,d_name=d_name,d_lname=d_lname,mobile=mobile,college=college,degree=degree,reg_no=reg_no,rdate=rdate )
                rreg.save()
                return render(request,"success.html")
        else:
            return render(request,"register.html") 
 
def paymentuser(request):  
    user= User.objects.get(username=request.user)
    reg=register.objects.filter(user=user)
    if reg:
        detail= register.objects.get(user=user)
        if request.method=="POST" :
            p_name= request.POST['p_name']
            l_name = request.POST['l_name']
            p_reg_no= request.POST['p_reg_no']
            mobile= request.POST['mobile']
            pmode = request.POST['pmode']
            pdate = request.POST['pdate']
            s=str(p_reg_no)
            d=str(detail.reg_no)
            l=str(mobile)
            m=str(detail.mobile)
            print(p_name,detail.d_name)
            print(p_reg_no,detail.reg_no)
            preg=payment(user=user,p_name=p_name,l_name=l_name,mobile=mobile,pmode=pmode,pdate=pdate,p_reg_no=p_reg_no,amount=25000)
            if  not p_name==detail.d_name:
                messages.error(request,"Enter  Correct First Name")
                return redirect('payment')
            elif  not l_name==detail.d_lname:
                messages.error(request,"Enter Correct Last Name")
                return redirect('payment')
            elif not s==d:
                messages.error(request,"Enter Correct Registration Number")
                return redirect('payment')
            elif not l==m:
                messages.error(request,"Enter Correct Contact Number")
                return redirect('payment')
            else:   
                preg.save()
                messages.success(request,"You have successfully paid the registration fee")
                t=paystatus.objects.create(s_name=p_name,s_lname=l_name,s_reg_no=p_reg_no,state="PAID")
                t.save()
                return redirect('index')
        else:
            return render(request,"payment.html")
    else:
        messages.warning(request,"Please register yourself first")
        return redirect('index')

def studentUser(request):
   user= User.objects.get(username=request.user)
   details=student.objects.filter(user=user)
   if details:
       messages.warning(request,"You have already filled student deatils")
       return redirect('index')
   else: 
        if request.method=="POST":
          f_name = request.POST['f_name']
          f_lname = request.POST['f_lname']
          email = request.POST['email']
          age =request.POST['age']
          number= request.POST['number']
          gender= request.POST['gender']
          father= request.POST['father']
          l_father= request.POST['l_father']
          address = request.POST['address']
          #photo = request.POST['photo']
          dob = request.POST['dob']
          sreg = student(user= user,f_name=f_name,f_lname=f_lname,email=email,age=age,number=number,gender=gender,father=father,l_father=l_father,address=address,dob=dob)
          sreg.save()
          messages.success(request,"Your details saved")
          return redirect('index')
        else:
          return render(request,"student.html")

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def render_pdf_view(request):
    user= User.objects.get(username=request.user)
    reg= register.objects.get(user=user)
    template_path = 'report_ack.html'
    context = {
             "reg_name":reg.d_name,
             "rumber": reg.reg_no,
             "reg_date" :reg.rdate,
             "reg_phone" : reg.mobile,
             "reg_clg" : reg.college,
             "reg_degree" :reg.degree,
       }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Acknowlegment.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
   


def check(request):
 user=User.objects.get(username=request.user)
 details=student.objects.filter(user=user)
 if  details:
    return redirect('register')
 else:
    messages.warning(request,"Please first fill your details")
    return redirect('index')
 

      
