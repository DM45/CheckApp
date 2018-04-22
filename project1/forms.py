from django import forms
from .models import Document


class UpdateDocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('name', 'department', 'last_success_check_date', 'document_file')


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