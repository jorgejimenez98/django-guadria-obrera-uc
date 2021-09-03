from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def getPagination(request, querySet, pageSize):
    paginator = Paginator(querySet, pageSize)
    page = request.GET.get('page')
    try:
        querySet = paginator.page(page)
    except EmptyPage:
        querySet = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        querySet = paginator.page(1)
    return querySet
