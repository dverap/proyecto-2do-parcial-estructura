from django.shortcuts import redirect, render,HttpResponse
from .forms import CargoForm
from .models import Cargo

# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>Bienvenido a mi Sitio Web</h1>")
    return render(request, "inicio.html")
# vistas de Cargos
def crearCargo(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("entro por post")
        cargo_form = CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
    else:
        print("entro por get")
    cargo_form = CargoForm()
    cargos = Cargo.objects.filter(estado=True)  
    return render(request,"pages/cargo.html",{'cargoForm':cargo_form,'cargos':cargos  ,'accion':'Crear'})    

def editarCargo(request,id):
    error,cargo_form=None,None
    try:
       cargo = Cargo.objects.get(id=id)
       if request.method == "GET":
           cargo_form = CargoForm(instance=cargo)  
       else:
           cargo_form = CargoForm(request.POST,instance=cargo)   
           if cargo_form.is_valid():
                cargo_form.save()
                return redirect('cargo')
                      
    except Exception as e:
        error=e    
    cargos = Cargo.objects.filter(estado=True)  
    return render(request,"pages/cargo.html",{'cargoForm':cargo_form,'cargos':cargos  ,'accion':'Actualizar'}) 

def eliminarCargo(request,id):  
   cargo = Cargo.objects.get(id=id)
   if request.method == 'POST':
        # eliminacion fisica del registro
        print(cargo)
        cargo.delete()
        # eliminacion logica del registro
        # Cargo.estado=False
        #cargo.save()
        # regresa a la pagina de listado de cargos
        return redirect("cargo")
   return render(request,'pages/eliminar_cargo.html',{'cargo':cargo})  

# vistas de departamentos



# vistas de empleados


# def cargo(request):
#     #return HttpResponse("<h1>Mantenimiento De Cargos...</h1>")
#     return render(request,"pages/cargo.html")

def departamento(request):
    #return HttpResponse("<h1>Mantenimiento De departamentos</h1>")
    return render(request,"pages/departamento.html")
def empleado(request):
    #return HttpResponse("<h1>Mantenimiento De Empleados</h1>")
    return render(request,"pages/empleado.html")

