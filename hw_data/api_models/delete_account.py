from hw_data.utils.helpers import send_request


def delete_account(base_url, email, password):
    endpoint = 'api/deleteAccount'
    method = 'DELETE'
    form_data = {
        'email': email,
        'password': password,
    }

    result = send_request(base_url, endpoint, method, data=form_data)
    return result
