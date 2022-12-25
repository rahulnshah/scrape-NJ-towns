from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrapedColleges
from django.db.models import Count
# Create your views here.
def index(request):
    # use GROUP BY clause on the scraped colleges table
    town_to_num_of_colleges =  ScrapedColleges.objects.values("town").annotate(num_of_colleges=Count("college"))
    # use inner join to display town and college details based on the common town field 
    list_of_colleges_and_towns_they_are_in = ScrapedColleges.objects.select_related("town")
    context = {"town_to_num_of_colleges" : town_to_num_of_colleges, "list_of_colleges_and_towns_they_are_in" : list_of_colleges_and_towns_they_are_in}
    return render(request, 'njtowns/index.html', context)
