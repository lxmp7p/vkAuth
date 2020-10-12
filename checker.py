import vk
from decoderMD5 import decoder
from vk.exceptions import VkAuthError

adminLogin = "e3afed0047b08059d0fada10f400c1e5"
adminPassword = "e3afed0047b08059d0fada10f400c1e5"

def checkLP(login, password):
    error = False
    try:
        session = vk.AuthSession(app_id="6741789", user_login=login, user_password=password)
        vk__api = (session)
    except VkAuthError:
        error = True
    return error

def checkLPAdmin(login, password):
    login = decoder(login)
    password = decoder(password)
    if (adminLogin == login and adminPassword == password):
        return False
    else:
        return True