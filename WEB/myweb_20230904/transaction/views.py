import time
from django.db import transaction
from django.shortcuts import render
from transaction.models import Emp


def home(request):
    return render(request, 'transaction/index.html')


#@transaction.atomic()
def insert(request):
    start = time.time()
    Emp.objects.all().delete()

    for i in range(1, 1001):
        if i == 500:
            emp = Emp(empno='500번', ename='name' + str(i), deptno=i)
            emp.save()
        else:
            emp = Emp(empno=i, ename='name' + str(i), deptno=i)
            emp.save()
    end = time.time()
    runtime = end - start
    cnt = Emp.objects.count()
    return render(request, 'transaction/index.html',
                  {'cnt': cnt, 'runtime': f'{runtime:.2f}초'})


def list(request):
    empList = Emp.objects.all().order_by('empno')
    return render(request, 'transaction/list.html', {'empList': empList, 'empCount': len(empList)})
