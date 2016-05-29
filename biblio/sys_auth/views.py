from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib import auth


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        auth.login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


def logout(request):
    auth.logout(request)
    return redirect("/")