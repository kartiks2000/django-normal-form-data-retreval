# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from formapp import forms
# Create your views here.

def index(request):
    myd = {"mytxt" : "this is Kartik..."}
    return render(request,'index1.html',context=myd)

def fm(request):
    form = forms.Formname()

    if request.method == 'POST':

        form = forms.Formname(request.POST)

        if form.is_valid():
            print("form recieved successfully...")
            print("name: " + form.cleaned_data['name'])
            print("email: " + form.cleaned_data['email'])
            print("text: " + form.cleaned_data['text'])



    return render(request,'index2.html',{'form' : form})

