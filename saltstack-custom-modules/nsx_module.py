import logging
try:
    import json
    import requests
    import urllib3
    HAS_DEPENDENCIES = True
except ImportError:
    HAS_DEPENDENCIES = False

log = logging.getLogger(__name__)

__virtual_name__ = 'nsx'

def __virtual__():
    if HAS_DEPENDENCIES:
        return __virtual_name__
    else:
        return False, 'The hello module cannot be loaded: dependency packages unavailable.'

urllib3.disable_warnings()

def firewall_section():
    url = "https://10.182.3.46/policy/api/v1/infra/domains/default/security-policies"

    headers = {
      'authorization': 'Basic YWRtaW46QWRtaW4hMjNBZG1pbg=='
    }

    response = requests.request("GET", url, headers=headers, verify=False)


    id = response.json()['results'][0]


    return id

def get_segments_full():
    url = "https://10.182.3.46/policy/api/v1/infra/segments"

    headers = {
      'authorization': 'Basic YWRtaW46QWRtaW4hMjNBZG1pbg=='
    }

    response = requests.request("GET", url, headers=headers, verify=False)

    id = response.json()['results']

    return id

def get_segments_names():
    url = "https://10.182.3.46/policy/api/v1/infra/segments"

    headers = {
      'authorization': 'Basic YWRtaW46QWRtaW4hMjNBZG1pbg=='
    }


    response = requests.get(url, headers=headers, verify=False)

    names = [ i["display_name"] for i in response.json()["results"] ]

    return names


def get_segment_id_by_name(name):
    url = "https://10.182.3.46/policy/api/v1/infra/segments"

    headers = {
      'authorization': 'Basic YWRtaW46QWRtaW4hMjNBZG1pbg=='
    }


    response = requests.get(url, headers=headers, verify=False)

    id = [ i["id"] for i in response.json()["results"] if i["display_name"] == name ]

    return id
