from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

import json
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
# Create your views here.

from django.shortcuts import render

def about_us(request):
    return render(request, 'about.html')



def contact_us(request):
    return render(request, 'contact-us.html')


def home(request):
    return render(request, 'index.html')
    # if 'name' in request.session:
    #     request.session.modified = True
    #     data = Products.objects.all()
    #     # return JsonResponse(data, safe=False)
    # else:
    #     response = redirect('login')
    #     return response



def registration(request):
    # frm = RegistrationForm(request.POST)
    # if frm.is_valid():
    #     nm = frm.cleaned_data['username']
    #     pw = frm.cleaned_data['password']
    #     em = frm.cleaned_data['email']

        # if User.objects.filter(username = nm).first():
        #     messages.error(request, "This username is already taken")
        #     return render(request, 'register.html')
        # reg = User.objects.create_user(username=nm, password=pw, email=em)
        # reg.save()
        # return render(request, 'login.html',{'form':frm})
    # else:
    #     frm = RegistrationForm()
    #     return render(request, 'register.html',{'form':frm})


    if request.method == 'POST':
        print("Register")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return render(request, 'register.html')
        print(username, email, password )

        reg = User.objects.create_user(username=username, password=password, email=email)
        reg.save()
        return redirect('/login/')
    else:
        # frm = RegistrationForm()
        return render(request, 'register.html')
    



def login(request):
    Users=User.objects.all()
    print(Users)
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Validate username and password
        # print(username, password, Users[3].password ,"data")

        user = authenticate(username = username, password = password)
        print(user, "username")
        if user is not None:
            print("ok")
            auth.login(request, user)
            request.session['name'] = 'OkaySession'
            return redirect('/products/')
        else:
            print("not ok")
            error_message = "Invalid username or password."
        
        return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/login/')


def addProducts(request):
    data = Products.objects.all()
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            category = request.POST.get('category')
            images = request.FILES.getlist('image')

            product = Products.objects.create(name=name, desc=description)
            # product.save()

            for image in images:
                Image.objects.create(product=product, image=image)

            # imagesArray = []
            # for image in images:
            #     imagesArray.append(image)

            # image_paths_str = ','.join(str(path) for path in imagesArray)

            # product = Products(name=name, disc=description, img= image_paths_str)
            # product.save()

            # print(name, description, images, request.POST)

            # for image in images:
            #         product.create(img=image)


            return render(request, 'addProduct.html', {'data': data})
            # response = redirect('/')
            # return response
        else:
            return render(request, 'addProduct.html', {'data': data})
    else:
        return render(request, 'pageNotAvailable.html')

        






def products(request):
    data = Products.objects.all()
    print(data)
    # for product in data:
    #     print(product.img.split(','))
    #     product.image_paths = product.img.split(',')

    return render(request, 'products.html', {'data': data})

def jsonProductdata(request):
    products = list(Products.objects.all())
    data = {
        'products': [
            {
                'id': product.id,
                'name': product.name,
                'desc': product.desc,
                'category': product.category,
                'image': product.images.first().image.url if product.images.first() else None
            }
            for product in products
        ]
    }
    return JsonResponse(data, safe=False)

def product(request, id):
    data = Products.objects.filter(id=id)
    # print(data, "sjufhi")

    # for product in data:
    #     print(product.img.split(','))
    #     product.image_paths = product.img.split(',')
    return render(request, 'product.html', {'data': data})


def deleteProduct(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    return redirect('addProduct')



def enquirySubmit(request, product_id):
    product = Products.objects.get(id=product_id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        message = request.POST.get('message')
        Name = first_name + ' ' + last_name
        print("Data:",first_name, last_name, email)

        subject = 'Enquiry from {}'.format(first_name)
        email_body = 'Name: {}\nEmail: {}\ncontact_no: {}\nMessage: {}\nProduct Name: {}\nProduct Description: {}'.format(Name, email,contact_no, message, product.name, product.desc)
        send_mail(subject, email_body, 'patilvb1999@gmail.com', ['patilvb1999@gmail.com'])

        user_subject = 'Enquiry Confirmation'
        user_email_body = 'Dear {},\n\nThank you for your enquiry. We will get back to you shortly.'.format(first_name)
        send_mail(user_subject, user_email_body, 'sender@example.com', [email])
    
        return JsonResponse({'message': 'Enquiry submitted successfully.'})
    else:
        return render(request, 'product.html')


def enquiry_submit(request, id):
    # product = Products.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        message = request.POST.get('message')
        # Compose the email message
        Name = first_name + ' ' + last_name
        print(Name, email, message, contact_no)

        # Send the email to the owner

        # subject = 'Enquiry from {}'.format(first_name)
        # email_body = 'Name: {}\nEmail: {}\ncontact_no: {}\nMessage: {}\nProduct Name: {}\nProduct Description: {}'.format(Name, email,contact_no, message, product.name, product.desc)
        # send_mail(subject, email_body, 'patilvb1999@gmail.com', ['patilvb1999@gmail.com'])


        # Send a confirmation email to the user

        # user_subject = 'Enquiry Confirmation'
        # user_email_body = 'Dear {},\n\nThank you for your enquiry. We will get back to you shortly.'.format(first_name)
        # send_mail(user_subject, user_email_body, 'sender@example.com', [email])

        return redirect('products')
    else:
        return render(request, 'enquiry.html')