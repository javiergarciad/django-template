from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader



CONTEXT ={"title": ("Django Template")}

def home(request):
    """Return homepage"""
    template = loader.get_template("./public/home.html")
    return HttpResponse(template.render(CONTEXT, request))


# ----------------------------------------------------------------------------
# ERRORS
# -----------------------------------------------------------------------------
def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'.500.html', data)

def error_403(request, exception):
        data = {}
        return render(request,'403.html', data)

def error_400(request, exception):
        data = {}
        return render(request,'400.html', data)