from .models import Product,Cart,CartItems, Order, OrderItem
from django.shortcuts import get_object_or_404,redirect,render
# views.py in your checkout app

from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItems.objects.filter(cart=cart)

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        # Create an order and associated order items
        order = Order.objects.create(user=request.user, cart=cart, total_price=total_price)
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )

        # Clear the user's cart after checkout
        cart_items.delete()

        return redirect('order_confirmation')  # Redirect to a confirmation page or another relevant view

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'shop/checkout.html', context)



def Shop(request):
    return render(request,'shop/cart.html')

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user)
    cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')


def remove_from_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    cart=Cart.objects.get(user=request.user)

    cart_item=CartItems.objects.filter(cart=cart,product=product).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

def update_cart(request):
    if request.method=='POST':
        cart=Cart.objects.get(user=request.user)
        for product_id, quantity in request.POST.items():
            if product_id.isdigit() and int (quantity)>0:
                product=get_object_or_404(Product,id=product_id)
                cart_item, created=CartItems.objects.get_or_create(cart=cart,product=product)
                cart_item.quantity=int(quantity)
                cart_item.save()
            elif product_id.isdigit() and int(quantity)==0:
                product= get_object_or_404(Product,id=product_id)
                cart_item= CartItems.objects.filter(cart=cart, product=product).first()
                if cart_item:
                    cart_item.delete()

    return redirect('view_cart')

def view_cart(request):
    cart=Cart.objects.get(user=request.user)
    cart_items= CartItems.objects.filter(cart=cart)
    total_price=sum(item.product.price * item.quantity for item in cart_items)
    context={
        'cart_items': cart_items,'total_price':total_price
    }
    return render (request,'shop/view_cart.html',context)

