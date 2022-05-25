from keycloak import keycloak_admin
from ..models.exceptions import UpdateSecurityException
from keycloak.exceptions import KeycloakGetError
import ast


def get_security_info(token: str) -> dict:

    try:
        realm_info = keycloak_admin.get_realm(token=token)
        password_policy_string = realm_info["passwordPolicy"]

        array_single_policy = password_policy_string.split(" and ")

        policy_dict = {}
        for single in array_single_policy:
            arr = single.split("(")
            name = arr[0]
            value = arr[1].replace(")", "")
            policy_dict[name] = value

        policy_dict_response = {}
        # min len
        if "length" in policy_dict.keys():
            policy_dict_response["length"] = int(policy_dict["length"])
        else:
            policy_dict_response["length"] = 6
        # passwordHistory
        if "passwordHistory" in policy_dict.keys():
            policy_dict_response["passwordHistory"] = int(
                policy_dict["passwordHistory"]
            )
        else:
            policy_dict_response["passwordHistory"] = 0
        # days of validity
        if "forceExpiredPasswordChange" in policy_dict.keys():
            policy_dict_response["forceExpiredPasswordChange"] = int(
                policy_dict["forceExpiredPasswordChange"]
            )
        else:
            policy_dict_response["forceExpiredPasswordChange"] = 0
        # min upper case
        if "upperCase" in policy_dict.keys() and int(policy_dict["upperCase"]) > 0:
            policy_dict_response["upperCase"] = True
        else:
            policy_dict_response["upperCase"] = False
        # min lower case
        if "lowerCase" in policy_dict.keys() and int(policy_dict["lowerCase"]) > 0:
            policy_dict_response["lowerCase"] = True
        else:
            policy_dict_response["lowerCase"] = False
        # min digits
        if "digits" in policy_dict.keys() and int(policy_dict["digits"]) > 0:
            policy_dict_response["digits"] = True
        else:
            policy_dict_response["digits"] = False
        # special character
        if (
            "specialChars" in policy_dict.keys()
            and int(policy_dict["specialChars"]) > 0
        ):
            policy_dict_response["specialChars"] = True
        else:
            policy_dict_response["specialChars"] = False

        return policy_dict_response

    except KeycloakGetError as e:
        error = ast.literal_eval(e.error_message.decode("UTF-8"))
        if "errorMessage" in error:
            raise UpdateSecurityException(
                status_code=e.response_code,
                message=error["errorMessage"],
            )
        elif "error" in error:
            raise UpdateSecurityException(
                status_code=e.response_code,
                message=error["error"],
            )

        raise UpdateSecurityException()


def update_policies(token, policies):
    policies_dict = policies
    policies_string = ""

    dict_keys = policies_dict.keys()
    for key in dict_keys:
        # min len
        if key == "length" and policies_dict["length"] > 0:
            policies_string += "length(" + str(policies_dict["length"]) + ") and "
        if key == "length" and policies_dict["length"] == 0:
            policies_string += "length(6) and "
        # passwordHistory
        if key == "passwordHistory" and policies_dict["passwordHistory"] > 0:
            policies_string += (
                "passwordHistory(" + str(policies_dict["passwordHistory"]) + ") and "
            )
        # days of validity
        if (
            key == "forceExpiredPasswordChange"
            and policies_dict["forceExpiredPasswordChange"] > 0
        ):
            policies_string += (
                "forceExpiredPasswordChange("
                + str(policies_dict["forceExpiredPasswordChange"])
                + ") and "
            )
        # min upper case
        if key == "upperCase" and policies_dict["upperCase"] is True:
            policies_string += "upperCase(1) and "
        # min lower case
        if key == "lowerCase" and policies_dict["lowerCase"] is True:
            policies_string += "lowerCase(1) and "
        # min digits
        if key == "digits" and policies_dict["digits"] is True:
            policies_string += "digits(1) and "
        # special character
        if key == "specialChars" and policies_dict["specialChars"] is True:
            policies_string += "specialChars(1) and "

    try:
        if len(policies_string) > 5:
            final_policies_string = policies_string[:-5]
        realm_info = keycloak_admin.get_realm(token=token)
        to_send = {}
        to_send["id"] = realm_info["id"]
        to_send["passwordPolicy"] = final_policies_string
        err_result = keycloak_admin.update_realm(token=token, payload=to_send)

        if len(err_result) > 0:
            raise UpdateSecurityException()

    except KeycloakGetError as e:
        error = ast.literal_eval(e.error_message.decode("UTF-8"))
        if "errorMessage" in error:
            raise UpdateSecurityException(
                status_code=e.response_code,
                message=error["errorMessage"],
            )
        elif "error" in error:
            raise UpdateSecurityException(
                status_code=e.response_code,
                message=error["error"],
            )

        raise UpdateSecurityException()
