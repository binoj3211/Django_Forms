from django.views.generic import View, ListView
from django.shortcuts import render, redirect

from myapp.forms import ContactForm
from myapp.models import Contact

class ContactView(View):
    
    def get(self, request):
        form = ContactForm() # Unbound Instantiation
        return render(request, "myapp/contact.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST) # Bound Instantiation
        if form.is_valid():
            instance = form.save()
            return render(request, "myapp/success.html", {"data": instance})
        else:
            return render(request, "myapp/contact.html", {"form": form})

class ContactListView(ListView):
    template_name = "myapp/contact-list.html"
    context_object_name = "records"
    queryset = Contact.objects.all()

class ContactUpdateView(View):

    def get(self, request, id):
        form = ContactForm(instance=Contact.objects.get(id=id))
        return render(request, "myapp/contact.html", {"form": form})
    
    def post(self, request, id):
        form = ContactForm(request.POST, instance=Contact.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("list-contact")
        else:
            return render(request, "myapp/contact.html", {"form": form})
    