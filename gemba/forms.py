from django import forms

from gemba.models import SHIFT_CHOICES, HOUR_CHOICES
from tools.models import JobModel


class ParetoDetailForm(forms.Form):
    job = forms.ModelChoiceField(queryset=JobModel.objects.all().order_by("name"))
    qty = forms.IntegerField()
    good = forms.IntegerField()


class DowntimeMinutes(forms.Form):
    minutes = forms.IntegerField(min_value=0)


class DowntimeMinutesJob(forms.Form):
    minutes = forms.IntegerField(min_value=0)
    job = forms.ModelChoiceField(queryset=JobModel.objects.all().order_by("name"))


class ScrapQuantity(forms.Form):
    qty = forms.IntegerField(min_value=0)


class ScrapQuantityJob(forms.Form):
    qty = forms.IntegerField(min_value=0)
    job = forms.ModelChoiceField(queryset=JobModel.objects.all().order_by("name"))


class AssignShift(forms.Form):
    shift = forms.ChoiceField(choices=SHIFT_CHOICES)
    hours = forms.ChoiceField(choices=HOUR_CHOICES)
