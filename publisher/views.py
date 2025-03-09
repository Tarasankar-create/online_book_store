from django.shortcuts import render,redirect
from.models import Catagory,Add_Book
from django.contrib import messages

def pub_home(request):
    name=request.session.get('pname')
    return render(request,'pub_home.html',{'name':name})

def addbook(request):
    ob = Catagory.objects.all()  # Get all categories
    if request.method == 'POST':
        cname = request.POST['cname']
        
        # Try to get the category, handle the exception if it does not exist
        try:
            category = Catagory.objects.get(c_name=cname)
        except Catagory.DoesNotExist:
            messages.error(request, f"The category '{cname}' does not exist.")  # Show an error message
            return redirect('addbook')  # Redirect to the same page to try again

        bname = request.POST['bname']
        aname = request.POST['aname']
        isbnno = request.POST['isbn']
        bprice = request.POST['bprice']
        dis = request.POST['dis']
        review = request.POST.get('review', '')
        
        # Check if a file is uploaded
        if 'bimage' in request.FILES:
            image = request.FILES['bimage']
        else:
            image = None  # Handle the case where no file is uploaded
        
        # Create the book entry in the Add_Book model
        obj = Add_Book.objects.create(
            c_name=category,
            bookname=bname,
            authorname=aname,
            isbn=isbnno,
            price=bprice,
            discount=dis,
            bookdoc=image,
            review=review
        )

        messages.success(request, f"Book '{bname}' added successfully!")  # Success message
        return redirect('addbook')  # Redirect after successful addition
    
    return render(request, 'add_book.html', {'cdata': ob})  # Pass categories to template

def viewbook(request):
    ob=Add_Book.objects.all()
    if request.method=='POST':
        btn=request.POST['btn']
        isbnno=request.POST['isbnno']
        if btn =='Delete':
            ob=Add_Book.objects.get(isbn=isbnno).delete()
            ob=Add_Book.objects.all()
            return redirect('viewbook')
        if btn =='Edit':
            try:
                obj=Add_Book.objects.get(isbn=isbnno)
                return render(request,'edit.html',{'data':obj})
            except Exception:
                return redirect('viewbook')
    return render(request,'viewbook.html',{'bookdata':ob})


def update(request):
    if request.method == 'POST':
        isbnno = request.POST['isbnno']
        bname = request.POST['bname']
        bprice = request.POST['bprice']
        aname = request.POST['aname']
        dis = request.POST['dis']
        # image_file=request.FILES['image']
        
        # Get the object and update its fields
        obj = Add_Book.objects.get(isbn=isbnno)
        obj.bookname = bname
        obj.price = bprice
        obj.authorname = aname
        obj.discount = dis
        
        # Save the updated object
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            obj.bookdoc = image_file
        
        # Save the updated object
        obj.save()

        return redirect('viewbook')
    
    return render(request, 'edit.html')
