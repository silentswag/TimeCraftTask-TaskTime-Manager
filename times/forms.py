from django import forms

class TaskForm(forms.Form):
    Prichoices = [('top', 'Top'), ('medium', 'Medium'), ('low', 'Low')]
    id= forms.ChoiceField(choices=Prichoices,widget=forms.Select(attrs={'class': 'form-control'}))
    task_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    duration = forms.DurationField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}))
