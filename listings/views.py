from django.shortcuts import render

def index(request):
    render(request, 'listings/listings.html')

def listings(request):
    render(request, 'listings/listing.html')
    
def search(request):
    render(request, 'listings/search.html')
    
