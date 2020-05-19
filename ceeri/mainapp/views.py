from django.shortcuts import render

from . import forms
from .backend.mainapp import document
from django.http import HttpResponse
from more_itertools import partition
from django.forms.formsets import formset_factory
# Create your views here.


def index(request):

    if request.method == "POST":
        all_forms = {"form1": forms.Form1,
                     "form2": forms.Form2,
                     "form3": forms.Form3,
                     "form4": forms.Form4,
                     "form5": forms.Form5,
                     "form6": formset_factory(forms.Form6, extra=4),
                     }

        for i in range(1, len(all_forms)+1):

            all_forms[f"form{i}"] = all_forms[f"form{i}"](
                prefix=f"form{i}",
                data=request.POST)

        if all(all_forms[i].is_valid() for i in all_forms):
            document.main(all_forms)

        else:
            return HttpResponse(f"<h1>INVALID FORM : CLICK BACK BUTTON TOP LEFT<br>"
                                "{'\n'.join(map(lambda x:x.errors if not x.is_valid() else "", all_forms.values()))}</h1>")

        return HttpResponse("<h1>Sent</h1>")

    all_forms = {"form1": forms.Form1,
                 "form2": forms.Form2,
                 "form3": forms.Form3,
                 "form4": forms.Form4,
                 "form5": forms.Form5,
                 "form6": formset_factory(
                     forms.Form6, extra=4),
                 }
    sections = [f"mainapp/section{i}.html" for i in range(1, len(all_forms)+1)]

    for i in range(1, len(all_forms)+1):
        all_forms[f"form{i}"] = all_forms[f"form{i}"](prefix=f"form{i}")

    return render(request,
                  "mainapp/index.html",
                  context={**all_forms,
                           "sections": sections,

                           "section8": ["Grant agency Title of the project and reference number",
                                        "Duration(from mm/yy to mm/yy)",
                                        "Percentage of time devoted /being devoted/to be devoted, in many months",
                                        "Amount in lakh Rs."],
                           "section9":  [],
                           "section10": [],
                           "section11": [],
                           "section12": [],
                           })
