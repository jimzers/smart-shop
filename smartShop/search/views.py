from django.conf import settings
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
from django.shortcuts import render

from ..product.utils import products_with_details
from ..product.utils.availability import products_with_availability
from .forms import SearchForm


def paginate_results(results, get_data, paginate_by=settings.PAGINATE_BY):
    paginator = Paginator(results, paginate_by)
    page_number = get_data.get('page', 1)
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        raise Http404('No such page!')
    return page


def evaluate_search_query(form, request):
    results = products_with_details(request.user) & form.search()
    return products_with_availability(results, discounts=request.discounts,
                                      local_currency=request.currency)

"""
def search(request):
    '''
        if not settings.ENABLE_SEARCH:
            raise Http404('No such page!')
        form = SearchForm(data=request.GET or None)
    '''
    try:
        clothing = Clothing.objects.get(pk=clothing_id)
    except Clothing.DoesNotExist:
        raise Http404('Clothing does not exist')

    if form.is_valid():
        budget = document.ClothingSearch.budget.value
        clothetype = document.ClothingSearch.type.value
        clothepreference = document.ClothingSearch.preference.value
        friendliness = document.ClothingSearch.friendly.value
        for clothe in clothing.Clothing.objects.all():
            searchlist = []
            if budget >= clothe.clothing_price and clothetype == clothe.clothing_type and clothepreference == clothe.clothing_style:
                if friendliness == clothe.friendly:
                    searchlist.append(clothe)

                    # for obj in searchlist:
                    # RETURN OBJECTIMAGE + URL IN SEARCHRESULTS HTML FILE
                else:
                    searchlist.append(clothe)
                    # for obj in searchlist:
                    # RETURN OBJECTIMAGE + URL IN SEARCHRESULTS HTML FILE
    return render(request, 'searchresults.html', {'searchlist': searchlist})



        query = form.cleaned_data.get('q', '')
        results = evaluate_search_query(form, request)

    else:
        query, results = '', []
    page = paginate_results(list(results), request.GET)
    ctx = {
        'query': query,
        'results': page,
        'query_string': '?q=%s' % query}
    return render(request, 'search/results.html', ctx)
"""