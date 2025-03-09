from django.shortcuts import render, get_object_or_404,HttpResponse
from django.http import JsonResponse
from publisher.models import Catagory, Add_Book  

def bookcatagory(request):
    ob = Catagory.objects.all()
    if request.method == "POST":
        cname = request.POST.get('cname')  
        try:
            category = get_object_or_404(Catagory, c_name=cname)  
            books = Add_Book.objects.filter(c_name=category)  

            book_data = []
            for book in books:
                book_data.append({
                    'book_name': book.bookname,
                    'author_name': book.authorname,
                    'isbn': book.isbn,
                    'price': book.price,
                    'discount':book.discount,
                    'image': book.bookdoc.url,
                    'review': book.review
                })

            return JsonResponse({'data': {'books': book_data}})
        except Catagory.DoesNotExist:  
            return JsonResponse({'data': {'books': []}}) 
    
    return render(request, 'book_catagory.html', {'bdata': ob})


def add_to_cart(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")

        # Check if the cart exists in the session, otherwise initialize it as an empty list
        if "cart" not in request.session:
            request.session["cart"] = []

        cart = request.session["cart"]
        found = False  # Flag to track if the book already exists in the cart

        # Loop through the cart to check if the book already exists
        for item in cart:
            if item["isbn"] == int(isbn):  # Check for the same ISBN
                item["quantity"] += 1  # Increase quantity if found
                found = True
                break

        # If the book is not found in the cart, fetch its details and add it as a new item
        if not found:
            book = Add_Book.objects.filter(isbn=isbn).values(
                "bookname", "authorname", "isbn", "price", "discount", "bookdoc"
            ).first()

            if book:
                book["quantity"] = 1  # Default quantity = 1
                cart.append(book)  # Add the new book to the cart

        # Save the updated cart back to the session
        request.session["cart"] = cart
        request.session.modified = True

        return JsonResponse({"message": "Book added to cart", "cart_size": len(cart)})

    return JsonResponse({"message": "Invalid request"}, status=400)


def view_cart(request):
    cart = request.session.get("cart", [])
    if not cart:
        return render(request, "cart.html", {"message": "Your cart is empty."})
    return render(request, "cart.html", {"cart": cart})


def remove_from_cart(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")
        print(f"Removing book with ISBN: {isbn}")
        
        # Get the current cart from session
        cart = request.session.get("cart", [])
        print(f"Current Cart: {cart}")

        # Find the index of the first occurrence of the book by ISBN
        for book in cart:
            if book["isbn"] == int(isbn):
                cart.remove(book)  # Remove the first matching book
                break  # Exit the loop after removing the first match

        print(f"Updated Cart: {cart}")

        # Save the updated cart back to the session
        request.session["cart"] = cart
        request.session.modified = True

        return JsonResponse({"message": "Book removed from cart", "cart_size": len(cart)})

    return JsonResponse({"message": "Invalid request"}, status=400)




def checkout(request):
    cart = request.session.get("cart", [])
    total_amount = 0  # Initialize total

    for book in cart:
        # Calculate total price
        total_price = book['price'] * book['quantity']
        
        # Calculate discount amount
        discount_amount = (total_price * book['discount']) / 100
        
        # Final price after discount
        final_price = total_price - discount_amount
        
        book['total_price'] = round(final_price, 2)
        total_amount += final_price

    request.session["cart"] = cart  # Save updated cart with prices
    request.session["total_amount"] = round(total_amount, 2)
    request.session.modified = True

    return render(request, "checkout.html", {"cart": cart, "total_amount": round(total_amount, 2)})


def payment(request):
    return HttpResponse('hello')


def cus_home(request):
    cname=request.session.get('name')
    return render(request,'cus_home.html',{'cus_name':cname})


def payment_options(request):
    total_amount = request.session.get("total_amount", 0)

    if total_amount == 0:
        return render(request, "checkout.html", {"error": "Your cart is empty!"})

    return render(request, "payment_options.html", {"total_amount": total_amount})

from django.shortcuts import  redirect

def process_payment(request):
    if request.method == "POST":
        payment_method = request.POST.get("payment_method")
        
        # Store payment method in session (for later use)
        request.session["payment_method"] = payment_method

        if payment_method == "credit_card":
            return redirect("credit_card_payment")  # Redirect to card payment page
        elif payment_method == "paypal":
            return redirect("paypal_payment")  # Redirect to PayPal page
        elif payment_method == "cash_on_delivery":
            return redirect("cod_success")  # Show order confirmation for COD

    return redirect("payment_options")  # If no method selected, go back to selection page
def order_success(request):
    total_amount = request.session.get("total_amount", 0)
    
    # Clear the cart after the order is placed successfully
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True
    
    return render(request, "order_success.html", {'total_amount': total_amount})
def credit_card_payment(request):
    return render(request,'credit_card_payment.html')
def paypal_payment(request):
    return render(request,'paypal_payment.html')
def cod_success(request):
    return render(request,'cod_success.html')


