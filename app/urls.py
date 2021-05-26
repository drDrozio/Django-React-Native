from django.urls import path
from .import views
from .views import ClassView

urlpatterns = [
    path('testFunction',views.testFunction),
    path('classview',ClassView.as_view())
] 