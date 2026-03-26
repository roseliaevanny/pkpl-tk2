from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'nama_kelompok': 'ac3b',
    }
    
    return render(request, 'main.html', context)