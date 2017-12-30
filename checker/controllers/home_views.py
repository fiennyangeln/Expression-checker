from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from checker.controllers import expression_checker

# Create your views here.
def home_page(request):
    param={}
    return render(request,'value.html',param)

def answer_checker(request):
    #if ('value_1' in request.POST and 'value_2' in request.POST):
    res ={}
    res['result']= False
    if request.method == 'POST' :# and 'value_1' in request.POST and 'value_2' in request.POST:
        value = json.loads(request.body.decode("UTF-8"))
        if ('value_1' in value and 'value_2' in value):
            value_1=value['value_1']
            value_2=value['value_2']
            res['result']=expression_checker.check(value_1,value_2)
    return HttpResponse(json.dumps(res),content_type='application/json')
