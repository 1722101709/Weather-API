from django.shortcuts import render
from . import services


def weather(request):
    if request.method == 'POST':
        query = request.POST['query']
        query = query[0].upper() + query[1:]
        response, code = services.get_data(query)
        flag = True if code == 200 else False
        data = {}
        if flag:
            data = {'data' : response['forecast']['forecastday']}
            for i in range(7):
                data['data'][i].update({'id' : i+1})
        data.update({'flag' : flag})
        data.update({'area' : query})
        return render(request, 'weather.html', data)
    else:
        return render(request, 'weather.html')


def home(request):
    return render(request, 'company.html')
