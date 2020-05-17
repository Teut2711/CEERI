from django import forms
from django.utils.safestring import mark_safe


class Form1(forms.Form):
    institute = forms.CharField(label="",
        max_length=200, 
        widget=forms.TextInput, 
        help_text=mark_safe('<small class="form-text text-muted">'
                            '*Send recognition/affiliation certificate in case of private institutes.</small>'))


class Form2(forms.Form):
    project_title = forms.CharField(label="",
        widget=forms.TextInput())


class Form3(forms.Form):

    subjects = forms.MultipleChoiceField(
        label="",
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[("a", 'Animal Sciences & Biotechnology'), ("b", 'Inorganic and Physical Chemistry'),
                 ("c", 'Organic and Medicinal Chemistry'), ("d",
                                                            'Disaster Preparedness'),
                 ("e", 'Earth Sciences'), ("f", 'Mathematical Sciences'),
                 ("g", 'Physical Sciences'), ("h", 'Engineering Sciences')],
    )


class Form4(forms.Form):
    ### not required
    name = forms.CharField(required=False, max_length=100,
                           widget=forms.TextInput())


    
    mobile = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'type': "tel", 'pattern':'[0-9]{4,5}-[0-9]{5, 10}' }))

    telephone = forms.IntegerField(required=False, 
        widget=forms.TextInput(attrs={'type': "tel", 'pattern':'((\+*)(0*|(0 )*|(0-)*|(91 )*)(\d{12}+|\d{10}+))'}))

    fax = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'type': "tel", 'pattern':'[0-9]{10}'}))

    email = forms.EmailField(required=False, )



class Form5(forms.Form):
    
    title = forms.CharField(max_length=100, 
            help_text=mark_safe('<small class="form-text text-muted">' 
            'Prof/Dr/Mr./Ms'),  widget=forms.TextInput())

    name = forms.CharField(max_length=100,
                           widget=forms.TextInput())

    sex = forms.ChoiceField(choices=[('male', "Male"),
                                          ('female', 'Female')],
        widget=forms.RadioSelect(
                                 ))

    address = forms.CharField(max_length=100,
                              widget=forms.TextInput(
                                  ))

    mobile = forms.IntegerField(widget=forms.TextInput(
        attrs={'type': "tel", 'pattern':'[0-9]{10}' }), help_text=mark_safe('<small class="form-text text-muted">'
        'Eg. 9098956756")</small>'))
    
    telephone = forms.IntegerField(
        widget=forms.TextInput(attrs={'type': "tel"}), help_text=mark_safe('<small class="form-text text-muted">'
        'Eg. 0124-4089734</small>'))

    fax = forms.IntegerField(
        widget=forms.TextInput(attrs={'type': "tel"}), help_text=mark_safe('<small class="form-text text-muted">'
        'Eg. 0124-4089734</small>'))

    email = forms.EmailField()

    position = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                ))

    dob = forms.DateField(label="Date of Birth",
                          widget=forms.DateInput( attrs={'type': 'date'}))

    highestdegree = forms.CharField(label="Highest Degree University/Institute", 
                                    max_length=100,
                                    widget=forms.TextInput)

    totaltime = forms.IntegerField(
        label="Total time to be devoted to project(in number of months)",
        min_value=0,
        widget=forms.TextInput(
            attrs={'type': "tel", 'pattern':'[0-9]{10}'}))
