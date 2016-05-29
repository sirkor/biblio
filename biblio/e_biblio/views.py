from django.shortcuts import render, render_to_response, RequestContext, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.static import serve

from biblio import settings
from e_biblio.forms import DocumentAddForm
from e_biblio.models import Document
from django.shortcuts import get_object_or_404

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


def give_file(request, filename):
    link = 'files/' + filename

    f = open(link, 'rb')
    return HttpResponse(f, mimetype='application/octet-stream')


