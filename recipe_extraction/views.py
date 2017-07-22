from ingredient_pull import init
from django.shortcuts import render
from .forms import get
# Create your views here.
def get_ingredients(request):
    i = init()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = get(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ret_var = i.get_ingredients_string(form.cleaned_data['recipe'])
            return render(request, 'recipe_extraction/index.html', {'ingredients': ret_var})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = get()

    return render(request, 'recipe_extraction/index.html', {'ingredients': ''})