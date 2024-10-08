from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.db.models import Sum
from .models import Car, Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

    
# Add Post using class Based view
@method_decorator(login_required,name ='dispatch')
class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')
    def form_valid(self, form):
        form.instance.accounts = self.request.user
        return super().form_valid(form)


@method_decorator(login_required,name ='dispatch')
class EditCarView(UpdateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

    
@method_decorator(login_required,name ='dispatch')
class DeleteCarView(DeleteView):
    model = models.Car
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments 
        context['comment_form'] = comment_form
        return context
    
@method_decorator(login_required,name ='dispatch')
class ProfileView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'order_car.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'data'
   
    def success_view(request):
        return render(request, 'order_car.html')

def buy_car(request,id):
    
    car = Car.objects.get(id= id)
    if car.quantity > 0:
        
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user, car = car)
    
    return redirect('order',id)