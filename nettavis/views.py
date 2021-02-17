from django.shortcuts import render, get_object_or_404

from .models import Artikkel

# Create your views here.
def nettavis_template(request):
    artikler = Artikkel.objects
    return render(request,'index.html', {'artikler': artikler})

def artikkel_template(request, artikkel_id):
    artikkel = get_object_or_404(Artikkel, pk=artikkel_id)
    return render(request,'artikkel.html', {'artikkel': artikkel})