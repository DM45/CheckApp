from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Document
from .forms import UpdateDocumentForm


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
	form_class = UpdateDocumentForm
	success_url = '/'

	def get_form_kwargs(self, **kwargs):
		kwargs = super().get_form_kwargs(**kwargs)
		kwargs['groups'] = self.request.user.groups
		return kwargs


'''
	def get_form_kwargs(self):
		kwargs = super(DocumentUpdate, self).get_form_kwargs()
		kwargs['user_group'] = self.request.user.groups
		return kwargs
'''
'''
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['topic'].queryset = ContactTopic.objects.filter(
            is_active=True,
        )

'''

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