from django import forms
from django.utils.safestring import mark_safe


class Form1(forms.Form):
    institute = forms.CharField(label="",
                                max_length=300,
                                widget=forms.TextInput,
                                help_text=mark_safe('<small class="form-text text-muted">'
                                                    '*Send recognition/affiliation certificate'
                                                    ' in case of private institutes.</small>'))


class Form2(forms.Form):
    project_title = forms.CharField(label="",
                                    widget=forms.TextInput)


class Form3(forms.Form):

    subjects = forms.MultipleChoiceField(
        label="",
        widget=forms.CheckboxSelectMultiple,
        choices=[("a", 'Animal Sciences & Biotechnology'),
                 ("b", 'Inorganic and Physical Chemistry'),
                 ("c", 'Organic and Medicinal Chemistry'),
                 ("d", 'Disaster Preparedness'),
                 ("e", 'Earth Sciences'), ("f", 'Mathematical Sciences'),
                 ("g", 'Physical Sciences'), ("h", 'Engineering Sciences')])


class Form4(forms.Form):
    ### not required
    name = forms.CharField(label="Name", required=False, max_length=50,
                           widget=forms.TextInput)

    mobile = forms.CharField(label="Mobile No.", max_length=15, required=False, widget=forms.TextInput(
        attrs={'type': "tel"}))

    telephone = forms.CharField(label="Telephone No.",max_length=15,
                                widget=forms.TextInput(attrs={'type': "tel"}),
                                help_text=mark_safe('<small class="form-text text-muted">'
                                                    'Eg. 0124-4089734</small>'))

    fax = forms.CharField(label="Fax",max_length=15, required=False, widget=forms.TextInput(
        attrs={'type': "tel"}))

    email = forms.EmailField(label="E-mail Address",required=False)


class Form5(forms.Form):

    title = forms.ChoiceField(
        choices=[('prof', 'Prof'),  ('dr', 'Dr'),
                 ('mr', 'Mr.'),  ('ms', 'Ms.')])

    name = forms.CharField(max_length=100,
                           widget=forms.TextInput)

    sex = forms.ChoiceField(choices=[('M', "Male"),
                                     ('F', 'Female')],
                            widget=forms.RadioSelect)

    address = forms.CharField(max_length=100,
                              widget=forms.Textarea(attrs={"rows":"4"}))

    mobile = forms.CharField(max_length=15,
                             widget=forms.TextInput(
                             attrs={'type': "tel"}),
                             help_text=mark_safe('<small class="form-text text-muted">'
                                                 'Eg. 9098956756</small>'))

    telephone = forms.CharField(max_length=15,
                                widget=forms.TextInput(attrs={'type': "tel"}),
                                help_text=mark_safe('<small class="form-text text-muted">'
                                                    'Eg. 0124-4089734</small>'))

    fax = forms.CharField(max_length=15,
                          widget=forms.TextInput(attrs={'type': "tel"}),
                          help_text=mark_safe('<small class="form-text text-muted">'
                                              'Eg. 0124-4089734</small>'))

    email = forms.EmailField()

    position = forms.CharField(max_length=100,
                               widget=forms.TextInput)

    dob = forms.DateField(label="Date of Birth",
                          widget=forms.DateInput(
                              attrs={'type': 'date'}))

    highestdegree = forms.CharField(label="Highest Degree University/Institute",
                                    max_length=200,
                                    widget=forms.TextInput)

    totaltime = forms.IntegerField(
        label="Total time to be devoted to project(in number of months)",
        min_value=0,
    )
