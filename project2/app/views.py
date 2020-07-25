import os
import time

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pip._vendor.requests import delete

from.models import *

def welcome(request):
    emp=employee.objects.all()
    return render(request,'base.html',{'emp':emp})


def student_reg(request):
    if request.method=='POST':
        reg=student()
        log=logindata()
        fee=fees()

        name=request.POST['T1']
        standard=request.POST['T2']
        roll = request.POST['T3']
        email = request.POST['T4']
        passwd = request.POST['T5']
        usertype='student'

        reg.name=name
        reg.standard=standard
        reg.roll_number=roll
        reg.email=email

        fee.name = name
        fee.standard = standard
        fee.roll_number = roll
        fee.email = email
        if standard=='4':
            fee.fees_due=4000
        elif standard=='5':
            fee.fees_due=5000
        elif standard=='6':
            fee.fees_due=6000
        elif standard=='7':
            fee.fees_due=7000
        elif standard=='8':
            fee.fees_due=8000
        elif standard=='9':
            fee.fees_due=9000
        else:
            fee.fees_due=10000

        log.email=email
        log.password=passwd
        log.usertype=usertype



        fee.save()

        reg.save()
        log.save()
        emp = employee.objects.all()
        return render(request,'StudentReg.html',{'msg':'Data Saved','emp':emp})

    else:
        emp = employee.objects.all()
        return render(request,'StudentReg.html',{'emp':emp})

def show_data(request):
    emp=employee.objects.all()
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            data = fees.objects.all()

            return render(request, 'ShowData.html', {'data': data,'emp':emp})
        elif ut == 'employee':
            data = fees.objects.all()

            return render(request, 'ShowData.html', {'data': data,'emp':emp})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def edit_data(request):
    emp = employee.objects.all()
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            if request.method=='POST':
                email=request.POST['H1']
                reg=student.objects.get(email=email)
                return render(request,'EditData.html',{'data':reg,'emp':emp})


            else:
                return HttpResponseRedirect('/show_data/',{'emp':emp})
        else:
            return HttpResponseRedirect('/auth_error/')


    else:
        return HttpResponseRedirect('/auth_error/')


def edit_data1(request):
    emp=employee.objects.all()
    if request.method=='POST':

        name=request.POST['T1']
        standard=request.POST['T2']
        roll=request.POST['T3']

        email=request.POST['H2']
        reg=student.objects.get(email=email)

        reg.name=name
        reg.roll_number=roll
        reg.standard=standard
        try:

            requests.objects.get(email=email).delete()
        except:
            pass



        reg.save()

        return render(request,'EditData1.html',{'msg':'Data updated successfully','emp':emp})

    else:
        return HttpResponseRedirect('/show_data/',{'emp':emp})




def login(request):
    if request.method=='POST':
        email=request.POST['T1']
        passwd=request.POST['T2']
        try:
            log=logindata.objects.get(email=email,password=passwd)
            ut=log.usertype
            request.session['email']=email
            request.session['usertype']=ut


            if ut=='admin':
                return HttpResponseRedirect('/admin_home/')
            elif ut=='student':
                return HttpResponseRedirect('/student_home/')
            elif ut=='employee':
                return HttpResponseRedirect('/employee_home/')
        except:
            emp = employee.objects.all()

            return render(request, 'Login.html', {'msg': 'Enter Correct Email Or Password','emp':emp})




    else:
        emp = employee.objects.all()
        return render(request,'Login.html',{'emp':emp})

