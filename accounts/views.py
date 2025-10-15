from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from fastfoodapp.emails import send_welcome_email


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "login sucess")
            return redirect('/')

        else:
            messages.error(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name
                )
                user.save()
                print("User created")

                # ✅ Send welcome email
             #   send_welcome_email(user)

                messages.success(request, 'Registration successful! Check your email for a welcome message.')
                return redirect('login')
        else:
            messages.error(request, "Passwords mismatch")
            return redirect('signup')

    return render(request, 'signup.html')


# password change function
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")

        # check old password
        if not request.user.check_password(old_password):
            messages.error(request, "Old password is incorrect.")
            return redirect("profile")

        # check new password match
        if new_password1 != new_password2:
            messages.error(request, "New passwords do not match.")
            return redirect("profile")

        # save new password securely
        request.user.set_password(new_password1)
        request.user.save()

        logout(request)

        # ✅ Store success message for next page load
        messages.success(request, "Password updated successfully. Please login again.")

        return redirect("login")

    return render(request, "profile.html")
