from django.shortcuts import render
from . import search
from django.http import HttpResponse
# Create your views here.
def search_blog(request):

    if(request.method == "POST"):
        author_name = request.POST.get('name')
        res = search.search(author_name)
        return HttpResponse(res)
    else:
        return render(request, 'elasticsearchapp/search_page.html', {})