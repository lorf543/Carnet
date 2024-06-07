from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control, never_cache
from django.contrib import messages
from django.contrib.auth import get_user_model


from .forms import UserCreateForm
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        messages.success(
                request, f'Welcome to work {user}')

        if user is not None:

            login(request, user)
            return redirect('home')

        else:
            messages.success(
                request, 'There was an error Logging, try again.')
            return redirect('login_user')
    else:
        return render(request, 'auth/authenticate/login.html')
    
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def register_user(request):

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(form.errors)
            user = authenticate(request, username=username, password=password)

            # Login the user
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful')
                return redirect('home')
            else:
                messages.error(request, 'Registration failed. Please try again.')
        else:
            print(form.errors)
            messages.error(request, 'Form is not valid. Please check the entered data.')
    else:
        form = UserCreateForm()

    return render(request, 'auth/authenticate/register_user.html', {'form': form})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def log_out(request):
    logout(request)
    messages.success(request, 'You were logout')
    return redirect('login_user')


#________________HTMX__________________

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div class='text-danger bolder'>This username Already exist.</div>")
    else:
        return HttpResponse("<div class='text-success bolder'>This username is available.</div>")