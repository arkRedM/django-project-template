import requests

import keys
from master.models import MasterKeyValueData


# modify this notification send function to your need
def send_notification(fcm, title, message):
    try:
        fcm_auth_key = MasterKeyValueData.objects.get(key=keys.FCM_AUTH_KEY).value
        if fcm is not None:
            json = {
                keys.TO: str(fcm),
                keys.DATA: {
                    keys.TITLE: str(title),
                    keys.MESSAGE: str(message),
                }
            }

            url = keys.FCM_API_BASE_URL

            headers = {
                keys.CONTENT_TYPE: keys.APPLICATION_JSON,
                keys.AUTHORIZATION: 'key=' + fcm_auth_key
            }

            r = requests.post(url, headers=headers, json=json)

            for o in r:
                print(o)
        else:
            print("No Fcm")
    except (MasterKeyValueData.DoesNotExist, TypeError, ValueError) as e:
        print(e)

