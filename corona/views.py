from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm, ReportForm, DoctorForm, PatientForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.views import login as auth_login
from .models import User
from django.contrib.auth import get_user_model
from .models import Treatment, Status, Report, Patient, Doctor
from django.http import HttpResponseRedirect
User = get_user_model()

# Create your views here.
def home(request):
    title = "Covid Index Bootstrap Test"
    current_user = request.user
    return render(request, 'index.html', {"title": title, "current_user":current_user})

def signIn(request):
    msg = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_doctor:
                    return redirect('doctor')
                else:
                    return redirect('profile')   
            else:
                msg.append('You account has been deactivated!')
    else:
        msg.append('Invalid Login credentials, try again!')
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form,'errors': msg})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:
        form = SignupForm()
    return render( request, 'registration/registration_form.html', {'form': form} )

def activate_account(request, uidb64, token):
    title = 'CovTracker'
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)       
        return redirect('editprofile')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user    

    if current_user.is_doctor == True:
        profile = Doctor.get_doc_profile(current_user)

        return render(request, 'doctorprofile.html', {"profile": profile, "current_user": current_user})

    else:
        profile = Patient.get_pat_profile(current_user)
        patient_report = Report.objects.filter(user=current_user).first()    
    
        if request.method == 'POST':
            reportform = Reportform(request.POST,request.FILES)
            if reportform.is_valid():
                report = reportform.save(commit=False)
                report.user = current_user            
                report.save()
            return render(request, 'patientprofile.html', {"profile": profile, "current_user": current_user, "reportform":reportform, "patient_report":patient_report})
        else:
            reportform = ReportForm()        
        return render(request, 'patientprofile.html', {"profile": profile, "current_user": current_user, "reportform":reportform, "patient_report":patient_report})

@login_required(login_url='/accounts/login/')
def editprofile(request):
    current_user = request.user          
    if current_user.is_doctor == True:
        if request.method == 'POST':        
            form = DoctorForm(request.POST,request.FILES)
            if form.is_valid():
                add = form.save(commit=False)
                add.user = current_user            
                add.save()
            return redirect('profile')
        else:           
            form = DoctorForm()        
        return render(request, 'profile_edit.html', {"current_user": current_user, "form":form})

    else:
        if request.method == 'POST':        
            form = PatientForm(request.POST,request.FILES)
            if form.is_valid():
                add = form.save(commit=False)
                add.user = current_user            
                add.save()
            return redirect('profile')
        else:            
            form = PatientForm()    
        return render(request, 'profile_edit.html', {"current_user": current_user, "form":form})
