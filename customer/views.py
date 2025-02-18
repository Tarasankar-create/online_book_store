from django.shortcuts import render,get_object_or_404
from publisher.models import Catagory
from publisher .models import Add_Book
from django.http import JsonResponse



def pub_register(request):
    return render(request,'publisher_register.html')

def cus_home(request):
    cname=request.session.get('cname')
    return render(request,'cus_home.html',{'cus_name':cname})

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
    
    return render(request, 'book_catagory.html',{'bdata':ob})

def add_to_cart(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")

        if "cart" not in request.session:
            request.session["cart"] = []

        cart = request.session["cart"]
        found = False

        # Check if the book is already in the cart and increase quantity
        for item in cart:
            if item["ISBN_No"] == isbn:
                item["quantity"] += 1
                found = True
                break

        # If the book is not in the cart, add it
        if not found:
            book = Add_Book.objects.filter(ISBN_No=isbn).values(
                "Book_name", "Author_name", "ISBN_No", "Book_price", "Discount", "Book_image"
            ).first()
            if book:
                book["Book_image"] = book["Book_image"]  # Ensure image URL is stored
                book["quantity"] = 1  # Default quantity = 1
                cart.append(book)

        # Save updated cart session
        request.session["cart"] = cart
        request.session.modified = True
        return JsonResponse({"message": "Book added to cart", "cart_size": len(cart)})

    return JsonResponse({"message": "Invalid request"}, status=400)


def view_cart(request):
    cart = request.session.get("cart", [])
    return render(request, "cart.html", {"cart": cart})


def remove_from_cart(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")
        cart = request.session.get("cart", [])

        cart = [book for book in cart if book["ISBN_No"] != isbn]

        request.session["cart"] = cart
        request.session.modified = True
        return JsonResponse({"message": "Book removed from cart", "cart_size": len(cart)})
    
    return JsonResponse({"message": "Invalid request"},status=400)