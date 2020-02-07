from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me...'})

def eggs(request):
    return HttpResponse('<h1>Eggs are Great!</h1>')

def food(request):
	return HttpResponse('<h1>Food is the BEST thing. but not of my mess!</h1')

def football(request):
	return HttpResponse('<h1>Christiano RONALDO!</h1>')

def about(request):
	return render(request, 'about.html')
 
def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	worddictionary = {}


	for word in wordlist:
		if word in worddictionary:
			#increase
			worddictionary[word] += 1
		else:
			#Add
			worddictionary[word] = 1

	sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)



	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})
