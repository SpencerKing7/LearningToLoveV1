from django.urls import path
from .views import indexPageView, storyPageView, faqPageView, learnMorePageView


urlpatterns = [
    path('learnmore/', learnMorePageView, name='learnmore'),
    path('questions/', faqPageView, name='questions'),
    path('story/', storyPageView, name='story'),
    path('', indexPageView, name='index'),
]

