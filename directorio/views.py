from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx.shared import Inches

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

#Modelos
from directorio.models import Directorio

#Formularios
from directorio.forms import DirectorioForm

# Create your views here.
@login_required
def home(request):
    instancias = Directorio.objects.all()#.order_by('nombre');

    query = request.GET.get("q")
    if query:
        instancias = instancias.filter(nombre__icontains = query)

    contexto ={
        "directorio" : instancias
    }
    return render(request,'home.html', contexto)

@login_required
def create_directorio(request):
    title = "Nueva Persona"
    form = DirectorioForm(request.POST or None)

    if form.is_valid():
        instancia = form.save(commit = False)
        instancia.user = request.user
        instancia.save()
        return redirect(instancia.get_detail_path())
    contexto = {
        "title" : title,
        "form"  : form
    }

    return render(request,"form_dir.html",contexto)

@login_required
def milista_dir(request):
    lista = Directorio.objects.filter(user_id__exact= request.user.id)

    query = request.GET.get("q")

    if query:
        lista = lista.filter(nombre__icontains = query)
    contexto = {
        'lista' : lista
    }
    return render(request,'milista.html',contexto)

def seleccionar_acuses_mi_lista(request):
    instancias = Directorio.objects.filter(user_id__exact = request.user.id).exclude(status__exact=1)

    mensaje = "Selecciona los acuses de tu lista"

    invocador = "milista"

    if request.POST:
        acuses = request.POST.getlist("acuses")
        document = Document()

        for x in acuses:
            print(x)
            persona = get_object_or_404(Directorio, id= x)
            acuse(document,persona)
            document.add_page_break()

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=acuses.docx'
        document.save(response)

        return response

    contexto = {
        "instancias" : instancias,
        "mensaje" : mensaje,
        "invocador" : invocador
    }
    return render(request,"multiple_acuses.html",contexto)

def seleccionar_acuses_directorio(request):
    instancias = Directorio.objects.all().exclude(status__exact = 1)

    mensaje = "Aqui seleccionas los acuses del directorio general"

    invocador = "directorio"

    if request.POST:
        acuses = request.POST.getlist("acuses")

        document = Document()

        for x in acuses:
            print(x)
            persona = get_object_or_404(Directorio, id= x)
            acuse(document,persona)
            document.add_page_break()

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=acuses.docx'
        document.save(response)

        return response


    contexto = {
        "instancias" : instancias,
        "mensaje"   : mensaje,
        "invocador" : invocador
    }

    return render(request,"multiple_acuses.html",contexto)

@login_required
def edit_directorio(request, id = None):
    persona = get_object_or_404(Directorio,id = id)
    title = "Editando a: %s"%persona.nombre
    form = DirectorioForm(request.POST or None,instance = persona)

    if form.is_valid():
        instancia = form.save(commit = False)
        if instancia.user_id != request.user.id:
            instancia.modificado = request.user.username
        # instancia.user = request.user
        instancia.save()
        return redirect(instancia.get_detail_path())
    contexto = {
        "title" : title,
        "form" : form
    }

    return render(request,"form_dir.html",contexto)

@login_required
def detail_directorio(request, id = None):
    instancia = get_object_or_404(Directorio, id = id)
    contexto = {
        "title": "Detalles",
        "persona" :instancia,
    }

    return render(request,"detalle_dir.html",contexto)

@login_required
def confirm_delete_directorio(request,id = None):
    instancia = get_object_or_404(Directorio, id = id)
    contexto = {
        "persona" : instancia
    }
    return render(request,'confirm_delete.html',contexto)

@login_required
def delete_directorio(request, id=None):
    instancia = get_object_or_404(Directorio, id= id)
    instancia.delete()
    return redirect('directorio:home')

def un_acuse(request,id = None):
    persona = get_object_or_404(Directorio, id = id)
    document = Document()  
    
    acuse(document,persona)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    document.save(response)

    return response

def crear_mi_lista(request):
    instancias = Directorio.objects.filter(user_id__exact = request.user.id)
    # instancias = instancias.filter(status__exact = 2)
    document =Document()

    for persona in instancias:
        document.add_paragraph("%s%s"%(persona.profesion,persona.nombre))

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=lista.docx'
    document.save(response)

    return response

