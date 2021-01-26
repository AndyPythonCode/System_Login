from django.shortcuts import redirect

def unathenticated_user(view_func):
    def wrappers(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrappers   