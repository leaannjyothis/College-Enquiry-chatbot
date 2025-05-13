from django.shortcuts import render,redirect
from .models import *
from .models import Attendence as att
from .models import internalexammarklist as inte
from .models import internalmarklist as inte1
from .models import Events as eve
from .models import Fee_Payment as fee
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
flagattendance=0
flaginternal=0
flagclassinternal=0
flagfees=0
flagevents=0
from django.conf import settings
import os
csv_path= os.path.join(settings.BASE_DIR,'db2.csv')
df = pd.read_csv(csv_path,header=0,names=['Questions', 'Answers'])

InputTraffic = []
welcomeResponse = []

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def register1(request):
    
    form=registerform()
    form1=registerform1()
    mydict={'form':form,'form1':form1}
    if request.method=='POST':
        form=registerform(request.POST)
        form1=registerform1(request.POST)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,'Registration Successful')
            registration=form1.save()
            registration.user=user
            registration.save()
            group,created=Group.objects.get_or_create(name="userpage")
            group.user_set.add(user)
            return redirect('login1')
    else:
        return render(request,'register1.html',context=mydict)
          
def is_registration(user):
    return user.groups.filter(name="userpage").exists()

def login1(request):
        return render(request,'login1.html')

@login_required(login_url='login1')
@user_passes_test(is_registration)
def home(request):
    return render(request,'home.html')

def afterlogin_view(request):
    if is_registration(request.user):
        return redirect('home')

@login_required(login_url='login1')
@user_passes_test(is_registration)
def profile(request):
    profile1=registration.objects.get(user_id=request.user.id)
    if request.method=='POST':
        profile1=registration.objects.get(user_id=request.user)
        form3=registerform(request.POST,instance=profile1.user)
        form4=registerform1(request.POST,instance=profile1)
        if form3.is_valid() and form4.is_valid():
            user=form3.save()
            user.set_password(user.password)
            user.save()
            form4.save()
            return redirect('login1')
    else:
        form3=registerform(instance=profile1.user)
        form4=registerform1(instance=profile1)
        context={
            'form3':form3,'form4':form4
        }
    return render(request,'profile.html',context=context)  