def crear_mis_acuses(request):
    mis_acuses = Directorio.objects.filter(user_id__exact=request.user.id).exclude(status__exact=1)

    document = Document()

    for persona in mis_acuses:
        acuse(document,persona)
        document.add_page_break()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=lista.docx'
    document.save(response)
    return response

def crear_lista_general(request):
    instancias = Directorio.objects.all()
    document =Document()

    for persona in instancias:
        document.add_paragraph("%s%s"%(persona.profesion,persona.nombre))

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=lista.docx'
    document.save(response)

    return response

def acuses_generales(request):
    acuses = Directorio.objects.all().exclude(status__exact=1)

    document = Document()

    for persona in acuses:
        acuse(document,persona)
        document.add_page_break()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=lista.docx'
    document.save(response)
    return response 
# cuerpo del aacuse, recibiendo por parametro el objeto document y los datos de la persona
def acuse(document, persona):
    x = 1;
    while x<=4:
        document.add_paragraph()
        x = x+1
    p1 = document.add_paragraph()
    p1Format = p1.paragraph_format
    p1Format.space_before = Pt(0)
    p1Format.space_after = Pt(0)
    nombre = "%s%s"%(persona.profesion,persona.nombre)
    f = p1.add_run(nombre).font
    f.name = 'Arial'
    f.bold = True
    f.size = Pt(12)
    if persona.pareja:
        strpareja = "\ny %s"%persona.pareja
        fpareja = p1.add_run(strpareja).font
        fpareja.name = 'Arial'
        fpareja.bold = True
        fpareja.size = Pt(12)

    if persona.cargo:
        cargo = persona.cargo
        cargo = cargo.replace('\r','')
        p2 = document.add_paragraph()
        p2Format = p2.paragraph_format
        p2Format.space_before = Pt(0)
        p2Format.space_after = Pt(0)
        f2 = p2.add_run("%s"%cargo).font
        f2.name = "Arial"
        f2.size = Pt(12)
    if persona.direccion:
        direccion = persona.direccion
        direccion = direccion.replace('\r','')
        p3 = document.add_paragraph()
        p3Format = p3.paragraph_format
        p3Format.space_before = Pt(0)
        p3Format.space_after = Pt(0)
        f3 = p3.add_run("%s"%direccion).font
        f3.name = "Arial"
        f3.size = Pt(12)

    x = 1
    while x<=2:
        document.add_paragraph()
        x = x+1
    
    p4 =document.add_paragraph()
    p4Format = p4.paragraph_format
    p4Format.space_before = Pt(0)
    p4Format.space_after = Pt(0)
    p4Format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p4Format.first_line_indent = Inches(0.50)
    f4 = p4.add_run('Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemplo "Contenido aquí, contenido aquí". Estos textos hacen parecerlo un español que se puede leer. Muchos paquetes de autoedición y editores de páginas web usan el Lorem Ipsum como su texto por defecto, y al hacer una búsqueda de "Lorem Ipsum" va a dar por resultado muchos sitios web que usan este texto si se encuentran en estado de desarrollo. Muchas versiones han evolucionado a través de los años, algunas veces por accidente, otras veces a propósito (por ejemplo insertándole humor y cosas por el estilo).').font
    f4.name = 'Arial'
    f4.size = Pt(12)

    x = 1
    while x <=3:
        document.add_paragraph()
        x = x+1
    p5 =document.add_paragraph()
    p5Format = p5.paragraph_format
    p5Format.space_before = Pt(0)
    p5Format.space_after = Pt(0)
    p5Format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    f5 = p5.add_run('__________________________________').font
    f5.name = 'Arial'
    f5.size = Pt(12)    

    p6 =document.add_paragraph()
    p6Format = p6.paragraph_format
    p6Format.space_before = Pt(0)
    p6Format.space_after = Pt(0)
    p6Format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    f6 = p6.add_run('nombre, firma y fecha').font
    f6.name = 'Arial'
    f6.size = Pt(12)

