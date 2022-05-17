from keycloak import keycloak_account


def get_userinfo_for_create(access_token: str):
    user = keycloak_account.get_user(token=access_token)
    if user:
        extra_fields = dict()
        extra_fields["created_by"] = user["username"]
        extra_fields["modified_by"] = user["username"]
        return extra_fields
    else:
        return None


def get_userinfo_for_update(access_token: str):
    user = keycloak_account.get_user(token=access_token)
    if user:
        extra_fields = dict()
        extra_fields["modified_by"] = user["username"]
        return extra_fields
    else:
        return None
