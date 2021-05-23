# Initialise
from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter, EUDataCenter
from zcrmsdk.src.com.zoho.api.authenticator.store import FileStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken, TokenType
from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig
from django.conf import Settings, settings

class SDKInitializer(object):

    @staticmethod
    def initialize():

        user = UserSignature(email=settings.ZOHO_USER)
        # environment = EUDataCenter.PRODUCTION()
        if settings.ZOHO_DATACENTER == "EU":
            environment = EUDataCenter.PRODUCTION()
        else:
            environment = USDataCenter.PRODUCTION()
        
        token = OAuthToken(
            client_id=settings.ZOHO_CLIENT_ID,
            client_secret=settings.ZOHO_CLIENT_SECRET,
            token=settings.ZOHO_REFRESH_TOKEN,
            token_type=TokenType.REFRESH,
            redirect_url=settings.ZOHO_REDIRECT_URL,
        )

        logger = Logger.get_instance(
            level=Logger.Levels.INFO,
            file_path="zcrmsdk_error.log",
        )

        store = FileStore(
            file_path='zcrmsdk_oauthtokens.txt'
        )

        config = SDKConfig(
            auto_refresh_fields=True,
            pick_list_validation=False
        )

        resource_path = "."

        # request_proxy = RequestProxy(host='proxyHost', port=80)
        # request_proxy = RequestProxy(host='proxyHost', port=80, user='userName', password='password')

        Initializer.initialize(
            user=user,
            environment=environment,
            token=token,
            store=store,
            sdk_config=config,
            resource_path=resource_path,
            logger=logger
        )
