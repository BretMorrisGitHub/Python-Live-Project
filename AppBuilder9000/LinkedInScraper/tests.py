import json

from django.test import TestCase


# Create your tests here.
# testing grounds for methods
# json = {"info": "", "meta":{}, "results:[]"}
# json["results"] = ["firstname"]


def jsonArray2List(jsonObj):
    first_name = {}
    profile_id = {}
    sub_title = {}
    location = {}
    industry = {}
    last_name = {}

    results = jsonObj["results"]

    for i, result in enumerate(results):
        first_name['first_name' + str(i)] = result['first_name']
        profile_id['profile_id' + str(i)] = result['profile_id']
        sub_title['sub_title' + str(i)] = result['sub_title']
        location['location' + str(i)] = result['location']['default']
        industry['industry' + str(i)] = result['industry']
        last_name['last_name' + str(i)] = result['last_name']

    result_dict = {
        'first_names': first_name,
        'profile_id': profile_id,
        'sub_title': sub_title,
        'location': location,
        'industry': industry,
        'last_name': last_name,
    }

    return result_dict






