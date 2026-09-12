from django.shortcuts import render

# Create your views here.
def v1_app2(request):
    return render(request, 'app2/vista1_app2.html')

def v2_app2(request):
    return render(request, 'app2/vista2_app2.html')