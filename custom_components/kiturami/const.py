from homeassistant.const import Platform

DOMAIN = "kiturami"
TITLE = "귀뚜라미"
MODEL = "NCTR"

PLATFORMS: list[Platform] = [Platform.CLIMATE]

KITURAMI_API_URL = 'https://igis.krb.co.kr/api'

MAX_TEMP = 45
MIN_TEMP = 10

MAX_BATH_TEMP=80
MIN_BATH_TEMP=50
