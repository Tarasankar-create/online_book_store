from django.shortcuts import render, get_object_or_404, HttpResponse
from publisher.models import Catagory, Add_Book
from django.http import JsonResponse


# Publisher Registration View
def pub_register(request):
    return render(request, 'publisher_register.html')


# Customer Home View
def cus_home(request):
    cname = request.session.get('cname')
    return render(request, 'cus_home.html', {'cus_name': cname})


# Book Category View
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
                    'discount': book.discount,
                    'image': book.bookdoc.url,  # Get image URL
                    'review': book.review
                })

            return JsonResponse({'data': {'books': book_data}})
        except Catagory.DoesNotExist:
            return JsonResponse({'data': {'books': []}})
    
    return render(request, 'book_catagory.html', {'bdata': ob})


# Add Book to Cart
def add_to_cart(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")

        # Initialize cart if not present
        if "cart" not in request.session:
            request.session["cart"] = []

        cart = request.session["cart"]
        found = False

        # Check if the book is already in the cart and increase quantity
        for item in cart:
            if item["isbn"] == isbn:
                item["quantity"] += 1
                found = True
                break

        # If the book is not in the cart, add it
        if not found:
            book = Add_Book.objects.filter(isbn=isbn).first()  # Get the book object directly
            if book:
                # Store the book's details, including image URL
                cart_item = {
                    "bookname": book.bookname,
                    "authorname": book.authorname,
                    "isbn": book.isbn,
                    "price": book.price,
                    "discount": book.discount,
                    "image": book.bookdoc.url,  # Get image URL
                    "review": book.review,
                    "quantity": 1  # Default quantity
                }
                cart.append(cart_item)

        # Save updated cart session
        request.session["cart"] = cart
        request.session.modified = True
        return JsonResponse({"message": "Book added to cart", "cart_size": len(cart), "updated_cart": cart})

    return JsonResponse({"message": "Invalid request"}, status=400)


# View Cart
def view_cart(request):
    cart = request.session.get("cart", [])
    return render(request, "cart.html", {"cart": cart})


# Remove Book from Cart
from django.http import JsonResponse
from django.shortcuts import render, redirect

def remove_from_cart(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")
        cart = request.session.get("cart", [])

        # Remove the item with the matching ISBN
        cart = [item for item in cart if item['isbn'] != isbn]

        # Save the updated cart session
        request.session['cart'] = cart
        request.session.modified = True

        # Return a success message and updated cart size
        return JsonResponse({
            "message": "Book removed from cart",
            "cart_size": len(cart),
            "updated_cart": cart  # Return the updated cart so that you can update the frontend
        })

    return JsonResponse({"message": "Invalid request"}, status=400)


# Checkout View
def checkout(request):
    cart = request.session.get("cart", [])
    if not cart:
        return render(request, "cart.html", {"error": "Your cart is empty!"})

    return render(request, "checkout.html", {"cart": cart})


# Payment View (stub)
def payment(request):
    return HttpResponse('hello')
