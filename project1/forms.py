from django import forms
from .models import Document
from django.contrib.auth.models import User
from project1.choices import *


DOCUMENT_STATUS_LIMIT =  (('CHECKING', 'На проверке'), ('IRRELEVANT', 'Неактуально'))

class UpdateDocumentForm(forms.ModelForm):
	
	class Meta:
		model = Document
		fields = ('name', 'department', 'last_success_check_date', 'document_file', 'status', 'comment')
		labels = {'name':'Название документа', 'department': 'ЦЭС',
		'last_success_check_date': 'Дата последней успешной проверки', 'document_file': 'Файл',
		'status': 'Статус', 'comment': 'Комментарий'}

	def __init__(self, *args, **kwargs):
		groups = kwargs.pop('groups')
		super(UpdateDocumentForm, self).__init__(*args, **kwargs)
#		if groups:
		if 'Controler' in groups.all().values_list('name', flat=True):
			self.fields['status'].choices = DOCUMENT_STATUS_LIMIT

'''
		def __init__(self, user_group, *args, **kwargs):
#			self.request = kwargs.pop('request')
			super(UpdateDocumentForm, self).__init__(*args, **kwargs)
			self.user_group = user_group
			if self.user_group == 'Controler':
				self.fields['status'].choices = DOCUMENT_STATUS_LIMIT
'''
'''
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			if request.user.groups != 'Controler':			
				self.fields['status'].choices = ['Актуально', 'На доработке', 'Неактуально', 'В работе']

	name =  forms.ChoiceField(choices=[(x, x) for x in DOCUMENT_STATUS])

self.fields['status'].choices = ['Actual', 'In work']'''

