from django.http import JsonResponse


def api_response(data, success=True, status_code=200, message=None, error=None):
    response = {
        'data': data,
        'message': message,
        'success': success
    }
    if error:
        response['error'] = error
    return JsonResponse(response, status=status_code)