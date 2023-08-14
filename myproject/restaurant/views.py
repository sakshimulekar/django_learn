from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from .forms import DishForm
from .models import Dish,Orders
from django.contrib.auth.views import LoginView
from .forms import YourRegistrationForm  # Import your custom form
from .decorators import staff_required,customer_required,login_required
from django.contrib import messages
from .forms import PlaceOrderForm
# from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = YourRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user object but don't save it yet
            is_staff = form.cleaned_data.get('is_staff')  # Get the is_staff value from the form
            if is_staff:
                user.is_staff = True  # Set the user as staff if is_staff is True
            else:
                user.is_staff = False  # Set the user as non-staff if is_staff is False
            user.save()  # Save the user object with updated staff status
            # Additional processing (if needed)
            return redirect('restaurant:login')  # Redirect to login page after registration
    else:
        form = YourRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    dishes = Dish.objects.all()  # Fetch all dishes from the database
    context = {'dishes': dishes}
    return render(request, 'zomato/home.html', context)


def menu(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            dishes = Dish.objects.all()  # Display all dishes for staff members
        else:
            dishes = Dish.objects.filter(available=True)  # Display only available dishes for customers
    else:
        # Handle the case when the user is not authenticated (e.g., display a guest menu)
        dishes = Dish.objects.filter(available=True)  # Display only available dishes for unauthenticated users
    return render(request, 'zomato/menu.html', {'dishes': dishes})

@login_required
def create_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant:menu')  # Redirect to the menu page after successful upload
    else:
        form = DishForm()
    
    return render(request, 'zomato/create_dish.html',{'form': form}) 

@login_required
def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('restaurant:menu')
    else:
        form = DishForm(instance=dish)
    
    return render(request, 'zomato/edit_dish.html', {'form': form, 'dish': dish})

@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    
    if request.method == 'POST':
        dish.delete()
        return redirect('restaurant:menu')
    
    return redirect('restaurant:menu')  # Redirect back to menu if accessed via GET

@login_required
def place_order(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.username
            order.status = 'received'
            order.save()
            order.order_dishes.add(dish)
            messages.success(request, 'Order placed successfully!')
            return redirect('restaurant:menu')
    else:
        form = PlaceOrderForm()
    
    return render(request, 'zomato/place_order.html', {'form': form, 'dish': dish})


@login_required
def staff_orders(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()

    orders = Orders.objects.filter(staff_member=request.user)
    context = {'orders': orders}
    return render(request, 'restaurant/staff_orders.html', context)


# views.py

def my_orders(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        dish_id = request.POST.get('dish_id')
        action = request.POST.get('action')

        order = get_object_or_404(Orders, id=order_id)
        dish = get_object_or_404(Dish, id=dish_id)

        if action == 'remove':
            order.order_dishes.remove(dish)

    orders = Orders.objects.filter(customer=request.user)
    context = {'orders': orders}
    return render(request, 'restaurant/my_orders.html', context)


def remove_dish(request, order_id, dish_id):
    order = get_object_or_404(Orders, id=order_id)
    dish = get_object_or_404(Dish, id=dish_id)
    order.order_dishes.remove(dish)
    return redirect('my_orders')
