from django.shortcuts import render
from collection.models import Laptops

# Create your views here.
def index(request):
    mything = Laptops.objects.all()

    # defining the variable
    number = 6
    #mything = "My Thing A"

    # passing the variable to the view
    return render(request, 'index.html', {
        'number': number,
	'mything': mything,
    })

