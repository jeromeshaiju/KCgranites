from email.message import EmailMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Send an email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = "Name:  "+name+" \nEmail: "+email+"\n\nMESSAGE\n"+form.cleaned_data['message']
            print(name, email, message)
            send_mail(
                f'New Contact Form Submission from name: {name} , email:{email}',
                message,
                email,
                ["jeromeshaijukc2007@gmail.com"], 
                fail_silently=False,
            )
            
            return render(request, 'index.html')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

from django.http import HttpResponse

def about(request):
    return render(request, 'about.html')

def gallery(request):
    gallery_items = [
        {'title': 'Project Title 1', 'description': 'Description of the project.', 'image': 'images/gallery1.jpg'},
        {'title': 'Project Title 2', 'description': 'Description of the project.', 'image': 'images/gallery2.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},
        {'title': 'Project Title 3', 'description': 'Description of the project.', 'image': 'images/gallery3.jpg'},

        # Add more items as needed
    ]
    return render(request, 'gallery.html', {'gallery_items': gallery_items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Send an email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = "Name:  "+name+" \nEmail: "+email+"\n\nMESSAGE\n"+form.cleaned_data['message']
            print(name, email, message)
            send_mail(
                f'New Contact Form Submission from name: {name} , email:{email}',
                message,
                email,
                ["jeromeshaijukc2007@gmail.com"], 
                fail_silently=False,
            )
            
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

