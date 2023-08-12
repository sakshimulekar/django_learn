from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

menu = [
    {"id":1,
     "name":"pizza",
     "image":"https://b.zmtcdn.com/data/pictures/2/18935632/ee6ca53d353d7887991ce147907df42f_o2_featured_v2.jpg",
     "price":150,
     "available":True
    },
    {"id":2,
     "name":"burger",
     "image":"https://images.deliveryhero.io/image/fd-my/LH/n97c-hero.jpg",
     "price":250,
     "available":True
    },
    {"id":3,
     "name":"Etalian_Sandwich",
     "image":"https://media.gettyimages.com/id/1186934750/photo/italian-sandwich-with-roasted-red-peppers.jpg?s=612x612&w=gi&k=20&c=2Ksuu_h-EttGn2kGueEoYihfd0hepuFsgLSjlU0vMic=",
     "price":200,
     "available":True
    },
    {"id":4,
     "name":"springs roll",
     "image":"https://media.gettyimages.com/id/876292200/photo/beef-taquito-platter.jpg?s=2048x2048&w=gi&k=20&c=aoouvp76AkM6bUfgMNJMzLBce8xDrvjPQ0175z5D7pA=",
     "price":100,
     "available":False
    },
    {"id":5,
     "name":"paneer cheesy Toast",
     "image":"https://media.gettyimages.com/id/1394791667/photo/tandoori-paneer-cheese-toast.jpg?s=1024x1024&w=gi&k=20&c=OfR84eGV9lZaP4Wqh1Ylz9kANHCpePwPdkjCje8Eq_4=",
     "price":150,
     "available":False
    },
]

def menu_list(request):
    return render(request, 'menu_list.html', {'menu': menu})

from django.shortcuts import render, redirect
from .forms import CreateItemForm  # Import your form class

def create_item(request):
    global menu
    
    if request.method == 'POST':
        form = CreateItemForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            price = form.cleaned_data['price']
            available = form.cleaned_data['available']
            
            new_item = {
                'id': len(menu) + 1,
                'name': name,
                'image': image,
                'price': price,
                'available': available
            }
            
            menu.append(new_item)
            
            return redirect('menu_list')
    else:
        form = CreateItemForm()
        
    return render(request, 'create_item.html', {'form': form})



def edit_item(request, item_id):
    if request.method == 'POST':
        for item in menu:
            if item['id'] == item_id:
                item['name'] = request.POST['name']
                item['price'] = float(request.POST['price'])
                item['available'] = True if request.POST.get('available') else False
                break  # Exit the loop after updating the item
        return redirect('menu_list')  # Redirect to the menu list page
    else:
        item = get_menu_item_by_id(item_id)  # Implement this function to retrieve the item by ID from the menu list
        if item:
            return render(request, 'edit_item.html', {'item': item})
        else:
            return HttpResponse('Menu item not found')

def get_menu_item_by_id(id):
    for item in menu:
        if item["id"] == id:
            return item
        
    return None

def del_item(request, item_id):
    item = get_menu_item_by_id(item_id)
    if item:
        menu.remove(item)  # Assuming menu is your dictionary

    return redirect('menu_list')