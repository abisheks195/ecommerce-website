from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from ecommerce.forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
    "title": "Hi there!"
    }
    if request.user.is_authenticated():
        context["premium_content"] = "YEHHHHHH!";
    return render(request, "home_page.html", context);

def about_page(request):
    context = {
    "title": "This is the about page!"
    }
    return render(request, "home_page.html", context);

def contact_page(request):
    contact_form = ContactForm(request.POST or None);
    context = {
    "title": "This is the contact page!",
    "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data);
        if request.is_ajax():
            return JsonResponse({'message':'Thank you!'});

    if contact_form.errors:
        print(contact_form.cleaned_data);
        errors = contact_form.errors.as_json();
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json');

    # if request.method == "POST":
    #     print(request.POST.get('fullname'));
    #     print(request.POST.get('email'));
    #     print(request.POST.get('content'));
    return render(request, "contact/view.html", context);
