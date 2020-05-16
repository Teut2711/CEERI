from django import forms

class Form1(forms.Form):
    institute = forms.Textarea()

class Form2(forms.Form):
    project_title = forms.Textarea()

class Form3(forms.Form):

    subjects = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[("3a", 'Animal Sciences & Biotechnology'), ("3b", 'Inorganic and Physical Chemistry'),
                ("3c", 'Organic and Medicinal Chemistry'),("3d",  'Disaster Preparedness'),
                ("3e", 'Earth Sciences'), ("3f", 'Mathematical Sciences'),
                ("3g", 'Physical Sciences'), ("3h", 'Engineering Sciences')],
    )



class Form4(forms.Form):

    subjects = forms.Textarea()
    
class Form5(forms.Form):

    subjects = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[("3a", 'Animal Sciences & Biotechnology'), ("3b", 'Inorganic and Physical Chemistry'),
                ("3c", 'Organic and Medicinal Chemistry'),("3d",  'Disaster Preparedness'),
                ("3e", 'Earth Sciences'), ("3f", 'Mathematical Sciences'),
                ("3g", 'Physical Sciences'), ("3h", 'Engineering Sciences')],
    )