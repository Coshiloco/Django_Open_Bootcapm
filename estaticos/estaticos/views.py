from django.shortcuts import render


def estaticos(request):
    return render(request=request, template_name="estaticos.html", context={})
