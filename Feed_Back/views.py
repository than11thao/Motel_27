from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import sendFeedBack
from Feed_Back.models import FeedBack
# Create your views here.
class RenterFeedBack(TemplateView):
    template_name= "renter_dashboard/partial/feedback.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['send_feed_back_form'] = sendFeedBack(initial={"room":self.request.user.renter.room})
        context['feedbacks']=FeedBack.objects.filter(room = self.request.user.renter.room)
        return context
    
    def post(self, request):
        send_feed_back_form=sendFeedBack(request.POST)
        if send_feed_back_form.is_valid():
            print("valid")
            send_feed_back_form.save()
        else:
            print("invalid")
        return redirect("feedback:renter_feed_back")