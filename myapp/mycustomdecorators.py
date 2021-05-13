from django.http import HttpResponse, JsonResponse

from functools import wraps

from django.shortcuts import redirect

# this middleware is not callable(means cant use like mycustomdecorator(params))
def mycustomdecorator(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_anonymous:
            # return JsonResponse({"Your blocked from custom middleware, user name:": str(request.user)})
            return redirect('/admin/login')
        else:
            print("from my custom middleware, user name:", request.user)
            return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


# ====================================== OR ===========================
# this middleware is callable(means can use like mycustomdecorator(params))


def mycallablecustomdecorator(params=None):
    def anyname(function):
        @wraps(function)
        def anyothername(request, *args, **kwargs):
            if params == "allow":
                return function(request, *args, **kwargs)
            else:
                return HttpResponse("Not allowed")

        return anyothername
    return anyname