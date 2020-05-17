from django.shortcuts import render

from . import forms
from django.http import HttpResponse
# Create your views here.


def index(request):

    if request.method == "POST":

        print(request.POST)
        return HttpResponse("<h1>Sent</h1>")

    form1 = forms.Form1(prefix="form1")
    form2 = forms.Form2(prefix="form2")
    form4 = forms.Form4(prefix="form3")
    form3 = forms.Form3(prefix="form4")
    form5 = forms.Form5(prefix="form5")

    

    return render(request,
                  "mainapp/index.html",
                  context={'form1': form1,
                           'form2': form2,
                           'form3': form3,
                           "form4": form4,
                           'form5': form5,

                           'sections': [
                               f"mainapp/section{i}.html"
                               for i in list(range(1, 5+1))
                           ],

                           "section1": [],
                           "section2": [],
                           
                           "section4": [],
                           "section5": ['Title', 'Name', 'Sex', 'Full Official Address',
                                        'Mobile', 'Telephone', 'Fax', 'Email', 'Position', 'Date of birth',
                                        'Highest Degree University/Institute', 'Date',
                                        'Total time to be devoted to project (in man months per year)'],
                           "section6": list(range(4)),
                           "section7": list(range(4)),
                           "section8": ["Grant agency Title of the project and reference number",
                                        "Duration(from mm/yy to mm/yy)",
                                        "Percentage of time devoted /being devoted/to be devoted, in many months",
                                        "Amount in lakh Rs."],
                           "section9":  [],
                           "section10": [],
                           "section11": [],
                           "section12": [],
                           })
