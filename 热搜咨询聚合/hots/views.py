from django.shortcuts import render
from hots.models import HotsModel

def count_num():
    cou_dict = {
        "zh":None,
        "wb":None,
        "bz":None,
    }
    for i,key in zip(range(1, 4),cou_dict.keys()):
        c = HotsModel.objects.filter(source=i).count()
        cou_dict[key] = c
    return cou_dict

def index(request):
    activate_list = {
        '0': 'aa',
        '2': "weibo",
        '1': "zhihu",
        '3': "bb",
    }
    query = request.GET.get('q', None)
    if query in ['1', '2', '3']:
        all_data = HotsModel.objects.filter(source=int(query))
    else:
        all_data = HotsModel.objects.all()
        query = '0'

    ac = {}
    ac[activate_list[query]] = 'active'
    ac["data"] = all_data
    ac["count_num"] = count_num()
    return render(request, 'index.html', ac)
