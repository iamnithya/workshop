from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from register.forms import *
from django.views.generic import ListView


class Home(ListView):
  template_name="index.html"

  def get_queryset(self):
      return Chocolate.objects.all()


class UserRegistrationView(AnonymousRequiredMixin, FormView):
  template_name = "register_user.html"
  authenticated_redirect_url = reverse_lazy(u"home")
  form_class = UserRegistrationForm
  success_url = 'user/success/'


  def form_valid(self, form):
      form.save()
      return FormView.form_valid(self, form)

class addchocolateview(FormView):
      template_name="add_chocolate.html"
      form_class=ChocolateAddform
      success_url='/register/chocolate/success'

      def form_valid(self,form):
          form.save()
          return FormView.form_valid(self,form)