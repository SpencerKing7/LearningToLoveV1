from django.shortcuts import render
# from .models import Response


# Create your views here.
def indexPageView(request) :
    return render(request, 'pages/index.html')

def storyPageView(request) :
    return render(request, 'pages/story.html')

def faqPageView(request) :
    return render(request, 'pages/questions.html')

def learnMorePageView(request) :
    return render(request, 'pages/learnmore.html')

# def askMePageView(request) :
#     return render(request, 'app/askMe.html')