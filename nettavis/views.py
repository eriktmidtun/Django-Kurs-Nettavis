from django.shortcuts import render

# Create your views here.
def nettavis_template(request):
    return render(request,'index.html')