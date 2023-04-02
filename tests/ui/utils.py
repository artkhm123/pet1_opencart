import random

NON_EXISTING_USERNAME = "NON_EXISTING_USERNAME" + str(random.randint(0, 10))
WRONG_PASSWORD = "WRONG_PASSWORD"
OPENCART_USERNAME = "user"
OPENCART_PASSWORD = "bitnami"

MIN_WAIT = 1
H1_FONT_SIZE = 33
H1_FONT_COLOR = "rgba(68, 68, 68, 1)"

# в дальнейшем можно прикрутить, что бы цена бралась откуда то из базы например, а не была захардкодана
MAC_PRICE = {
    "USD": "$602.00",
    "GBP": "£368.73",
    "EUR": "472.33€"
}
IPHONE_PRICE = {
    "USD": "$123.20",
    "GBP": "£75.46",
    "EUR": "96.66€"
}

LOGIN_PAGE_PATH = "/admin"
CATALOG_PATH = "/component"
REG_PAGE_PATH = "/index.php?route=account/register"
iPHONE_PAGE = "/iphone"
MAC_PAGE = "/macbook"
