from gettext import translation
from django.http import HttpResponse
from django.shortcuts import redirect, render

from childmissedapp import models

#get distance
from math import radians, cos, sin, asin, sqrt

def get_distance(lat1, lon1, lat2, lon2):
    # Haversine Formula
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return 6371 * c  # km


# Create your views here.
def web(request):
    return render(request,'newweb.html')
def index(request):
    return render(request,'index.html')




#userreg
def userregister(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Phone = request.POST.get('phonenumber')
        Image = request.FILES.get('image')

        # Check if email already registered
        if userreg.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('Email already exists'); window.location.href='/register/';</script>")

        # Save user
        ureg = userreg(
            name=name,
            age=age if age else None,
            address=address,
            gender=gender,
            email=email if email else None,
            password=password,
            Phone=int(Phone) if Phone else None,  # Keep IntegerField, convert to int
            Image=Image,
        )
        ureg.save()

        return redirect('login')

    return render(request, 'register.html')

#helpreg

from .models import HelplineRegister
from geopy.geocoders import Nominatim

def helpline_register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if HelplineRegister.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")

        address = request.POST.get('address')

        # 🌍 GEOCODE ADDRESS
        geolocator = Nominatim(user_agent="helpline_locator")
        location = geolocator.geocode(address)

        lat = location.latitude if location else None
        lng = location.longitude if location else None

        data = HelplineRegister(
            office_name=request.POST.get('office_name'),
            helpline_type=request.POST.get('helpline_type'),
            officer_name=request.POST.get('officer_name'),
            designation=request.POST.get('designation'),
            gender=request.POST.get('gender'),
            address=address,
            latitude=lat,
            longitude=lng,
            email=email,
            password=request.POST.get('password'),
            phone=request.POST.get('phone'),
            profile_photo=request.FILES['profile_photo'],
            id_proof=request.FILES['id_proof'],
            isapproved=True
        )
        data.save()

        return redirect('helplinelogin')

    return render(request, 'helplineregistration.html')


#society views

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SocialMediaUser
from geopy.geocoders import Nominatim

def social_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        address = request.POST.get('address')

        # Email uniqueness
        if SocialMediaUser.objects.filter(email=email).exists():
            return HttpResponse(
                "<script>alert('Email already exists'); window.location.href='/socialregister/';</script>"
            )

        # Phone uniqueness
        if SocialMediaUser.objects.filter(phone=phone).exists():
            return HttpResponse(
                "<script>alert('Phone number already exists'); window.location.href='/socialregister/';</script>"
            )

        #  Geocode the address to get latitude and longitude
        geolocator = Nominatim(user_agent="society_locator")
        location = geolocator.geocode(address)

        latitude = location.latitude if location else None
        longitude = location.longitude if location else None

        reg = SocialMediaUser(
            name=name,
            email=email,
            phone=phone,
            bio=bio,
            password=password,
            image=image,
            address=address,
            latitude=latitude,
            longitude=longitude,
        )
        reg.save()

        return redirect('societylogin')

    return render(request, 'regsociety.html')


#userlogin


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = models.userreg.objects.get(email=email)

            if user.password == password:
                request.session['email'] = email
                return HttpResponse(
                    "<script>alert('Login Successful'); window.location.href='/userhome/';</script>"
                )
            else:
                return HttpResponse(
                    "<script>alert('Incorrect password'); window.location.href='/login/';</script>"
                )

        except models.userreg.DoesNotExist:
            return HttpResponse(
                "<script>alert('User does not exist'); window.location.href='/login/';</script>"
            )

    return render(request, 'login.html')

#home url
def home(request):
    if 'email' not in request.session:
        return redirect('login')
    else:
        return render(request,'userhome.html')
    
    #helpline login


def loginhelpline(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            helpline = HelplineRegister.objects.get(email=email)
            if helpline.password == password:
                
                request.session['email'] = email
                return redirect('helplinehome')
        except HelplineRegister.DoesNotExist:
            pass

        return HttpResponse("<script>alert('Invalid login'); window.location.href='/helplinelogin/';</script>")

            
    return render(request, 'helplinelogin.html')

def homehelp(request):
    email = request.session.get('email')
    if not email:
        return redirect('helplinelogin')

    helpline = HelplineRegister.objects.get(email=email)

    return render(request, 'helplinehome.html', {
        'helpline': helpline
    })






#society login

def loginsociety(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            usersociety=models.SocialMediaUser.objects.get(email=email)
            if usersociety.password==password:
                request.session['email']=email
                return HttpResponse(
                "<script>alert('Login Sucessfull'); window.location.href='/societyhome/';</script>"
            )
            
        except models.SocialMediaUser.DoesNotExist:
           return HttpResponse(
                "<script>alert('Invalid username or password'); window.location.href='/societylogin/';</script>")
    else:
        return render (request,'societylogin.html')
    
def homesociety(request):
    if 'email' not in request.session:
        return redirect('societylogin')
    else:
        return render(request,'societyhome.html')
    
#admin login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def loginadmin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # 🔥 Hardcoded admin account
        ADMIN_EMAIL = "devanvarada@gmail.com"
        ADMIN_PASSWORD = "stjosephs"

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            request.session['admin'] = True
            return HttpResponse("<script>alert('Login Successful'); window.location.href='/adminhome/';</script>")
        
        return HttpResponse("<script>alert('Invalid email or password'); window.location.href='/adminlogin/';</script>")

    return render(request, "adminlogin.html")



def homeadmin(request):
    if 'admin' not in request.session:
        return redirect('adminlogin')

    totalusers = models.userreg.objects.count()
    totalhelplines = models.HelplineRegister.objects.count()
    totalsociety = models.SocialMediaUser.objects.count()

    return render(request, 'adminhome.html', {
        "totalusers": totalusers,
        "totalhelplines": totalhelplines,
        "totalsociety": totalsociety
    })


    
#logout
    

def logout(request):
    request.session.flush()
    return redirect('newweb')

#profiles
#userprofile
from django.shortcuts import render, redirect
from .models import userreg

def profile(request):
    if 'email' not in request.session:
        return redirect('login')

    email = request.session['email']

    
    user = userreg.objects.filter(email=email).first()

    if not user:
        return redirect('login')

    return render(request, 'userprofile.html', {'user': user})

    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

def editprofile(request):
    if 'email' not in request.session:
        return redirect('login')

    email = request.session['email']

    # ✅ FIX: avoid MultipleObjectsReturned
    user = models.userreg.objects.filter(email=email).first()

    if not user:
        return HttpResponse('User not found')

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.address = request.POST.get('address')
        user.gender = request.POST.get('gender')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.Phone = request.POST.get('phonenumber')

        # update image ONLY if new one uploaded
        if request.FILES.get('image'):
            user.Image = request.FILES.get('image')

        user.save()

        # keep session email updated
        request.session['email'] = user.email

        return redirect('userprofile')

    return render(request, 'editprofile_user.html', {'user': user})




    
    


#helpline profile
def profilehelp(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            userhelp=models.HelplineRegister.objects.get(email=email)
            return render (request,'helplineprofile.html',{'userhelp':userhelp})
        except models.HelplineRegister.DoesNotExist:
            return HttpResponse('user not found')
    else:
        return redirect('helplinelogin')
def editprofilehelp(request):
    if 'email' not in request.session:
        return redirect('helplinelogin')

    current_email = request.session['email']

    try:
        userhelp = models.HelplineRegister.objects.get(email=current_email)
    except models.HelplineRegister.DoesNotExist:
        return HttpResponse("Helpline user not found")

    if request.method == 'POST':
        new_email = request.POST.get('email')

        # 🔐 email uniqueness check
        if models.HelplineRegister.objects.filter(email=new_email).exclude(id=userhelp.id).exists():
            return HttpResponse(
                "<script>alert('Email already exists'); window.history.back();</script>"
            )

        userhelp.office_name = request.POST.get('office_name')
        userhelp.helpline_type = request.POST.get('helpline_type')
        userhelp.officer_name = request.POST.get('officer_name')
        userhelp.designation = request.POST.get('designation')
        userhelp.gender = request.POST.get('gender')
        userhelp.email = new_email
        userhelp.phone = request.POST.get('phone')
        userhelp.address = request.POST.get('address')

        if request.FILES.get('profile_photo'):
            userhelp.profile_photo = request.FILES.get('profile_photo')

        if request.FILES.get('id_proof'):
            userhelp.id_proof = request.FILES.get('id_proof')

        userhelp.save()

        request.session['email'] = userhelp.email

        return redirect('helplineprofile')

    return render(request, 'helplineprofile_edit.html', {'userhelp': userhelp})

    
#society profile
def profilesociety(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            usersociety=models.SocialMediaUser.objects.get(email=email)
            return render (request,'societyprofile.html',{'usersociety':usersociety})
        except models.SocialMediaUser.DoesNotExist:
            return HttpResponse('user not found')
    else:
        return redirect('societylogin')
    


def editprofilesociety(request):
    if 'email' not in request.session:
        return redirect('societylogin')

    current_email = request.session['email']

    try:
        usersociety = models.SocialMediaUser.objects.get(email=current_email)
    except models.SocialMediaUser.DoesNotExist:
        return HttpResponse("Society user not found")

    if request.method == 'POST':
        new_email = request.POST.get('email')

        if models.SocialMediaUser.objects.filter(email=new_email).exclude(id=usersociety.id).exists():
            return HttpResponse(
                "<script>alert('Email already exists'); window.history.back();</script>"
            )

        usersociety.name = request.POST.get('name')
        usersociety.email = new_email
        usersociety.phone = request.POST.get('phone')
        usersociety.bio = request.POST.get('bio')

        if request.FILES.get('image'):
            usersociety.image = request.FILES.get('image')

        usersociety.save()

        request.session['email'] = usersociety.email

        return redirect('societyprofile')

    return render(request, 'societyprofile_edit.html', {'usersociety': usersociety})








#admin side
#  user manage 
def userlist(request):
    user=models.userreg.objects.all()
    return render(request,'userlist.html',{'user':user})


#delete users
def deleteuser(request,id):
    user=models.userreg.objects.get(id=id)
    user.delete()
    return redirect('userlist')


#  helpline manage 
def helplist(request):
    user=models.HelplineRegister.objects.all()
    return render(request,'helplist.html',{'user':user})


#delete helpline
def deletehelp(request,id):
    user=models.HelplineRegister.objects.get(id=id)
    user.delete()
    return redirect('helplist')


# Society List
def societylist(request):
    society = models.SocialMediaUser.objects.all()
    return render(request, 'societylist.html', {'society': society})

# Delete Society User
def deletesociety(request, id):
    user = models.SocialMediaUser.objects.get(id=id)
    user.delete()
    return redirect('societylist')

from django.shortcuts import render, redirect
from .models import MissingChildCase, userreg

def missing_child_form(request):
    if 'email' not in request.session:
        return redirect('/login/')

    user = userreg.objects.filter(
        email=request.session['email']
    ).first()

    if not user:
        return redirect('/login/')

    return render(request, "child_missing_form.html", {
        'user_name': user.name,
        'user_email': user.email,   # ✅ FIX HERE
    })



def case_success(request):
    return render(request, "case_success.html")


from geopy.geocoders import Nominatim
from .models import HelplineRegister

from django.http import HttpResponse

def submit_missing_case(request):
    if 'email' not in request.session:
        return redirect('/login/')

    user = userreg.objects.get(email=request.session['email'])

    if request.method != "POST":
        return redirect("/child_missing_form/")

    geolocator = Nominatim(user_agent="case_locator")
    location = geolocator.geocode(request.POST.get("missing_location"))

    if not location:
        return HttpResponse(
            "<script>alert('Invalid location'); window.history.back();</script>"
        )

    nearest_helpline = None
    min_distance = float('inf')

    for h in HelplineRegister.objects.filter(isapproved=True):
        if h.latitude and h.longitude:
            dist = get_distance(
                location.latitude, location.longitude,
                h.latitude, h.longitude
            )
            if dist < min_distance:
                min_distance = dist
                nearest_helpline = h

    if not nearest_helpline:
        return HttpResponse(
            "<script>alert('No nearby helpline available'); window.history.back();</script>"
        )

    MissingChildCase.objects.create(
        user=user,
        helpline=nearest_helpline,
        child_name=request.POST.get("child_name"),
        child_age=request.POST.get("child_age"),
        gender=request.POST.get("gender"),
        identification_marks=request.POST.get("marks"),
        description=request.POST.get("description"),
        missing_location=request.POST.get("missing_location"),
        missing_date=request.POST.get("missing_date"),
        missing_time=request.POST.get("missing_time"),
        photo=request.FILES.get("photo"),
        video=request.FILES.get("video"),
    )

    return redirect('case_success')

    



# ADMIN - CASE LIST
# ADMIN - CASE LIST
def admin_case_list(request):
    if 'admin' not in request.session:
        return redirect('adminlogin')

    cases = (
        MissingChildCase.objects
        .select_related('user', 'helpline')  
        .order_by('-created_at')
    )

    return render(request, 'admin_case_list.html', {
        'cases': cases
    })

def admin_delete_case(request, id):
    if 'admin' not in request.session:
        return redirect('adminlogin')

    case = MissingChildCase.objects.get(id=id)
    case.delete()
    return redirect('admin_case_list')



#helpline child image
from django.shortcuts import render, redirect
from .models import MissingChildImage

def helpline_home(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        matched_child = request.POST.get('matched_child')

        print("FILES:", request.FILES)   # DEBUG
        print("PHOTO:", photo)

        if photo:
            MissingChildImage.objects.create(
                photo=photo,
                matched_child=matched_child
            )
            return redirect('helpline_home')

    missing_children = MissingChildImage.objects.all().order_by('-created_at')
    return render(request, 'helpline_home.html', {
        'missing_children': missing_children
    })








#helpline list on user area

from django.shortcuts import render
from django.db.models import Q
from .models import HelplineRegister


def user_helpline_list(request):
    query = request.GET.get('q', '').strip()

    if query:
        helplines = HelplineRegister.objects.filter(
            Q(office_name__icontains=query) |
            Q(officer_name__icontains=query) |
            Q(address__icontains=query) |
            Q(helpline_type__icontains=query)
        )
    else:
        helplines = HelplineRegister.objects.all()

    return render(request, 'user_helpline_list.html', {
        'helplines': helplines,
        'query': query
    })






#map


from django.shortcuts import render
from django.http import JsonResponse
from geopy.geocoders import Nominatim
from .models import HelplineRegister

def child_detection_map(request):
    return render(request, 'child_detection_map.html')

def get_helplines(request):
    helplines = HelplineRegister.objects.filter(isapproved=True)
    data = []
    for h in helplines:
        if h.latitude and h.longitude:
            data.append({
                'name': h.office_name,
                'lat': h.latitude,
                'lng': h.longitude,
                'type': h.helpline_type,
            })
    return JsonResponse({'helplines': data})

def get_child_location(request):
    address = request.GET.get('location')
    geolocator = Nominatim(user_agent="missing_child_locator")
    location = geolocator.geocode(address)
    if location:
        return JsonResponse({'lat': location.latitude, 'lng': location.longitude})
    return JsonResponse({'error': 'Location not found'})




# case list of users
from django.shortcuts import render, redirect
from .models import MissingChildCase, userreg

def user_missing_cases(request):
    if 'email' not in request.session:
        return redirect('/login/')

    user = userreg.objects.get(email=request.session['email'])
    cases = MissingChildCase.objects.filter(user=user).order_by('-created_at')

    return render(request, 'user_missing_cases.html', {
        'cases': cases,
        'user_name': user.name
    })



#edit case listings of user
def edit_missing_case(request, case_id):
    if 'email' not in request.session:
        return redirect('/login/')

    user = userreg.objects.get(email=request.session['email'])
    case = MissingChildCase.objects.get(id=case_id, user=user)

    if request.method == "POST":
        case.child_name = request.POST.get("child_name")
        case.child_age = request.POST.get("child_age")
        case.gender = request.POST.get("gender")
        case.identification_marks = request.POST.get("marks")
        case.description = request.POST.get("description")
        case.missing_location = request.POST.get("missing_location")
        case.missing_date = request.POST.get("missing_date")
        case.missing_time = request.POST.get("missing_time")

        if request.FILES.get("photo"):
            case.photo = request.FILES.get("photo")

        if request.FILES.get("video"):
            case.video = request.FILES.get("video")

        case.save()
        return redirect('user_missing_cases')

    return render(request, 'edit_missing_case.html', {'case': case})



#delete case listings of user
def delete_missing_case(request, case_id):
    if 'email' not in request.session:
        return redirect('/login/')

    user = userreg.objects.get(email=request.session['email'])
    case = MissingChildCase.objects.get(id=case_id, user=user)
    case.delete()
    return redirect('user_missing_cases')





#seeing case verification helpline side

from django.shortcuts import render, redirect
from .models import MissingChildCase, HelplineRegister

def helpline_case_list(request):
    email = request.session.get('email')
    if not email:
        return redirect('helplinelogin')

    helpline = HelplineRegister.objects.get(email=email)

    cases = MissingChildCase.objects.filter(
        helpline=helpline
    ).order_by('-created_at')

    return render(request, 'helpline_case_list.html', {
        'cases': cases
    })




def approve_case(request, case_id):
    helpline = HelplineRegister.objects.get(email=request.session['email'])

    case = MissingChildCase.objects.get(
        id=case_id,
        helpline=helpline
    )

    case.status = 'APPROVED'
    case.save()
    return redirect('helpline_case_list')


def mark_found(request, case_id):
    helpline = HelplineRegister.objects.get(email=request.session['email'])

    case = MissingChildCase.objects.get(
        id=case_id,
        helpline=helpline
    )

    case.status = 'FOUND'
    case.save()
    return redirect('helpline_case_list')


def helpline_delete_case(request, case_id):
    helpline = HelplineRegister.objects.get(email=request.session['email'])
   
    case = MissingChildCase.objects.get(
        id=case_id,
        helpline=helpline
    )
    
    case.delete()
    return redirect('helpline_case_list')





# HELPLINE → SEND ALERT TO SOCIETY (VIEW)

from .models import SocietyAlert, SocialMediaUser
from geopy.geocoders import Nominatim

def send_alert_to_society(request, case_id):
    helpline = HelplineRegister.objects.get(email=request.session['email'])
    case = MissingChildCase.objects.get(id=case_id, helpline=helpline)

    geolocator = Nominatim(user_agent="alert_locator")
    location = geolocator.geocode(case.missing_location)

    if not location:
        return HttpResponse("Location error")

    society_users = SocialMediaUser.objects.all()  # (later radius filter)

    for user in society_users:
        SocietyAlert.objects.create(
            case=case,
            society_user=user,
            alert_message=f"Missing child near {case.missing_location}. Age {case.child_age}, {case.gender}.",
            alert_lat=location.latitude,
            alert_lng=location.longitude
        )

    return redirect('alerted_society_list', case_id=case.id)


def alerted_society_list(request, case_id):
    alerts = SocietyAlert.objects.filter(case_id=case_id)

    return render(
        request,
        'alerted_society_list.html',
        {'alerts': alerts}
    )





#society alert list
def society_alert_list(request):
    email = request.session.get('email')
    if not email:
        return redirect('societylogin')

    user = SocialMediaUser.objects.get(email=email)
    alerts = SocietyAlert.objects.filter(society_user=user).order_by('-created_at')

    return render(request, 'society_alert_list.html', {
        'alerts': alerts
    })





from django.shortcuts import render, redirect
from django.contrib import messages

def report_child_found(request, alert_id):

    if 'email' not in request.session:
        return redirect('societylogin')

    society_user = SocialMediaUser.objects.get(email=request.session['email'])

   
    alert = SocietyAlert.objects.filter(
        id=alert_id,
        society_user=society_user
    ).first()

    if not alert:
        messages.error(request, "Invalid or unauthorized alert.")
        return redirect('society_alert_list')

    if request.method == 'POST':
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        alert.found_lat = float(lat) if lat else None
        alert.found_lng = float(lng) if lng else None

        if 'photo' in request.FILES:
            alert.found_photo = request.FILES['photo']

        alert.status = 'REPORTED'
        alert.save()

        messages.success(request, "Child found report submitted successfully.")
        return redirect('society_alert_list')

    return render(request, 'report_child_found.html', {'alert': alert})


#HELPLINE → VIEW REPORT + NAVIGATE (VIEW)
def helpline_alert_reports(request):
    helpline = HelplineRegister.objects.get(email=request.session['email'])

    alerts = SocietyAlert.objects.filter(
        case__helpline=helpline,
        status='REPORTED'
    ).order_by('-created_at')

    return render(request, 'helpline_alert_reports.html', {
        'alerts': alerts
    })




#deepface AI assistant

from deepface import DeepFace
from django.shortcuts import render, redirect
from django.contrib import messages

def ai_face_verify(request, alert_id):

    
    if 'email' not in request.session:
        return redirect('helplinelogin')

    helpline = HelplineRegister.objects.get(email=request.session['email'])

   
    alert = SocietyAlert.objects.filter(
        id=alert_id,
        case__helpline=helpline,
        status='REPORTED'
    ).first()

    if not alert:
        messages.error(request, "Invalid or unauthorized alert.")
        return redirect('helpline_alert_reports')

    case = alert.case
    result = None
    error = None

    try:
        if not case.photo or not alert.found_photo:
            error = "One of the images is missing."

        else:
            verify = DeepFace.verify(
                img1_path=case.photo.path,
                img2_path=alert.found_photo.path,
                model_name="ArcFace",
                detector_backend="retinaface",
                distance_metric="cosine",
                enforce_detection=False
            )

            distance = verify.get("distance")

            if distance is not None and distance < 0.45:
                result = " PROBABLE MATCH"
            else:
                result = "NO MATCH"

    except Exception:
        error = "Face not clear or not detected properly."

    return render(request, "helpline_ai_verify.html", {
        "alert": alert,
        "case": case,
        "result": result,
        "error": error
    })
