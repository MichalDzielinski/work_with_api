from django.shortcuts import render
import requests

API_KEY = '4fd30a3f63bc4cf1b625796ae4787af1'

# def home(request):
#     country = request.GET.get('country')
#     category = request.GET.get('category')

#     if country:
#         url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
#         response = requests.get(url)
#         data = response.json()
#         articles = data['articles']
#     else:
#         url = f'https://newsapi.org/v2/top-headlines?category=in&apiKey={API_KEY}'
#         response = requests.get(url)
#         data = response.json()
#         articles = data['articles']



#     context = {
#         'articles' : articles
#     }

#     return render(request, 'newsapi/home.html', context)

def home(request):

    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

    articles = data['articles']
    

    context= {'articles':articles}

    return render(request, 'newsapi/home.html', context)
