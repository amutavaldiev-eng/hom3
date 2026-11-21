from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *

def register(request):
    if request.method == 'POST':
        data = request.POST
        CustomUser.objects.create_user(
            username=data.get('username'),
            password=data.get('password'),
            first_name=data.get('first_name'),
            phone=data.get('phone'),
            photo=request.FILES.get('photo')
        )
        return redirect('loginn')
    return render(request, 'registration.html')


def loginn(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            request,
            username=data.get('username'),
            password=data.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

    
    
@login_required
def logout_user(request):
    logout(request)
    return redirect('loginn')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def home(request):
    categories = Category.objects.all()
    games = Games.objects.order_by('date')
    return render(request, 'home.html', {'categories': categories,'games': games})


@login_required
def game_see(request, id):
    game = get_object_or_404(Games, id=id)
    return render(request, 'game_see.html', {'game': game})


@login_required
def matches(request):
    q = request.GET.get('q')
    category = request.GET.get('category')
    games = Games.objects.all()
    if category:
        games = games.filter(category_id=category)
    if q:
        games = games.filter(Q(teams__team1__icontains=q) | Q(teams__team2__icontains=q))
    games = games.order_by('date')
    return render(request, 'matches.html', {'games': games})


@login_required
def order_ticket(request, id):
    game = get_object_or_404(Games, id=id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0 and quantity <= game.tickets_count:
            Order.objects.create(
                user=request.user,
                game=game,
                quantity=quantity
            )
            game.tickets_count -= quantity
            game.save()
            return redirect('my_orders')
    return render(request, 'order.html', {'game': game})



@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})



@login_required
def cancel_order(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    if order.status != 'cancelled':
        game = order.game
        game.tickets_count += order.quantity
        game.save()
        order.status = 'cancelled'
        order.save()
    return redirect('my_orders')

