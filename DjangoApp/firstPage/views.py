from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

from firstPage import use_saved_model
# Create your views here.



def index(request):

    context={'a':'HelloWorld!'}
    return render(request,'index.html',context)
    #return HttpResponse({'a':1})

def predictMPG1(request):
    print(request)
    if request.method == 'POST':
        print(request.POST.dict())
        print('stock name:',request.POST.get('mk_stock'))
        if request.POST.get('mk_stock')!="":
            use_saved_model.program(request.POST.get('mk_stock'))
        if request.POST.get('tr_stock')!=None:
            use_saved_model.program(request.POST.get('tr_stock'))




    context={'a':'Hello New World!',
    'stock': request.POST.get('mk_stock')}
    return render(request,'index.html',context)



