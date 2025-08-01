from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Patient
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Payment




from io import BytesIO

# Create your views here.

def About(request):
    return render(request,'about.html')

def Index(request):
    return render(request,'index.html')

def contact(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        try:
            Contact.objects.create(name=n, contact=c, email=e, subject=s, message=m, msgdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def adminlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'login.html', locals())

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    dc = Doctor.objects.all().count()
    pc = Patient.objects.all().count()
    ac = Appointment.objects.all().count()

    d = {'dc': dc, 'pc': pc, 'ac': ac}
    return render(request,'admin_home.html', d)

def Logout(request):
    logout(request)
    return redirect('index')

def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        try:
            name = request.POST['name']
            mobile = request.POST['mobile']
            special = request.POST['special']
            shift_date = request.POST['shift_date']
            start_time = request.POST['shift_start_time']  
            end_time = request.POST['shift_end_time']      

            Doctor.objects.create(
                name=name,
                mobile=mobile,
                special=special,
                shift_date=shift_date,
                start_time=start_time,
                end_time=end_time
            )
            error = "no"
        except:
            error = "yes"

    return render(request, 'add_doctor.html', {'error': error})

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'view_doctor.html', context)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor.html')

def edit_doctor(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']

        doctor.name = n1
        doctor.mobile = m1
        doctor.special = s1

        try:
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_doctor.html', locals())

def add_patient(request):
    error = ""
    if request.method == "POST":
        try:
            name = request.POST['name']
            mobile = request.POST['mobile']
            gender = request.POST['gender']
            address = request.POST['address']
            department = request.POST['department']
            bed_number = request.POST['bed_number']

            Patient.objects.create(
                name=name,
                mobile=mobile,
                gender=gender,
                address=address,
                department=department,
                bed_number=bed_number
            )
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_patient.html', locals())

def view_patient(request):
    patients = Patient.objects.all()
    return render(request, 'view_patient.html', {'patients': patients})

def delete_patient(request, pid):
    Patient.objects.get(id=pid).delete()
    return redirect('view_patient')

def edit_patient(request, pid):
    patient = Patient.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        try:
            patient.name = request.POST['name']
            patient.mobile = request.POST['mobile']
            patient.gender = request.POST['gender']
            patient.address = request.POST['address']
            patient.department = request.POST['department']
            patient.bed_number = request.POST['bed_number']
            patient.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_patient.html', locals())



def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html', d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    d = {'appointment':appointment}
    return render(request,'view_appointment.html', d)



def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment1 = Appointment.objects.get(id=pid)
    appointment1.delete()
    return redirect('view_appointment.html')

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="yes")
    return render(request,'unread_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request,'view_queries.html', locals())

def bed_details(request):
    patients = Patient.objects.all()
    return render(request, 'bed_details.html', {'patients': patients})

def add_payment(request):
    patients = Patient.objects.all()
    if request.method == "POST":
        patient_id = request.POST.get('patient_id')
        total_fees = request.POST.get('total_fees')
        paid = request.POST.get('paid')

        patient = Patient.objects.get(id=patient_id)
        unpaid = float(total_fees) - float(paid)

        Payment.objects.create(
            patient=patient,
            total_fees=total_fees,
            paid=paid,
            unpaid=unpaid
        )
        return redirect('view_payments')  # redirect to the payment list view

    return render(request, 'add_payment.html', {'patients': patients})

def view_payments(request):
    payments = Payment.objects.select_related('patient').all()
    return render(request, 'view_payments.html', {'payments': payments})

def delete_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    payment.delete()
    return redirect('view_payments')

def edit_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    if request.method == 'POST':
        total_fees = int(request.POST.get('total_fees', 0))
        paid = int(request.POST.get('paid', 0))

        if paid > total_fees:
            return render(request, 'edit_payment.html', {'payment': payment, 'error': 'Paid amount cannot be more than total fees.'})

        unpaid = total_fees - paid
        payment.total_fees = total_fees
        payment.paid = paid
        payment.unpaid = unpaid
        payment.save()

        return redirect('view_payments')

    return render(request, 'edit_payment.html', {'payment': payment})


def download_receipt(request, id):
    payment = get_object_or_404(Payment, id=id)
    template = get_template('receipt_template.html')
    html = template.render({'payment': payment})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{payment.patient.name}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation error')
    return response