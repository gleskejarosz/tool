from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, TimeInput

from gemba.models import SHIFT_CHOICES, HOUR_CHOICES, DowntimeModel, Pareto

TODAY = datetime.today().strftime('%d-%m-%Y')


class ParetoDetailForm(forms.Form):
    good = forms.IntegerField(label="Packed Inners")


class ParetoTotalQtyDetailForm(forms.Form):
    output = forms.IntegerField(label="Total Output")
    good = forms.IntegerField(label="Total Good parts")

    def clean(self):
        result = super().clean()
        if not self.errors:
            if result["output"] <= result["good"]:
                raise ValidationError("Output should be more than good", code='invalid')


class DowntimeAdd(forms.Form):
    downtime = forms.ModelChoiceField(queryset=DowntimeModel.objects.all().order_by("code"))
    minutes = forms.IntegerField()


class DowntimeMinutes(forms.Form):
    minutes = forms.IntegerField(min_value=0)


class ScrapQuantity(forms.Form):
    qty = forms.IntegerField(min_value=0)


class NewPareto(forms.Form):
    shift = forms.ChoiceField(choices=SHIFT_CHOICES)
    hours = forms.ChoiceField(choices=HOUR_CHOICES)
    ops = forms.IntegerField()


class ParetoUpdateForm(forms.ModelForm):
    class Meta:
        model = Pareto
        fields = ["pareto_date", "shift", "ops", "hours", "time_stamp"]
        labels = {
            "time_stamp": "Shift started at",
            "ops": "Operators",
            "hours": "Shift length (hours)",
        }

        widgets = {
            'pareto_date': DateInput(attrs={"type": "date"}),
            'time_stamp': TimeInput(format='%H:%M'),
        }


class NotScheduledToRunUpdateForm(forms.ModelForm):
    class Meta:
        model = Pareto
        fields = ["not_scheduled_to_run"]

