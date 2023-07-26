from django.shortcuts import render

def show_index(request):
    if not request.user.is_authenticated:
        return render(request, "templates/index.html")
    context = {"role": request.user.role, "home_active":"active"}
    return render(request, "book/templates/base.html", context=context)