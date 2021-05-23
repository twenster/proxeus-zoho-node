# Zoho Node Setup

# Zoho email address / login
ZOHO_USER='zoho@email.address'

# Datacenter the user is registered in
# American
#ZOHO_DATACENTER="US"
# European
ZOHO_DATACENTER="EU"

# Zoho API credentials
# 1. Create an API connection at https://api-console.zoho.eu/
# 2. Add a self-client application
# 3. Get the REFRESH token
# Doc: https://help.zoho.com/portal/en/community/topic/kaizen-2-oauth2-0-and-self-client-api

ZOHO_CLIENT_ID=''
ZOHO_CLIENT_SECRET=''
ZOHO_REFRESH_TOKEN=''
ZOHO_REDIRECT_URL='https://crm.zoho.eu'

# SECURITY WARNING: keep the secret key used in production secret!
DJANGO_SECRET_KEY = ''