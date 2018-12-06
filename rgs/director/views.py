from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Document
from .forms import UploadFileForm

def index(request):
	form = UploadFileForm
	return render(request, "director/index.html", {"form": form})

class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context