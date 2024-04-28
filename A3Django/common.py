import json

from django.http import HttpResponse


def success(massage='ok'):
    result = {
        'code': 0,
        'msg': massage,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def success_data(data, massage='ok'):
    result = {
        'code': 0,
        'msg': massage,
        'data': data,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def fail(massage='fail'):
    result = {
        'code': 1,
        'msg': massage,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')
