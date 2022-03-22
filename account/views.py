from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile

# Create your views here.

customUser = get_user_model


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            return redirect('account:profile_edit', pk=new_user.id)
        return render(request, self.template_name, {'form': form})


class ProfileEditView(UpdateView):
    model = Profile
    fields = ('phone_no', 'address', 'city', 'state', 'country')
    template_name = 'account/profile_edit.html'
    context_object_name = 'form'