import pyttsx3
import threading
def student_signup(request):
    if request.method == "POST":
        flaginternal=0
        flagattendance=0
        flagclassinternal=0
        flagfees=0
        flagevents=0
        x = request.POST['message']
        welcome = "Chatbot : You are welcome.."
        bye = "Chatbot : Bye!!! "
       
        if x:
            vectorizer = CountVectorizer()
            count_vec = vectorizer.fit_transform(df['Questions']).toarray()
            welcome_input = ("hello", "hi", "greetings", "sup", "what's up","hey",)
            welcome_response = ["Hiiiiiii", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

            def bot(user_response):
                text = vectorizer.transform([user_response]).toarray()
                df['similarity'] = cosine_similarity(count_vec, text)
                return df.sort_values(['similarity'], ascending=False).iloc[0]['Answers']
            
            def welcome(user_response):
                user_response=cResponse=""
                for word in user_response.split():
                    if word.lower() in welcome_input:
                        return random.choice(welcome_response)
            def speak_response(cResponse):
                def speak():
                    engine = pyttsx3.init()
                    engine.say(cResponse)  # Speak out the response
                    engine.runAndWait()
                
                # Run the speak function in a background thread
                thread = threading.Thread(target=speak)
                thread.daemon = True  # Daemon threads will not block the program from exiting
                thread.start()

            user_response = x
            user_response = user_response.lower()
            print('user response is',user_response)
            flagattendance=0
            if  (user_response.find('attendance')!=-1):
                flagattendance=1
                print('inside if')
                regno=user_response.partition('attendance')[2]
                print('type of regno is',type(regno))
                print('reg no is',regno)
                data=att.objects.filter(Register_Number=regno).first()
                print('data is',data)
                print('type is',type(data))
                dat=data.ta
                print('result is',dat)
                #dat=data.ta
                #print('dat is',dat)

            elif  (user_response.find('internal')!=-1):
                flaginternal=1
                print('inside internal if')
                regno=user_response.partition('internal')[2]
                print('type of regno is',type(regno))
                print('reg no is',regno)
                data=inte.objects.filter(Register_Number=regno).first()
                print('data is',data)
                print('type is',type(data))
                android=data.Android_Programming
                os=data.Operating_System
                st=data.Software_Testing
                cn=data.Computer_Networks
                proj=data.Project
                os1=int(os)
                android1=int(android)
                st1=int(st)
                cn1=int(cn)
                proj1=int(proj)
                
                tm=android1+st1+cn1+os1+proj1
                tm1=str(tm)
                marks="Android:"+android+",OS:"+os+",Software Testing:"+st+",Comp Networks:"+cn+",Project:"+proj+",Total:"+tm1
                #dat=data.ta

                print('result is',marks)
                dat=marks
                #dat=data.ta
                #print('dat is',dat)
            elif (user_response.find('classmarks')!=-1):
                flagclassinternal=1
                print('inside internal if')
                regno=user_response.partition('classmarks')[2]
                print('type of regno is',type(regno))
                print('reg no is',regno)
                data=inte1.objects.filter(Register_Number=regno).first()
                print('data is',data)
                print('type is',type(data))
                android=data.Android_Programming
                os=data.Operating_System
                st=data.Software_Testing
                cn=data.Computer_Networks
                proj=data.Project
                os1=int(os)
                android1=int(android)
                st1=int(st)
                cn1=int(cn)
                proj1=int(proj)
                
                tm=android1+st1+cn1+os1+proj1
                tm1=str(tm)
                marks="Android:"+android+",OS:"+os+",Software Testing:"+st+",Comp Networks:"+cn+",Project:"+proj+",Total:"+tm1
                #dat=data.ta

                print('result is',marks)
                dat=marks
                #dat=data.ta
                #print('dat is',dat)
            elif (user_response.find('fees')!=-1):
                flagfees=1
                print('inside internal if')
                regno=user_response.partition('fees')[2]
                print('type of regno is',type(regno))
                print('reg no is',regno)
                data=fee.objects.filter(Register_Number=regno).first()
                print('data is',data)
                print('type is',type(data))
                due=data.Due
                lastdate=str(data.Last_Date)

                
       
                marks="Due Amount:"+due+",Last Date:"+lastdate
                #dat=data.ta

                print('result is',marks)
                dat=marks
                #dat=data.ta
                #print('dat is',dat)
            elif (user_response.find('events')!=-1):
                flagevents=1
                print('inside internal if')
                data=eve.objects.first()
                print('data is',data)
                print('type is',type(data))
                dat=data.Description
    
                #dat=data.ta
                #print('dat is',dat)
            #else:
                #cResponse=bot(user_response)
                #dat=cResponse
                #welcomeResponse.append(cResponse)
                

            InputTraffic.append(user_response)
            if(user_response not in ['bye','shutdown','exit', 'quit']):
                    if(welcome(user_response)!=None):
                        print('inside second if')
                        wResponse  = welcome(user_response)
                        print('welcome response type is',type(wResponse))
                        welcomeResponse.append(wResponse)
                        # print('welcomeResponse',welcomeResponse)
                    else:
                        # print("Chatbot : ",end="")
                        if flagattendance==1:
                            print('inside else')
                            flagattendance=0
                            flaginternal=0
                            flagclassinternal=0
                            flagfees=0
                            flagevents=0
                            cResponse = str(dat)
                            print(type(cResponse))
                            welcomeResponse.append(cResponse)
                        elif flaginternal==1:
                            print('inside internal')
                            flagattendance=0
                            flaginternal=0
                            flagclassinternal=0
                            flagfees=0
                            flagevents=0
                            cResponse=str(dat)
                            welcomeResponse.append(cResponse)
                        elif flagclassinternal==1:
                            print('inside class internal')
                            flagattendance=0
                            flaginternal=0
                            flagclassinternal=0
                            flagfees=0
                            flagevents=0
                            cResponse=str(dat)
                            welcomeResponse.append(cResponse)
                        elif flagfees==1:
                            print('inside class internal')
                            cResponse=str(dat)
                            welcomeResponse.append(cResponse)
                        elif flagevents==1:
                            flagattendance=0
                            flaginternal=0
                            flagclassinternal=0
                            flagfees=0
                            flagevents=0
                            print('inside class internal')
                            cResponse=str(dat)
                            welcomeResponse.append(cResponse)
                        else:
                            print('inside normal')
                            flagattendance=0
                            flaginternal=0
                            flagclassinternal=0
                            flagfees=0
                            flagevents=0
                            cResponse=bot(user_response)
                            welcomeResponse.append(cResponse)
                        # print('welcomeResponse',welcomeResponse)

            welcomeTrafficResponse = zip(InputTraffic,welcomeResponse)

            print("user query is",user_response)
            
            print("chat bot response is",cResponse)
            speak_response(cResponse)
            print('welcome traffic response',welcomeTrafficResponse)
            context = {'welcomeTrafficResp':welcomeTrafficResponse} 
            return render(request,'student_signup.html',context) 

    return render(request,'student_signup.html')        

@login_required
def logout_request(request):
    logout(request)
    return redirect('/')

def course(request):
    return render(request,'course.html') 
def admin_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email=='admin@gmail.com' and password=='admin':
            request.session['email']=email
            return redirect('admin_dashboard')
        else:
            alert="<script>alert('Incorrect'); window.location.href='/admin_login/'; </script>"
            return HttpResponse(alert)
    else:
        return render(request,'admin_login.html')    
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')
def user_list(request):
    if 'email' in request.session:
        users=registration.objects.all()
        return render(request,'userlist.html',{'u':users})
def timtable(request):
    return render(request,'timetable.html')
def fees(request):
    return render(request,'fees.html')
def delete_user(request,uid):
    user=registration.objects.get(id=uid)
    user.delete()
    return redirect('user_list')
def edit_user(request, uid):
    user = registration.objects.get(id=uid)
    
    if request.method == 'POST':
        # Update the User fields first and save
        user_instance = user.user
        user_instance.first_name = request.POST.get('firstname')
        user_instance.last_name = request.POST.get('lastname')
        user_instance.email = request.POST.get('email')
        user_instance.save()  # Save the changes made to the User model

        # Now update the registration model fields
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')
        user.adno = request.POST.get('adno')
        user.dep = request.POST.get('dep')
        user.gen = request.POST.get('gen')
        user.save()  # Save the changes made to the Registration model
        
        return redirect('user_list')
    else:
        return render(request, 'edituser.html', {'e': user})
    
    
from django.shortcuts import render
from django.http import JsonResponse
from groq import Groq
import json

# Initialize Groq client with your new API key
client = Groq(api_key="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")

def chatmate(request):
    if request.method == "POST":
        try:
            # Parse incoming JSON data
            data = json.loads(request.body)
            user_input = data.get('message', '')

            # Call Groq API
            response = client.chat.completions.create(
                model="llama3-70b-8192",  # Known working Groq model
                messages=[
                    {"role": "system", "content": "You are StudyMate, a chill chatbot for engineering students. Help with anything they ask!"},
                    {"role": "user", "content": user_input}
                ]
            )
            response_text = response.choices[0].message.content
            return JsonResponse({'response': response_text})
        except Exception as e:
            return JsonResponse({'response': f"Oops, something went wrong: {str(e)}"}, status=500)
    
    # Render the chat page
    return render(request, 'chat.html')


from django.shortcuts import render
from django.http import JsonResponse
import csv
import spacy
from .models import Attendence  # Import your model

# Load NLP model and responses
nlp = spacy.load("en_core_web_sm")
responses = {}
with open('db.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) >= 2:
            responses[row[0].lower()] = row[1]

def teachbot(request):
    if request.method == 'GET' and 'message' in request.GET:
        user_input = request.GET.get('message', '').lower().strip()
        if not user_input:
            return JsonResponse({'response': responses.get('default', 'Hello!')})

        # Step 1: Check for exact or partial keyword match
        best_match = None
        for key in responses.keys():
            if key in user_input or user_input in key:
                best_match = key
                break

        # Step 2: If no direct match, use NLP similarity
        if not best_match:
            doc = nlp(user_input)
            max_similarity = 0.7
            for key in responses.keys():
                key_doc = nlp(key)
                similarity = doc.similarity(key_doc)
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_match = key

        # Step 3: Handle response (database or CSV)
        if best_match == "attendance":
            try:
                words = user_input.split()
                student_name = None
                department = None
                semester = None

                # Parse input for filters
                if "attendance" in words:
                    for i, word in enumerate(words):
                        if word == "attendance" and i + 1 < len(words):
                            # Check for student name (could be multi-word)
                            student_name = " ".join(words[i + 1:]) if i + 1 < len(words) else None
                            break
                        if word in ["cs", "ee", "me"]:  # Department keywords
                            department = word.upper()
                        if word.startswith("semester") or word.isdigit():  # Semester keyword or number
                            semester = word.replace("semester", "").strip() if "semester" in word else word

                # Build database query based on filters
                filters = {}
                if student_name:
                    filters['Name__icontains'] = student_name  # Case-insensitive partial match
                if department:
                    filters['Department'] = department
                if semester:
                    filters['Semester'] = semester

                # Query the database
                if filters:
                    attendance_records = Attendence.objects.filter(**filters)
                else:
                    attendance_records = Attendence.objects.all()[:5]  # Default: up to 5 records

                # Format response
                if attendance_records:
                    response = "Attendance details:\n"
                    for record in attendance_records:
                        response += (f"Name: {record.Name}, Department: {record.Department}, "
                                    f"Semester: {record.Semester}, Register: {record.Register_Number}, "
                                    f"From: {record.From}, To: {record.To}, Status: {record.ta}\n")
                else:
                    response = "No attendance records found for the specified criteria."
            except Exception as e:
                response = f"Error fetching attendance: {str(e)}"
        else:
            response = responses.get(best_match, responses.get('understand', "I didn’t understand that."))

        return JsonResponse({'response': response})

    return render(request, 'teachbot.html')


from django.shortcuts import render, redirect

from .models import Faculty
from django.contrib import messages

def tregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        department = request.POST['department']
        phno = request.POST['phno']
        email = request.POST['email']
        password = request.POST['password']
        if Faculty.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            faculty = Faculty(name=name, gender=gender, department=department, phno=phno, email=email, password=password)
            faculty.save()
            return redirect('login')
    return render(request, 'tregister.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            faculty = Faculty.objects.get(email=email, password=password)
            request.session['femail'] = faculty.email
            request.session['faculty_id'] = faculty.id
            return redirect('teachbot')
        except Faculty.DoesNotExist:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def tprofile(request):
    email=request.session.get('femail')
    faculty = Faculty.objects.get(email=email)
    # faculty = Faculty.objects.get(id=request.session.get('faculty_id'))
    return render(request, 'tprofile.html', {'faculty': faculty})
def thome(request):

    return render(request, 'thome.html')
def edit_profile(request):
    faculty = Faculty.objects.get(id=request.session.get('faculty_id'))
    if request.method == 'POST':
        faculty.name = request.POST['name']
        faculty.gender = request.POST['gender']
        faculty.department = request.POST['department']
        faculty.phno = request.POST['phno']
        faculty.email = request.POST['email']
        if 'profilepic' in request.FILES:
            faculty.profilepic = request.FILES['profilepic']
        faculty.save()
        return redirect('tprofile')
    return render(request, 'edit_profile.html', {'faculty': faculty})

def logout_view(request):
    request.session.flush()
    return redirect('index')

from django.shortcuts import render, redirect
from .models import Event
from django.contrib import messages
from datetime import datetime

# Add Event View
def add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        description = request.POST.get('description')
        if name and date and description:
            Event.objects.create(name=name, date=date, description=description)
            messages.success(request, "Event added successfully!")
            return redirect('view_events')
        else:
            messages.error(request, "All fields are required!")
    return render(request, 'add_event.html')

# View Events View
def view_events(request):
    events = Event.objects.all()
    return render(request, 'view_events.html', {'events': events})

def studentbot(request):
    
    return render(request, 'studentbot.html')
import csv
import os
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings  # To access static/media files

def book_list(request):
    csv_path = os.path.join(settings.BASE_DIR, "Accession Register-reportresults (3).csv")  # Adjust if needed

    books = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Reads as dictionary
        for row in reader:
            books.append({
                "AccNo": row.get("Acc.No", "N/A"),    # Fix column names
                "AccDate": row.get("Acc.Date", "N/A"),
                "Title": row.get("Title", "N/A"),
                "Author": row.get("Author", "N/A"),
                "Publisher": row.get("Publisher", "N/A"),
                "Callno": row.get("Callno", "N/A"),
                "Price": row.get("price", "N/A"),
            })

    # Debugging: Print first row to check if column names are correct
    if books:
        print("First row:", books[0])  

    # Paginate (50 books per page)
    paginator = Paginator(books, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "books.html", {"page_obj": page_obj})


from django.shortcuts import render
from .models import StudentGPA, registration  # Import your registration model

def cgpa(request):
    if request.user.is_authenticated:
        try:
            # Get the user's profile from the registration model
            profile1 = User.objects.get(id=request.user.id)
            # Fetch CGPA using the profile (assuming name or another field links to StudentGPA)
            student = StudentGPA.objects.get(name=profile1.first_name)  # Adjust field as needed
            cgpa = student.cgpa
        except registration.DoesNotExist:
            cgpa = "User profile not found."
        except StudentGPA.DoesNotExist:
            cgpa = "No CGPA record found."
    else:
        cgpa = "User not logged in."
    
    context = {'cgpa': cgpa}
    return render(request, 'cgpa.html', context)