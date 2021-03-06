from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta
from django.urls import reverse


class DocumentQuerySet(models.QuerySet):
	def tomsk(self):
		return self.filter(department='ТЦЭС')

	def parabel(self):
		return self.filter(department='ПЦЭС')

	def kedrovij(self):
		return self.filter(department='КЦЭС')

	def strejevoy(self):
		return self.filter(department='СЦЭС')

	def irrelevant(self):
		return self.filter(status='IRRELEVANT')

	def irrelevant_tomsk(self):
		return self.filter(status='IRRELEVANT').filter(department='ТЦЭС')

	def irrelevant_parabel(self):
		return self.filter(status='IRRELEVANT').filter(department='ПЦЭС')

	def irrelevant_kedrovij(self):
		return self.filter(status='IRRELEVANT').filter(department='КЦЭС')

	def irrelevant_strejevoy(self):
		return self.filter(status='IRRELEVANT').filter(department='СЦЭС')


class Document(models.Model):

	TOMSK = 'ТЦЭС'
	PARABEL = 'ПЦЭС'
	KEDROVIJ = 'КЦЭС'
	STREJEVOY = 'СЦЭС'

	DOCUMENT_DEPARTMENT = [TOMSK, PARABEL, KEDROVIJ, STREJEVOY]

	DOCUMENT_STATUS = (('CHECKING', 'На проверке'), ('IRRELEVANT', 'Неактуально'),
		('ACTUAL', 'Актуально'), ('INWORK', 'В работе'), ('REWORK', 'На доработке'))

	name = models.CharField(max_length=50)
	department = models.TextField(choices=[(x, x) for x in DOCUMENT_DEPARTMENT])
	check_period = models.IntegerField(choices=((1,'1'), (3,'3'), (6,'6'), (12,'12')))
	last_success_check_date = models.DateField(default=None, null=True)
	objects = DocumentQuerySet.as_manager()
	next_check_date = models.DateField()
	status = models.TextField(default='IRRELEVANT', choices=DOCUMENT_STATUS)
	document_file = models.FileField(blank=True)
	comment = models.TextField(blank=True)


#	def get_absolute_url(self):
#		return reverse('document_edit', kwargs={'pk': self.pk})


	def change_abilitys(self):
		today = datetime.date.today()
		if today >= self.next_check_date:
			self.next_check_date = self.next_check_date + relativedelta(months=self.check_period)
			self.save(update_fields=['next_check_date'])

		if (((self.next_check_date - relativedelta(days=10) > today) and (
			self.next_check_date - relativedelta(days=10) - relativedelta(months=self.check_period) < self.last_success_check_date))
		or ((self.next_check_date - relativedelta(days=10) < today) and 
			self.last_success_check_date > self.next_check_date - relativedelta(days=10))):
	   		self.status = 'ACTUAL'
	   		self.save(update_fields=['status'])
		elif ((self.next_check_date - relativedelta(days=10) < today) and (
			self.last_success_check_date > (self.next_check_date - relativedelta(days=10) - relativedelta(months=self.check_period)))):
			self.status = 'INWORK'
			self.save(update_fields=['status'])
		elif self.status != 'INWORK' or self.status != 'CHECKING':
#		else:
			self.status = 'IRRELEVANT'
			self.save(update_fields=['status'])
		else: 
			self.status = 'IRRELEVANT'
			self.save(update_fields=['status'])

'''
	def actual_button(self):
		today = datetime.date.today()
		self.last_success_check_date = today
		self.save(update_fields=['last_success_check_date'])
		self.status = 'Актуально'
		self.save(update_fields=['status'])
'''
'''

class BaseUser(models.Model):
	CONTROLLER = 'ЦО'
	PERFORMER = 'ЦЭС'

	USER_ROLE = [CONTROLLER, PERFORMER]

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.TextField(choices=[(x, x) for x in USER_ROLE], blank=True)


'''
