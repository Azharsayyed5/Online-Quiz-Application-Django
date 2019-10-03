from django.urls import path,include
from Questions import views

urlpatterns = [
    path('test/', views.test),
    path('selectSubject/', views.selectSubject),
    path('PlayQuiz/', views.playQuiz),
    path('signup/', views.register),
    path('login/',views.login),
    path('validate',views.validate)
]
