from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request):
    servings = request.GET.get('servings', None)
    recipe = DATA['omlet']

    context = {
        'recipe': recipe,
        'servings': servings if servings is None else int(servings),
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = request.GET.get('servings', None)
    recipe = DATA['pasta']

    context = {
        'recipe': recipe,
        'servings': servings if servings is None else int(servings),
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = request.GET.get('servings', None)
    recipe = DATA['buter']

    context = {
        'recipe': recipe,
        'servings': servings if servings is None else int(servings),
    }
    return render(request, 'calculator/index.html', context)
