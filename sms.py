import requests

import keys
from master.models import MasterKeyValueData


def send_sms(mobile, msg, sender="mFeelB"):
    try:
        authkey = MasterKeyValueData.objects.get(key=keys.MSG91_AUTH_KEY).value

        url = 'http://api.msg91.com/api/sendhttp.php?authkey=' + authkey + '&mobiles='
        url += str(mobile)
        url += '&message=' + str(msg)
        url += '&sender=' + sender + '&route=4'

        # log
        print(url)
        print(requests.request('GET', url))
    except Exception as e:
        print(str(e))
