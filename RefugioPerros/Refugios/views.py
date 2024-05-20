from django.shortcuts import redirect, render
from Refugios.models import Refugio


# Create your views here.
def home(request):
    return render(request, 'home.html')

def agregar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        descripcion = request.POST.get('descripcion')

        nuevo_refugio = Refugio(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            descripcion=descripcion
        )
        nuevo_refugio.save()

        # Redirigir a la lista de refugios
        return redirect('listar')

    return render(request, 'agregarRefugio.html')

def listar(request):
    refugios = Refugio.objects.all()
    return render(request, 'listarRefugio.html', {'refugios': refugios})

def eliminar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        refugio = Refugio.objects.get(nombre=nombre)
        refugio.delete()
        
        return redirect('listar')
    
    return render(request, 'eliminarRefugio.html')

def modificar(request):
    
    return render(request, 'modificarRefugio.html')

def buscar(request):
    if request.GET["refugio"]:
        refugio = Refugio.objects.get(nombre=request.GET["refugio"])
        