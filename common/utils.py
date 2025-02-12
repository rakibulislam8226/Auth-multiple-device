from rest_framework import status, response


# Create Response for izitoast
def create_response(
    status_bool=True,
    data=None,
    message="",
    errors=None,
    meta=None,
    status_code=status.HTTP_200_OK,
):
    """
    This function is used to create a response for izitoast with the given data, message, errors, and meta.
    """
    response_data = {
        "status": status_bool,
        "message": message,
    }
    if data is not None:
        response_data["data"] = data
    if errors is not None:
        response_data["errors"] = errors
    if meta is not None:
        response_data["meta"] = meta

    return response.Response(response_data, status=status_code)
