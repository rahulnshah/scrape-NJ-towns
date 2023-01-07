from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrapedColleges, ScrapedTowns
from django.db.models import Count, Q
# Create your views here.
def index(request):
    # use GROUP BY clause on the scraped colleges table
    town_to_num_of_colleges =  ScrapedColleges.objects.values("town").annotate(num_of_colleges=Count("college"))
    # Get the querysets for the two models
    colleges = ScrapedColleges.objects.all()
    towns = ScrapedTowns.objects.all()
    # use inner join to display town and college details based on the common town field 
    # TODO: Figure out how display other fileds from the towns table along side the fields from the scraped_colleges table
    list_of_colleges_and_towns_they_are_in = colleges.filter(Q(town__in=towns))  
    context = {"towns" : towns, "town_to_num_of_colleges" : town_to_num_of_colleges, "list_of_colleges_and_towns_they_are_in" : list_of_colleges_and_towns_they_are_in}
    return render(request, 'njtowns/index.html', context)
