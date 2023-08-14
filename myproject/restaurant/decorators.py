from functools import wraps
from django.shortcuts import redirect

def _staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page
    return _wrapped_view

staff_required = _staff_required

def _login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('restaurant:login')  # Redirect to the login page
    return _wrapped_view

login_required = _login_required

def _customer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('restaurant:menu')  # Redirect to the menu page for staff
    return _wrapped_view

customer_required = _customer_required
