import csv,io
from django.shortcuts import render
from .forms import Predict_Form

from accounts.models import UserProfileInfo
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse
from django.contrib import messages
from generate.P import  Generate

from staticfg import CFGBuilder
from generate.PDA import PDA
from graphviz import Digraph
from itertools import combinations


@login_required(login_url='/')
def PredictRisk(request,pk):
    predicted = False
    predictions={}
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(UserProfileInfo, pk=pk)

        if form.is_valid():


            print("Before------")
            generator_temp=Generate('CFG.py')
            generator_temp.build_Path(generator_temp.cfg,1)


            print("Hell0-------")




            pred = form.save(commit=False)





            pred.profile = profile

            pred.save()
            predicted = True



    if predicted:
        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})

    else:
        form = Predict_Form()

        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})
