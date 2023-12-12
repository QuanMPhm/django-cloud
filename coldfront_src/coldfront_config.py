DEBUG = True
PLUGIN_AUTH_OIDC = True


OIDC_RP_CLIENT_ID = "coldfront"
OIDC_RP_CLIENT_SECRET = 'dvbETos2JzhkHaVwX8ssjFQY2yIOYiVq'

OIDC_OP_AUTHORIZATION_ENDPOINT = "http://keycloak:8080/realms/master/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = "http://keycloak:8080/realms/master/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = "http://keycloak:8080/realms/master/protocol/openid-connect/userinfo"
OIDC_RP_SIGN_ALGO = 'RS256'    # Because HS256 didn't seem to work??? https://github.com/mozilla/mozilla-django-oidc/issues/382
OIDC_OP_JWKS_ENDPOINT = "http://keycloak:8080/realms/master/protocol/openid-connect/certs"

# LOGIN_REDIRECT_URL = "/cloud/login"
# LOGIN_REDIRECT_URL_FAILURE = "/cloud/login"