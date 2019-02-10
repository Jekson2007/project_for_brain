#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#import tkinter
import newmnk as mnk # import quadratic aproximation
#import ast
import itertools

#first_sample = ast.literal_eval(input('Enter the first selection, separated by commas : ')) # input first sample
#second_sample = ast.literal_eval(input('Enter the second selection, separated by commas : ')) # input second sample

def two_dictionars_with_max_and_min_function(x,y):
    ''' the function returns two dictionaries with data of the best and worst variants of the combination of two samples, namely the variables of the quadratic function a, b, c and their sequence.'''
    
    combx = list(itertools.permutations(x)) # make list combinations first sample
    comby = list(itertools.permutations(y)) # make list combinations second sample
    n=0 # start for counter
    b=[90] # default error for worst aproximation
    b1=[0] # default error for best function
    d={'%':(),'a':(),'b':(),'c':()} # dictionary with function and two samples for best aproximation
    d1={'%':(),'a':(),'b':(),'c':()} # dictionary with function and two samples for WORST aproximation
    for var in combx:
        n+=1 # counter
        for var_two in comby:
            function = mnk.myfirstclass(var,var_two) # this is class where we can change need funktion
            a = function.kvadrat()# this we can change need funktion

            s = a[3] # error aproximation
            if s < b[0]: # comparison error aproximation and writing dictionary 'd'
                b[0]=s
                d['a']=a[0]
                d['b']=a[1]
                d['c']=a[2]
                d['first']=var
                d['second']=var_two
                d['%']=s
                
            else:
                pass
            if s > b1[0]: # comparison error aproximation and writing dictionary 'd1'
                b1[0]=s
                d1['a']=a[0]
                d1['b']=a[1]
                d1['c']=a[2]
                d1['first']=var
                d1['second']=var_two
                d1['%']=s
                
            else:
                pass
    return d,d1

def drawGrafic(first_sample, second_sample):

    s = two_dictionars_with_max_and_min_function(first_sample,second_sample)

    DictionaryWithBestVar = s[1]
    DictionaryWithWorstVar = s[0]

    x = DictionaryWithBestVar['first']
    y = DictionaryWithBestVar['second']


    def BestQuadraticRegression(var):
        a = DictionaryWithBestVar['a']
        b = DictionaryWithBestVar['b']
        c = DictionaryWithBestVar['c']
        function_to_var = a*(var**2) + b*var + c
        return function_to_var

    def WorstQuadraticRegression(var):
        a = DictionaryWithWorstVar['a']
        b = DictionaryWithWorstVar['b']
        c = DictionaryWithWorstVar['c']
        function_to_var = a*(var**2) + b*var + c
        return function_to_var

    def ForPrintFormula(dictionary):# for print lable into diagrame
        var_a = format(dictionary['a'], '.2f') # for print variation 'a' only 2 number after zero
        var_b = format(dictionary['b'], '.2f') # for print variation 'b' only 2 number after zero
        var_c = format(dictionary['c'], '.2f') # for print variation 'c' only 2 number after zero
        var_percent = format(dictionary['%'], '.2f') # for print variation 'error' only 2 number after zero
        return var_a, var_b, var_c, var_percent

    xnew=np.linspace(np.min(x),np.max(x),100) # genarate variation 'x', values 100 elements

    y_worst=[WorstQuadraticRegression(var) for var in xnew] # solution of the worst equation with genereted variations 'x'
    y_best=[BestQuadraticRegression(var) for var in xnew] # solution of the best equation with genereted variations 'x'

    sample,best_var,worst_var = plt.plot(first_sample,second_sample,'o',xnew,y_worst, xnew, y_best) # for draw two grafics with our dot from samples

    plt.xlabel(u'First_sample') # name lable for abcisa
    plt.ylabel(u'Second_sample') # name lable for ordinate

    plt.legend((worst_var, best_var),(
        u'f(x)={a}x$^2$+{b}x+{c} error {var_percent}%'.format(
            a=ForPrintFormula(DictionaryWithBestVar)[0],
            b=ForPrintFormula(DictionaryWithBestVar)[1], 
            c=ForPrintFormula(DictionaryWithBestVar)[2], 
            var_percent=ForPrintFormula(DictionaryWithBestVar)[3]), 
        u'f(x)={a}x$^2$+{b}x+{c} error {var_percent}%'.format(
            a=ForPrintFormula(DictionaryWithWorstVar)[0],
            b=ForPrintFormula(DictionaryWithWorstVar)[1], 
            c=ForPrintFormula(DictionaryWithWorstVar)[2], 
            var_percent=ForPrintFormula(DictionaryWithWorstVar)[3], 
        loc='best')
        )
    )

    plt.grid(True) # gradueted my diagrame
    plt.savefig('My_grafic')# our diagrame is saves
    plt.show() # draw diagrame
