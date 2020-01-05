from django.shortcuts import render
from Feedbackapp.forms import FeedbackForm
from Feedbackapp.models import FeedbackData
from django.http.response import HttpResponse
import datetime as dt

date1= dt.datetime.now()
def FeedbackView(request):
    if request.method=="POST":
        fform = FeedbackForm(request.POST)
        print(request.POST)
        if fform.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('ratings')
            feedback1= request.POST.get('feedback')
            data = FeedbackData(
                name=name1,
                ratings=rating1,
                feedback=feedback1,
                date=date1
            )
            data.save()
            feedbacks= FeedbackData.objects.all()
            fform= FeedbackForm
            return render(request,'feedbackfile.html',{'fform':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse("User Missed Some values..")
    else:
        fform= FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request,'feedbackfile.html',{'fform':fform,'feedbacks':feedbacks})

