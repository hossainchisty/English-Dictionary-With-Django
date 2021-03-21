from django.shortcuts import render
from PyDictionary import PyDictionary
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def word(request):
    try:
        search = request.GET.get('search')
        dictionary = PyDictionary()
        meaning = dictionary.meaning(search)
        synonyms = dictionary.synonym(search)
        antonyms = dictionary.antonym(search)
    except (RuntimeError, TypeError, NameError,KeyError):
            messages.error(request, "No search results found. Please refine your word.")

    finally:
        context = {
                'meaning': meaning['Noun'][0],
                'synonyms': synonyms,
                'antonyms': antonyms,
                'search':search }
    return render(request, 'word.html', context)




   
