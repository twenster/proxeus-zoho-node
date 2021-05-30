from django.apps import AppConfig
from django.conf import Settings, settings
import requests
import time

class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'

    def ready(self):
        #pass
        # Register the service against Proxeus
        defaultServiceName = "Zoho CRM"
        defaultJWTSecret = "my secret"
        defaultServicePort = "8011"
        defaultAuthkey = "auth"
        defaultProxeusUrl = "http://127.0.0.1:1323"
        defaultRegisterRetryInterval = 5

        payload = {
            "ID": settings.PROXEUS_SERVICENAME or defaultServiceName,
            "Name": settings.PROXEUS_SERVICENAME or defaultServiceName,
            "Details": settings.PROXEUS_SERVICENAME or defaultServiceName,
            "Url": settings.PROXEUS_URL or defaultProxeusUrl,
            "Secret": settings.PROXEUS_JWTSECRET or defaultJWTSecret
        }
        while True:
            try:
                response = requests.post(defaultProxeusUrl+"/api/admin/external/register", payload)
                response.raise_for_status()
                if (response.status_code == 200):
                    print("Node registered!")
                    break
            except requests.exceptions.HTTPError as errh:
                print(errh)
            except requests.exceptions.ConnectionError as errc:
                print(errc)
            except requests.exceptions.Timeout as errt:
                print(errt)
            except requests.exceptions.RequestException as err:
                print(err)
            #wait defaultRegisterRetryInterval seconds before next attempt
            timesleep(defaultRegisterRetryInterval)

