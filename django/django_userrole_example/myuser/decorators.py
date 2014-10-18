from functools import wraps

from django.http import HttpResponse

from myuser.models import MyUser

_default_unauthorized_html = """
    <h1>Unauthorized</h1>
    <p>The server could not verify that you are authorized to access the URL
    requested. You either supplied the secured url ,
    or your browser doesn't understand how to supply the credentials required.
    <em>Contact Administrator</em></p>
    """
    
def _get_unauthorized_response(text=None, headers=None):
    response = HttpResponse()
    response.status_code = 401
    response.content = text or _default_unauthorized_html
    response.headers = headers or {}
    return response


def roles_required(*roles):
    '''
    roles_required decorator
    '''

    def wrapper(function):

        @wraps(function)
        def check_roles(request, *args, **kwargs):       
            if request.user.is_authenticated():
                return function(request, *args, **kwargs)
            else:
                myuser = MyUser.objects.get(user=request.user)
                if any([myuser.has_role(role) for role in roles]):
                     return function(request, *args, **kwargs)
            
            return _get_unauthorized_response()
        return check_roles
    return wrapper
