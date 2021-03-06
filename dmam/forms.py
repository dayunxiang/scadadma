# -*- coding: utf-8 -*-

from django import forms
from django.utils.dateparse import parse_datetime
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget


from entm.models import Organization
from .models import DMABaseinfo
import datetime

class DMACreateForm(forms.ModelForm):

    class Meta:
        model = DMABaseinfo
        fields = ['dma_no','dma_name','creator','create_date']



class DMABaseinfoForm(forms.ModelForm):
    belongto  = forms.CharField()

    class Meta:
        model = DMABaseinfo
        fields = ['dma_no','pepoles_num','acreage','user_num','pipe_texture','pipe_length','pipe_links','pipe_years','pipe_private','ifc','aznp','night_use','cxc_value']

    def __init__(self,*args,**kwargs):
        super(DMABaseinfoForm, self).__init__(*args, **kwargs)

        # self.fields['password'].widget = forms.PasswordInput()
        self.fields['belongto'].initial = self.instance.belongto.name
        
    def clean_belongto(self):
        organ_name = self.cleaned_data.get("belongto")
        print('organ_name:',organ_name)
        organ = Organization.objects.get(name=organ_name)
        return organ

class AssignStationForm(forms.Form):
    stationassign = forms.CharField()

    # class Meta:
    #     model = DMABaseinfo
    #     fields = ('dma_no',)


class StationAssignForm(forms.ModelForm):
    stationassign = forms.CharField()

    class Meta:
        model = DMABaseinfo
        fields = ('dma_no',)

