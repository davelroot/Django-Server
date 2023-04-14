from django import forms
from django.forms import CharField, Form, ModelChoiceField, Select, TextInput

from .models import Briefingapplication, Briefinglojavirtual, Briefingwebsites


class Briefing_lojavirtualFrom(Form):
	
	class Meta:
		model = Briefinglojavirtual
		fields = '__all__'

		exclude = [
			'turno_id',
			'created',
			'modified'
		]

class Briefing_frontendFrom(Form):
	
	class Meta:
		model = Briefingwebsites
		fields = '__all__'

		exclude = [
			'turno_id',

		]

class Briefing_mobileFrom(Form):
	
	class Meta:
		model = Briefingapplication
		fields = '__all__'

		exclude = [
			'turno_id',

		]











