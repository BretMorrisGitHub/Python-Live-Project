from django.shortcuts import render

# Create your views here.
def CookinGadget_home(request):
    # render function takes argument - request
    # and returns HTML as response
    return render(request, 'CookinGadget/CookinGadget_home.html')