def student_home(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        email=request.session['email']
        if ut=='student':
            try:
                emp = employee.objects.all()
                phd = photodata.objects.get(email=email)
                dt=student.objects.get(email=email)

                return render(request, 'StudentHome.html', {'ph': phd,'dt':dt,'emp':emp})
            except:
                emp = employee.objects.all()
                dt = student.objects.get(email=email)
                return render(request, 'StudentHome.html',{'dt':dt,'emp':emp})





        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def employee_home(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        email=request.session['email']
        if ut=='employee':
            try:
                dt=employee.objects.get(email=email)
                phd = photodata.objects.get(email=email)
                emp=employee.objects.all()

                return render(request, 'EmployeeHome.html', {'ph': phd,'dt':dt,'emp':emp})
            except:
                dt = employee.objects.get(email=email)
                emp = employee.objects.all()
                return render(request,'EmployeeHome.html',{'dt':dt,'emp':emp})



        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')






def admin_home(request):
    if request.session.has_key('usertype'):
        ut = request.session['usertype']
        email=request.session['email']
        if ut == 'admin':
            try:
                phd = photodata.objects.get(email=email)
                dt = admindata.objects.get(email=email)
                emp=employee.objects.all()

                return render(request, 'AdminHome.html', {'ph': phd,'dt':dt,'emp':emp})

            except:
                dt = admindata.objects.get(email=email)
                emp = employee.objects.all()

                return render(request, 'AdminHome.html',{'dt':dt,'emp':emp})

        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def auth_error(request):
    return render(request,'AuthError.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['usertype']

    except:
        pass
    return HttpResponseRedirect('/login/')

def admin_reg(request):
    if request.session.has_key('usertype'):
        emp=employee.objects.all()
        ut=request.session['usertype']
        if ut=='admin':
            if request.method=='POST':
                reg=admindata()
                log=logindata()

                name = request.POST['T1']

                contact = request.POST['T3']
                email = request.POST['T4']
                passwd=request.POST['T5']
                usertype='admin'

                reg.name=name
                reg.contact=contact

                reg.email=email
                log.email=email
                log.password=passwd
                log.usertype=usertype




                reg.save()
                log.save()

                return render(request,'AdminReg.html',{'msg':'admin successfully registered','emp':emp})



            else:
                return render(request,'AdminReg.html',{'emp':emp})

        else:
            return HttpResponseRedirect('/auth_error/')

    else:
        return HttpResponseRedirect('/auth_error/')





def upload_photo(request):
    if request.session.has_key('usertype'):
        emp=employee.objects.all()
        if request.method=='POST':
            phd=photodata()
            email=request.session['email']
            try:
                phde = photodata.objects.get(email=email)
                os.remove("./media/" + phde.photo)
                phde.delete()

            except:
                pass
            try:
                ph = request.FILES['F1']
                path = os.path.basename(ph.name)
                file_ext = os.path.splitext(path)[1][1:]
                phname = str(int(time.time())) + '.' + file_ext
                fs = FileSystemStorage()
                fs.save(phname, ph)

                try:
                    dueph=fees.objects.get(email=email)
                    dueph.photo = phname
                    dueph.save()
                except:
                    pass


                phd.photo = phname

                phd.email = email
                phd.save()

                return render(request, 'UploadPhoto.html', {'msg': 'Photo Uploaded Successfully','emp':emp})
            except:
                return render(request, 'UploadPhoto.html', {'msg': 'file not found','emp':emp})




        else:
            return render(request,'UploadPhoto.html',{'emp':emp})

    else:
        return HttpResponseRedirect('/auth_error/')

def change_password(request):
    if request.session.has_key('usertype'):
        emp=employee.objects.all()
        if request.method=='POST':
            email=request.session['email']
            opass=request.POST['T1']
            npass=request.POST['T2']
            try:
                log=logindata.objects.get(email=email,password=opass)
                log.password=npass
                log.save()


                return render(request, 'ChangePassword.html', {'msg': 'Password Updated','emp':emp})

            except:
                return render(request,'ChangePassword.html',{'msg':'Enter correct old Password','emp':emp})



        else:
            return render(request,'ChangePassword.html',{'emp':emp})

    else:
        return HttpResponseRedirect('/login/')

def employee_reg(request):
    emp=employee.objects.all()
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            if request.method=='POST':
                reg=employee()
                log=logindata()

                name = request.POST['T1']
                id=request.POST['T2']
                contact = request.POST['T4']
                email = request.POST['T3']
                passwd=request.POST['T5']
                usertype='employee'

                reg.name=name
                reg.ID=id
                reg.contact=contact
                reg.email=email
                log.email=email
                log.password=passwd
                log.usertype=usertype

                reg.save()
                log.save()

                return render(request,'EmployeeReg.html',{'msg':'employee successfully registered','emp':emp})



            else:
                return render(request,'EmployeeReg.html',{'emp':emp})

        else:
            return HttpResponseRedirect('/auth_error/')

    else:
        return HttpResponseRedirect('/auth_error/')






def search_student(request):
    emp=employee.objects.all()
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='employee' or ut=='admin':
            if request.method=='POST':
                email=request.POST['T1']
                try:
                    a=fees.objects.get(email=email)

                    return render(request,'SearchStudent.html',{'a':a,'emp':emp})

                except:
                    return render(request,'SearchStudent.html',{'msg':'No student Found','emp':emp})


            else:
                return render(request,'SearchStudent.html',{'emp':emp})


    else:
        return HttpResponseRedirect('/auth_error/')

def change_photo(request):
    if request.session.has_key('usertype'):
        emp = employee.objects.all()
        if request.method=='POST':
            email=request.session['email']

            try:
                newph = request.FILES['T1']
                try:
                    phd = photodata.objects.get(email=email)
                    phd.delete()

                    os.remove("./media/" + phd.photo)
                except:
                    pass

                phd=photodata()


                path = os.path.basename(newph.name)
                file_ext = os.path.splitext(path)[1][1:]
                phname = str(int(time.time())) + '.' + file_ext
                fs = FileSystemStorage()
                fs.save(phname, newph)

                try:
                    dueph = fees.objects.get(email=email)
                    dueph.photo = phname
                    dueph.save()
                except:
                    pass

                phd.email = email
                phd.photo = phname

                phd.save()


                return render(request, 'ChangePhoto.html', {'msg': 'photo changed successfully','emp':emp})
            except:
                return render(request,'ChangePhoto.html', {'msg': 'file not found','emp':emp})


        else:
            return render(request,'ChangePhoto.html',{'emp':emp})

    else:
        return HttpResponseRedirect('/auth_error/')



def edit_request(request):
    if request.session.has_key('usertype'):
        emp=employee.objects.all()
        ut=request.session['usertype']
        email=request.session['email']
        if ut=='student':
            if request.method=='POST':
                req=requests()
                req.email=email
                req.message=request.POST['T1']
                req.name=request.POST['T2']

                req.standard=request.POST['T3']
                req.roll_number=request.POST['T4']
                req.save()
                return render(request,'EditRequest.html',{'msg':'request sent to admin','emp':emp})


            else:
                return render(request,'EditRequest.html',{'emp':emp})

        else:
            return HttpResponseRedirect('/auth_error/')

    else:
        return HttpResponseRedirect('/auth_error/')

def show_request(request):
    if request.session.has_key('usertype'):
        emp=employee.objects.all()
        ut=request.session['usertype']
        if ut=='admin':
            req=requests.objects.all()
            return render(request,'ShowRequest.html',{'requests':req,'emp':emp})



        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def fees_deposit(request):
    emp=employee.objects.all()
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        email=request.session['email']
        if ut=='student':


            fee = fees.objects.get(email=email)
            return render(request,'FeesDeposit.html',{'fee':fee,'emp':emp})

        else:
            return HttpResponseRedirect('/auth_error/')

    else:
        return HttpResponseRedirect('/auth_error/')

def rest_fees(request):
    emp = employee.objects.all()
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        email=request.session['email']
        if ut == 'student':
            if request.method=='GET':
                fee=fees.objects.get(email=email)
                if fee.fees_due==0:
                    return render(request, 'RestFees.html', {'mg': 'No fees amount due','emp':emp})

                else:
                    return render(request,'RestFees.html',{'fee':fee,'emp':emp})

            else:
                fee = fees.objects.get(email=email)
                fee_dep = request.POST['T1']
                fee.fees_due = (fee.fees_due)-int(fee_dep)
                fee.save()

                return render(request, 'RestFees.html', {'msg': 'Fees successfully deposited','emp':emp})



        else:
            return HttpResponseRedirect('/auth_error/')

    else:
        return HttpResponseRedirect('/auth_error/')


def due_fees(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='employee':
            due=fees.objects.all().exclude(fees_due=0)
            emp=employee.objects.all()
            return render(request,'DueFees.html',{'due':due,'emp':emp})

        else:
            return HttpResponseRedirect('/auth_error/')

    else:
        return HttpResponseRedirect('/auth_error/')


def delete_data(request):
    if request.session.has_key('usertype'):
        emp=employee.objects.all()
        ut=request.session['usertype']
        if ut=='admin':
            if request.method=='POST':
                email=request.POST['H1']
                student.objects.get(email=email).delete()
                logindata.objects.get(email=email).delete()
                fees.objects.get(email=email).delete()
                try:
                    requests.objects.get(email=email).delete()
                except:
                    pass
                try:
                    photodata.objects.get(email=email).delete()
                except:
                    pass


                return render(request,'DeleteData.html',{'msg':'data deleted successfully','emp':emp})
            else:
                return HttpResponseRedirect('/show_data/',{'emp':emp})

        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def delete_photo(request):
    if request.session.has_key('usertype'):
        email=request.session['email']

        if request.method=='GET':
            try:
                phd = photodata.objects.get(email=email)
                os.remove("./media/" + phd.photo)
                phd.delete()
                try:
                    phfees = fees.objects.get(email=email)

                    phfees.photo = 'no'

                    phfees.save()
                except:
                    pass



            except:
                pass

            return HttpResponseRedirect('/go_home/')



        else:

            return render(request, 'DeletePhoto.html')





    else:
        return HttpResponseRedirect('/auth_error/')

def go_home(request):
    if request.session.has_key('usertype'):
        ut=request.session['usertype']
        if ut=='admin':
            return HttpResponseRedirect('/admin_home/')
        elif ut=='student':
            return HttpResponseRedirect('/student_home/')
        else:
            return HttpResponseRedirect('/employee_home/')

    else:
        return HttpResponseRedirect('/login/')











