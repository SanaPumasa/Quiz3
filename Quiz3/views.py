from django.shortcuts import render
from CompanyPortal.models import jobOpenings

def jobOpenings_detail_view(request, id=1):
    obj = jobOpenings.objects.get(id=id)
    print(obj)
    context = {
        'object': obj,
    }
    return render(request, 'detail_view.html', context)

def jobOpenings_list_view(request):
    qs = jobOpenings.objects.all()
    print(qs)
    context = {
        'query': qs,
    }
    return render(request, 'list_view.html', context)

def accounts(request, id=1):
    obj = accounts.objects.get(id=id)
    print(obj)
    context = {
        'object': obj
    }
    return render(request, 'register.html')