from noah.constants import KEY_ERR_CODE, KEY_MESSAGE, KEY_SUCCESS_CODE

# projects
PROJECTS_LIST_SENT = {
    KEY_SUCCESS_CODE: 1101,
    KEY_MESSAGE: "Sent list of all projects"
}

PROJECT_CREATED_SUCCESSFULLY = {
    KEY_SUCCESS_CODE: 1102,
    KEY_MESSAGE: "Project created successfully."
}

PROJECT_UPDATED_SUCCESSFULLY = {
    KEY_SUCCESS_CODE: 1103,
    KEY_MESSAGE: "Project updated successfully."
}

PROJECT_PART_BLOCK_CREATED = {
    KEY_SUCCESS_CODE: 1104,
    KEY_MESSAGE: "Project part's block created successfully."
}

PROJECT_PART_BLOCK_UPDATED = {
    KEY_SUCCESS_CODE: 1105,
    KEY_MESSAGE: "Project part's block updated successfully."
}


TEMPLATE_ID_NOT_PROVIDED = {
    KEY_ERR_CODE: 1201,
    KEY_MESSAGE: "Template id isn't provided"
}

TEMPLATE_DOES_NOT_HAVE_PARTS = {
    KEY_ERR_CODE: 1202,
    KEY_MESSAGE: "Selected template doesn't have any parts."
}

PROJECT_DOES_NOT_EXISTS = {
    KEY_ERR_CODE: 1203,
    KEY_MESSAGE: "Specified project doesn't exists."
}

INVALID_PROJECT_DETAIL = {
    KEY_ERR_CODE: 1204,
    KEY_MESSAGE: "Provided invalid data to update project details."
}

PROJECT_PART_DOES_NOT_EXISTS = {
    KEY_ERR_CODE: 1205,
    KEY_MESSAGE: "Specified project part doesn't exists."
}

EMPTY_BLOCK_ERROR = {
    KEY_ERR_CODE: 1206,
    KEY_MESSAGE: "You have left a block empty. Use the empty block first and then add another one."
}

INVALID_PROJECT_PART_BLOCK_DETAIL = {
    KEY_ERR_CODE: 1207,
    KEY_MESSAGE: "Provided invalid data to update project part block details"
}

PROJECT_PART_BLOCK_DOES_NOT_EXISTS = {
    KEY_ERR_CODE: 1208,
    KEY_MESSAGE: "Specified project part block doesn't exists."
}

ONE_PROJECT_PART_BLOCK_NEED = {
    KEY_ERR_CODE: 1209,
    KEY_MESSAGE: "You need to have at least one block per script"
}

# tutorials
TUTORIALS_LIST_SENT = {
    KEY_SUCCESS_CODE: 1301,
    KEY_MESSAGE: "Sent list of all tutorials"
}

TUTORIAL_WITH_SPECIFY_ID_NOT_FOUND = {
    KEY_ERR_CODE: 1401,
    KEY_MESSAGE: "Specified tutorial not found"
}

# templates
TEMPLATES_LIST_SENT = {
    KEY_SUCCESS_CODE: 1503,
    KEY_MESSAGE: "Sent list of all templates."
}

TEMPLATE_WITH_SPECIFY_ID_SENT = {
    KEY_SUCCESS_CODE: 1502,
    KEY_MESSAGE: "Specified template sent."
}

TEMPLATE_WITH_SPECIFY_ID_NOT_FOUND = {
    KEY_ERR_CODE: 1601,
    KEY_MESSAGE: "Specified template not found."
}

# users
USERS_NEW_PASSWORD_SET = {
    KEY_SUCCESS_CODE: 1701,
    KEY_MESSAGE: "You will recieve an email with instructions to reset your password.",
}

USERS_NEW_PASSWORD_ERR = {
    KEY_ERR_CODE: 1801,
    KEY_MESSAGE: "Email-id not registered.",
}

USERS_SIGN_UP_SUCCESS = {
    KEY_SUCCESS_CODE: 1702,
    KEY_MESSAGE: "You have been registered successfully."
}

USERS_SIGN_UP_FAILURE = {
    KEY_ERR_CODE: 1802,
    KEY_MESSAGE: "Sign-up error.Please check all the fields."
}

USER_ACCOUNT_ALREADY_EXISTS = {
    KEY_ERR_CODE: 1803,
    KEY_MESSAGE: "User already exists with specified email-id."
}

USERS_SIGN_IN_SUCCESS = {
    KEY_SUCCESS_CODE: 1703,
    KEY_MESSAGE: "You have been logged in successfully."
}

USERS_SIGN_IN_FAILURE = {
    KEY_ERR_CODE: 1804,
    KEY_MESSAGE: "Invalid email-id/password."
}

USER_DOES_NOT_EXISTS = {
    KEY_ERR_CODE: 1805,
    KEY_MESSAGE: "The email-id doesn't exists.Please check again."
}

USERS_SIGN_OUT_SUCCESS = {
    KEY_SUCCESS_CODE: 1704,
    KEY_MESSAGE: "Logout successful."
}

USERS_SIGN_OUT_FAIL = {
    KEY_ERR_CODE: 1806,
    KEY_MESSAGE: "There was a problem while Logging you out."
}

USER_DELETED_SUCCESS = {
    KEY_SUCCESS_CODE: 1705,
    KEY_MESSAGE: "Your account was deleted successfully."
}

USER_DETAIL_GET_UPDATED = {
    KEY_SUCCESS_CODE: 1706,
    KEY_MESSAGE: "Your profile is updated."
}

USER_UPDATE_INVALID_DETAIL = {
    KEY_ERR_CODE: 1807,
    KEY_MESSAGE: "Failed to update the information."
}

EMAIL_IS_REQUIRED_FOR_PASSWORD_RESET_REQUEST = {
    KEY_ERR_CODE: 1808,
    KEY_MESSAGE: 'Please enter your email-id.'
}

USERS_INVALID_OLD_PASSWORD_ERR = {
    KEY_ERR_CODE: 1809,
    KEY_MESSAGE: "Invalid current password"
}

USERS_MISSING_OLD_PASSWORD_ERR = {
    KEY_ERR_CODE: 1810,
    KEY_MESSAGE: "Please enter current password."
}

# miscellaneous
MISCELLANEOUS_SUCCESS = {
    KEY_SUCCESS_CODE: 1901,
    KEY_MESSAGE: "Sent miscellaneous page."
}

SENT_ALL_MISCELLANEOUS_PAGE = {
    KEY_SUCCESS_CODE: 1902,
    KEY_MESSAGE: "Sent all miscellaneous pages."
}

MISCELLANEOUS_ERR_SLUG = {
    KEY_ERR_CODE: 2001,
    KEY_MESSAGE: "Provided slug isn't available."
}

MISCELLANEOUS_ERR_DATA = {
    KEY_ERR_CODE: 2002,
    KEY_MESSAGE: "Invalid data"
}
