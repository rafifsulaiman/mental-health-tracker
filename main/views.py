from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306222771',
        'name' : 'Rafif sulaiman',
        'class' : 'PBP C'
    }
    return render(request, "main.html", context)