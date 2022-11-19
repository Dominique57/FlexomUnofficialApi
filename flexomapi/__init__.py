from .models import SignInRes, BuildingsInfoRes, BuildingAuthorizationsRes, BuildingAuthRes, \
    ZonesRes, IotsRes
from .requests.auth import post_auth, get_building_auths, post_building_auth
from .requests.building import get_buildings_info, get_zones, get_iots
from .requests.request_handler import RequestHandler
from .settings import USER_EMAIL, USER_PASS
from .clients import UserClient, BuildingClient


def run_client():
    user_client = UserClient.build_client(USER_EMAIL, USER_PASS)
    if not user_client:
        raise Exception("Failed to create client")
    binfos = user_client.get_buildings_info()
    binfo = binfos.__root__[0]
    building_client = BuildingClient.build_client(user_client, binfo)
    zones = building_client.get_zones()
    print(zones.json())
    iots = building_client.get_iots()
    print(iots.json())


def run_legacy():
    # Login to account
    res_auth: SignInRes = RequestHandler(
        lambda: post_auth(USER_EMAIL, USER_PASS),
        lambda: None,
        SignInRes
    ).handle_or_throw()
    print(res_auth.json())
    print()

    # Get account's buildings
    res_binfos: BuildingsInfoRes = RequestHandler(
        lambda: get_buildings_info(res_auth.token),
        lambda: None,
        BuildingsInfoRes
    ).handle_or_throw()
    print(res_binfos.json())
    print()
    res_binfo = res_binfos.__root__[0]

    # Get buildings user's authorizations
    res_bauths: BuildingAuthorizationsRes = RequestHandler(
        lambda: get_building_auths(res_binfo.buildingId, res_auth.token),
        lambda: None,
        BuildingAuthorizationsRes
    ).handle_or_throw()
    print(res_bauths.json())
    print()

    # Get authorization of ourselves
    building_auth = None
    for bauth in res_bauths.__root__:
        if bauth.user.email == res_auth.email:
            building_auth = bauth
            break
    else:
        raise Exception("Failed to found bauth of given user")
    print(building_auth.json())
    print()

    # Login to the building with given authorizations
    res_bauth: BuildingAuthRes = RequestHandler(
        lambda: post_building_auth(res_binfo.hemis_base_url, res_binfo.kernel_slot, res_auth.email,
                                   building_auth.token),
        lambda: None,
        BuildingAuthRes
    ).handle_or_throw()
    print(res_bauths.json())
    print()

    # Get building's zones
    res_zones: ZonesRes = RequestHandler(
        lambda: get_zones(res_binfo.hemis_base_url, res_bauth.token),
        lambda: None,
        ZonesRes
    ).handle_or_throw()
    print(res_zones.json())
    print()

    # Get building's iot's
    res_iots: IotsRes = RequestHandler(
        lambda: get_iots(res_binfo.hemis_base_url, res_bauth.token),
        lambda: None,
        IotsRes
    ).handle_or_throw()
    print(res_iots.json())
    print()


def run():
    # run_legacy()
    run_client()
