from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import CustomUser


def add_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to a user list or success page
    else:
        form = CustomUserForm()

    return render(request, 'users/add_user.html', {'form': form})


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

