from django.shortcuts import render

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        if 'form1' in request.POST:
            name1 = request.POST['name1']
            print('Name1: ',name1)
        if 'form2' in request.POST:
            name2 = request.POST['name2']
            print('Name2: ',name2)
        return render(request, 'index.html')
