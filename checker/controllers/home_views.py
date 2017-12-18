from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from checker.controllers import answer_checker

# Create your views here.
def home_page(request):
    param={}
    param['not_complete'] = False
    param['result'] = False
    #if ('input_box_1' in request.POST and 'input_box_2' in request.POST):
    if ('input_box_2' in request.POST):
        print(request.POST)
        #if (request.POST['input_box_1'] == None or request.POST['input_box_2'] == None):
        #if (request.POST['input_box_1'] == '' or request.POST['input_box_2'] == ''):
        if request.POST['input_box_2'] == '':
            param['not_complete']=1
        else:
            param['result']=True
            #TODO: Is this needed?
            #param['input_box_1'] = request.POST['input_box_1']
            param['input_box_2'] = request.POST['input_box_2']

            #value = answer_checker.expression_checker(param['input_box_1'], param['input_box_2'])
            #param['value']=value
        print(param)
        print("aku disini")
    else:
        print("aku disana")
    return render(request,'value.html',param)

def answer_checker(request):
    #if ('value_1' in request.POST and 'value_2' in request.POST):
    res ={}
    if request.method == 'POST' :
        res['result']=True
    else:
        res['result']=False
    return HttpResponse(json.dumps(res),content_type='application/json')
