from .settings import USER_EMAIL, USER_PASS
from .auth import send_auth, send_buildings_info, send_building_auths,      \
    send_building_auth

def run():
    res_auth = send_auth(USER_EMAIL, USER_PASS)
    print(res_auth.json())
    print()

    res_binfos = send_buildings_info(
        res_auth.token
    )
    print(res_binfos.json())
    print()

    res_bauths = send_building_auths(
        res_binfos.__root__[0].buildingId,
        res_auth.token
    )
    print(res_bauths.json())
    print()

    building_auth = None
    for bauth in res_bauths.__root__:
        if bauth.user.email == res_auth.email:
            building_auth = bauth
            break
    else:
        raise Exception("Failed to found bauth of given user")
    print(building_auth.json())
    print()

    res_bauth = send_building_auth(res_auth.email, building_auth.token)
    print(res_bauths.json())
    print()
