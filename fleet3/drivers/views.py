from datetime import date, datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from drivers.forms import BookOfDriverForm
from drivers.models import DriverCertificatesModel, DriversModel
from vehicles.forms import BridgeDateForm, BridgeForm, SearchForm




class AddDriverView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = DriversModel
    fields = '__all__'
    template_name = 'add_driver.html'
    success_url = '/adddriver/'
    success_message = 'Dodano kierowce do bazy danych'




class UpdateDriverView(LoginRequiredMixin, UpdateView):
    model = DriversModel
    fields = '__all__'
    template_name = 'edit_driver.html'
    success_url = '/drivers/'




class DeleteDriverView(LoginRequiredMixin, View):
    def get(self, request, id):
        employee = DriversModel.objects.get(id=id)
        employee.delete()
        return redirect('/drivers/')




class ShowDriversView(LoginRequiredMixin, View):
    def get(self, request):
        drivers = DriversModel.objects.all()
        note = f"Kierowców w bazie {len(drivers)}"
        return render(request, 'show_drivers.html', {'drivers': drivers, 'note': note})




class EditDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_edit_driver.html', {'form':form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            object = DriversModel.objects.filter(id=form.cleaned_data['id'])
            if object.exists():
                return redirect(f'/editdriver/{object[0].id}')
            else:
                info = 'Brak kierowcy o takim ID'
                return render(request, 'bridge_edit_driver.html', {'form': form, 'info': info})





class DeleteDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_del_driver.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            if DriversModel.objects.filter(id=id).exists():
                return redirect(f'/deletedriver/{id}')
            else:
                info = "Brak kierowcy o podanym ID"
                return render(request, 'bridge_del_driver.html', {'form': form, 'info':info})




class SearchPersonView(LoginRequiredMixin, View):
    def get(self, request):
        form = SearchForm(request.GET)
        form.is_valid()
        text = form.cleaned_data.get('text', '')
        result = DriversModel.objects.filter(Q(firstname__icontains=text)|Q(lastname__icontains=text))
        note = f"wyszukano {len(result)}"
        ctx ={'form': form,
            'drivers': result,
             'note': note}
        return render(request, 'show_drivers.html', ctx)  




class DetailsDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_details_driver.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            if DriversModel.objects.filter(id=form.cleaned_data['id']).exists():
                object = DriversModel.objects.get(id=form.cleaned_data['id'])
                return redirect(f'/detailsofdriver/{object.id}')
            else:
                info = 'Brak kierowcy o takim ID'
                return render(request, 'bridge_details_driver.html', {'form': form, 'info':info})


       

class BookOfDriverView(LoginRequiredMixin, View):
    def get(self, request, id):
        driver = DriversModel.objects.get(id=id)
        today = date.today()
        return render(request, 'bookdriver.html', {'driver': driver,
                                                   'today': today})




class BookOfDriverEditView(LoginRequiredMixin, View):
    def get(self, request, id):
        driver_ = DriversModel.objects.get(id=id)
        today = date.today()
        if DriverCertificatesModel.objects.filter(driver=driver_).exists():
            unit = DriverCertificatesModel.objects.get(driver=driver_)
            form = BookOfDriverForm(instance=unit)
        else:
            form = BookOfDriverForm()
        ctx = {'form': form, 'driver': driver_, 'today': today}
        return render(request, 'bookdriverform.html', ctx)
    def post(self,request, id):
        unit = DriversModel.objects.get(id=id)
        object, created = DriverCertificatesModel.objects.get_or_create(driver=unit)
        form = BookOfDriverForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/detailsofdriver/{id}')





class BridgeDatePersonView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeDateForm()
        return render(request, 'dedline_bridge.html', {'form': form})
    def post(self, request):
        form = BridgeDateForm(request.POST)
        if form.is_valid():
            date2 = form.cleaned_data['date2']
            return redirect(f'/dedlineperson/{date2}')
        else:
            info = "Nieprawidłowe dane"
            return render(request, 'dedline_bridge.html', {'form': form, 'info': info})




class DedlinePersonView(LoginRequiredMixin, View):
    def get(self, request, date_string):
        dedline = datetime.strptime(date_string, "%Y-%m-%d")
        dedline = datetime.date(dedline)
        drivers = DriversModel.objects.filter(
                Q(certyficate__driver_licence_enddate__lte=dedline)|
                Q(certyficate__kwalifikacja_data_konc__lte=dedline)|
                Q(certyficate__ADR_data_konc__lte=dedline)
                )
        note = f"Kierowców z granicznymi terminami {len(drivers)}"
        return render(request, 'show_drivers.html', {'drivers': drivers, 'note': note})