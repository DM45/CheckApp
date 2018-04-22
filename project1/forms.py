from django import forms
from .models import Document
from django.contrib.auth.models import User


class UpdateDocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('name', 'department', 'last_success_check_date', 'document_file', 'status')

		def __init__(self, *args, **kwargs):
			super(UpdateDocumentForm, self).__init__(*args, **kwargs)
			if request.user.groups == 'Controler':			
				self.fields['status'].choices = ['Актуально', 'На доработке', 'Неактуально', 'В работе']

'''
class DocumentForm(forms.ModelForm):
	class Meta:
		models = Document
		fields = ('name', 'department', 'last_check_date', 'check_period')

#		def document_new(request):
#    		if request.method == "POST":
#        		form = DocumentForm(request.POST)
#        		if form.is_valid():
#            		document = form.save(commit=False)
#            		post.save()
#            	return redirect('post_detail', pk=post.pk)
#    		else:
#        		form = DocumentForm()
#    	return render(request, 'blog/post_edit.html', {'form': form})'''