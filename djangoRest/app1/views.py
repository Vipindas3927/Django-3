from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class First(View):
    def get(self, request):
        return HttpResponse('Good Morning')


# inheritance
class FirstClass(View):
    cls1 = "This is First class content"
    def get(self, request):
        return HttpResponse(self.cls1)

class SecondClass(FirstClass):
    cls2 = "This is Second class content"
    def get(self, request):
        return HttpResponse(self.cls1+"<br>"+self.cls2)

class ThirdClass(SecondClass):
    cls3 = "This is Third class content"
    def get(self, request):
        return HttpResponse(self.cls1+"<br>"+self.cls2+"<br>"+self.cls3)

class FourthClass:
    cls4 = "This is Forth class content"
    def get(self, request):
        return HttpResponse(self.cls4)

class FifthClass(FirstClass, FourthClass):
    cls5 = "This is Fifth class content"
    def get(self, request):
        return HttpResponse(self.cls1+"<br>"+self.cls4+"<br>"+self.cls5)

class SixthClass(ThirdClass, FifthClass):
    cls6 = "This is Sixth class content"
    def get(self, request):
        return HttpResponse(self.cls1+"<br>"+self.cls2+"<br>"+self.cls3+"<br>"+self.cls4+"<br>"+self.cls5+"<br>"+self.cls6)

class SeventhClass(FirstClass):
    cls7 = "This is Seventh class content"
    def get(self, request):
        return HttpResponse(self.cls1+"<br>"+self.cls7)

class EighthClass(FirstClass):
    cls8 = "This is Eighth class content"
    def get(self, request):
        return HttpResponse(self.cls1+"<br>"+self.cls8)
