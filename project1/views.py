from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Document
#from .forms import UpdateDocumentForm


class DocumentsView(ListView):
	template_name = 'project1.html'
	model = Document
	paginate_by = None

	def get_context_data(self, **kwargs):
		context = super(DocumentsView, self).get_context_data(**kwargs)
		context['irrelevant_documents'] = self.object_list.irrelevant()
		context['tomsk_ces'] = self.object_list.tomsk()
		context['parabel_ces'] = self.object_list.parabel()
		context['kedrovij_ces'] = self.object_list.kedrovij()
		context['strejevoy_ces'] = self.object_list.strejevoy()
		context['irrelevant_tomsk'] = self.object_list.irrelevant_tomsk()
		context['irrelevant_parabel'] = self.object_list.irrelevant_parabel()
		context['irrelevant_kedrovij'] = self.object_list.irrelevant_kedrovij()
		context['irrelevant_strejevoy'] = self.object_list.irrelevant_strejevoy()
		return context


class DocumentUpdate(UpdateView):
	template_name = 'document_form.html'
	model = Document
	fields = ['name', 'department', 'last_success_check_date', 'document_file']
	success_url = '/'


#	form = UpdateDocumentForm
'''
	def upload_file(request):
		if request.method == 'POST':
			form = UpdateDocumentForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
			return redirect('/')
		else:
			form = UpdateDocumentForm()
			return render(request, 'document_form', {'form': form})
'''