from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bill
from .forms import CreateBillForm, EditBillForm
from User.models import Renter
import datetime
import json

# Create your views here.
class BillSite(LoginRequiredMixin, TemplateView):
    template_name = "manage_bill/dashboard.html"
    login_url = 'home:login'
    create_bill_form = CreateBillForm

    def get(self, request, month = None):
        context = self.get_context_data(month)
        return self.render_to_response(context)
    
    def get_context_data(self, month= None, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print("month: ",)
        if month== None:
            bills=Bill.objects.all()
        else:
            bills= Bill.objects.filter(date__month=month)
        context['create_bill_form'] = self.create_bill_form
        context['bills'] = bills
        return context
    
    def post(self, request):
        if request.is_ajax():
            form = self.create_bill_form(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"valid": True})
            else:
                error_dict = form.errors.items()
                error_dict= json.dumps(dict(error_dict))
                return JsonResponse({"valid":False, 'errors': error_dict})


class EditBillSite(LoginRequiredMixin,TemplateView):
    template_name="manage_bill/edit_bill.html"
    login_url='home:login'
    
    def get_context_data(self,id):
        bill=Bill.objects.get(id=id)
        context=super().get_context_data()
        context['id']=id
        initial_form_data={}
        try:
            for field in EditBillForm().fields.keys():
                initial_form_data.update({field:getattr(bill,field)}) 
        except:
            initial_form_data={}
            
        initial_form_data['date']=datetime.datetime.strftime(initial_form_data['date'],'%d/%m/%Y')  
        context['edit_form']=EditBillForm(initial=initial_form_data)
        return context
    
    def post(self,request,id):
        bill_instance=Bill.objects.get(id=id)
        form=EditBillForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            try:
                for field in EditBillForm().fields.keys():
                    if hasattr(bill_instance,field):
                        setattr(bill_instance,field,cd[field])
            
            except:
                return HttpResponse("ko xac dinh")
            bill_instance.save()
        else:
            return HttpResponse("not valid")
        return redirect("bill:bill_site")
  

def delete_bill(request, id):
    Bill.objects.get(id=id).delete()
    return JsonResponse({'valid':'true'})

class BillOfRenterSite(TemplateView):
    template_name = "renter_dashboard/partial/bill.html"
    
    def get(self,request,date= None):
        Renter.objects
        if not Bill.objects.filter(room=request.user.renter.room).exists():
            return HttpResponse("Hiện tại phòng không có hóa đơn")
        else:
            return self.render_to_response(self.get_context_data(date))
        
    def get_context_data(self, date= None):
        room = self.request.user.renter.room
        context = super().get_context_data()
        bills = Bill.objects.filter(room=room).order_by("-date")

        if date!=None:
            date_cvt = datetime.datetime.strptime(date, "%Y-%m").date()
            month = date_cvt.month
            year = date_cvt.year
            try:
                bill = bills.get(date__month=month, date__year=year)
            except:
                bill=bills.first()
                context['message']="Ngày được chọn không có hóa đơn"
        else:
            bill= bills.first()

        context['bills']= bills
        context['bill'] = bill

        return context

            


