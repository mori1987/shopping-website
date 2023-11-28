from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views import View


class contact(View):
    def get(self,request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')  # یک URL پس‌مانی برای نمایش پیام موفقیت ایجاد کنید
        else:
            form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})
