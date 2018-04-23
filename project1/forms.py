from django import forms
from .models import Document
from django.contrib.auth.models import User


class UpdateDocumentForm(forms.ModelForm):
	ACTUAL = 'Актуально'
	IRRELEVANT = 'Неактуально'
	REWORK = 'На доработке'
	CHECKING = 'На проверке'

	DOCUMENT_STATUS_LIMIT = [ACTUAL, IRRELEVANT, REWORK, CHECKING]

	class Meta:
		model = Document
		fields = ('name', 'department', 'last_success_check_date', 'document_file', 'status')
		labels = {'name':'Название документа', 'department': 'ЦЭС',
		'last_success_check_date': 'Дата последней успешной проверки', 'document_file': 'Файл',
		'status': 'Статус'}

		def __init__(self, *args, **kwargs):
			groups = kwargs.pop('groups')
			super(UpdateDocumentForm, self).__init__(*args, **kwargs)
			if groups == 'Controler':
				self.fields['status'].choices = DOCUMENT_STATUS_LIMIT
'''
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			if request.user.groups != 'Controler':			
				self.fields['status'].choices = ['Актуально', 'На доработке', 'Неактуально', 'В работе']

	name =  forms.ChoiceField(choices=[(x, x) for x in DOCUMENT_STATUS])

self.fields['status'].choices = ['Actual', 'In work']'''

