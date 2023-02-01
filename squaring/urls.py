from django.urls import path
from squaring.views import HelloWorldView, SquareView,WelcomeView

urlpatterns = [
    #squaring/
    #NOTE: in class, the 'path' to the HelloWorldView was the word 'home'. Here, it's empty instead. 
    #How will that change the way that the user will access this url in the browser or in code?
    path('home', HelloWorldView.as_view(), name="home"),
    path('<int:number>', SquareView.as_view()),
    path('', WelcomeView.as_view()),
]
