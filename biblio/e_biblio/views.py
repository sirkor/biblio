from django.shortcuts import render, render_to_response, RequestContext, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from biblio import settings
from e_biblio.forms import DocumentAddForm
from e_biblio.models import Document
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView


def index(request):
    args = {'document': Document.objects.all()}
    return render_to_response('index.html', args, context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('thanks.html', context=RequestContext(request))


@login_required
def add_document(request):
    if request.POST:
        form = DocumentAddForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('/thanks/')
    else:
        form = DocumentAddForm()
    return render_to_response('add_document.html', {'form': form}, context_instance=RequestContext(request))


def del_document(request, id=0):
    del_id = Document.objects.get(id = id)
    del_id.delete()
    return redirect('/')


def update_view(request, id=0):
    if request.POST:
        name = request.POST['name']
        format = request.POST['format']
        special = request.POST['special']
        document_type = request.POST['document_type']
        doc = Document.objects.get(id = id)
        doc.name = name
        doc.format = format
        doc.special = special
        doc.document_type = document_type
        doc.save()
        return redirect('/')
    else:
        return render_to_response('update_document.html', context_instance=RequestContext(request))


def search_view(request):
    if request.GET:
        name = request.GET['name']
        format = request.GET['format']
        special = request.GET['special']
        document_type = request.GET['document_type']
        doc = Document.objects.filter(name__icontains = name, format__icontains= format, special__icontains = special,
                                      document_type__icontains = document_type)
        return render_to_response('search.html', {'document': doc}, context_instance=RequestContext(request))
    else:
        return render_to_response('search.html', context_instance=RequestContext(request))