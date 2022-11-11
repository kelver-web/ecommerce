from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . forms import ContactForm

User = get_user_model()

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            body = render_to_string('contact.txt', form.cleaned_data)
            mail.send_mail('Confirmação de contato', 
                            body,
                            'kelverwt@gmail.com',
                            ['kelverwt@gmail.com', form.cleaned_data['email']])

            messages.success(request, 'Seu contato foi enviado com sucesso!')
            return HttpResponseRedirect(reverse('contact'))
        
        else:
            return render(request, 'contact.html', {'form': form })
    else:
        form = ContactForm()
    
        return render(request, 'contact.html', {'form': form})
