from django.shortcuts import render , redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout 
from MainApp.models import Contact


#REGISTER_View
def register(request) :
    if request.method == "POST" :
        """ Get Value & Submitting Data """
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #Check Password
        if password == password2 :
            # Check Username if exits or now
            if User.objects.filter(username=username).exists() :
                messages.error(request, 'Username already exist , Try With Another one')
                return redirect('register')
            else :
                if User.objects.filter(email=email).exists() :
                    messages.error(request, 'Email already exist , Try with Another one')
                    return redirect('register')
                else :
                    # return
                    # Save User
                    user = User.objects.create_user(username=username , password=password ,email=email ,first_name=first_name , last_name=last_name)
                    """ Login After REGISTER  """
                    # auth.login(request, user)
                    # messages.success(request, "You're Now Logged!" ) 
                    # return redirect('home')
                    """ REDIRECT USER INTO LOGIN """
                    user.save();
                    messages.success(request, "You're Now Logged")
                    return redirect('login')
        else :
            messages.error(request , 'Passwords Not Match')
            return redirect('register')
    else : 
        return render(request , 'register.html')

# LoginForm
def login(request) :
    if request.method == "POST" :
        """ Submitting DATA """
        username = request.POST['username']
        password = request.POST['password']
        """ Check username & Password """
        user = auth.authenticate(username=username, password=password)
        """ if user is Known in DATABASE """
        if user is not None :
            auth.login(request, user)
            messages.success(request, "You're no loggined")
            return redirect('dashboard')
        else :
            messages.error(request, "Password or Username wrong , try agian!")
            return redirect('login')
    else :
        return render(request , 'login.html')

#LogoutView
def logoutView(request) :
    """ Logout Function """
    logout(request) 
    return redirect('home')

    return render(request , 'login.html')


# USER DASHBOARD

def dashboard(request) :
    """ FILTER RESERVED REALTOR """
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts' : user_contact
    }
    return render(request , 'dashboard.html', context)