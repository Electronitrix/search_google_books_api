"""
   Queries google-books API and outputs result to a file in an
   easy to read format.
"""
import requests
import json
import urllib

url = "https://www.googleapis.com/books/v1/volumes?q="
query = input("Please enter the name of the book you want to search for:")

url =  url + urllib.parse.quote_plus(query)
response = requests.get(url)
result = response.json()

outputFile = ""

if result['totalItems'] == 0:
	outputFile += "No Result Found!!!"
else:
	for book in result['items']:
		outputFile += book['volumeInfo']['title'].upper() + "\n"
		outputFile += book['selfLink'] + "\n"
		#import pdb;pdb.set_trace()
		outputFile += book['volumeInfo']['authors'][0] + " - " + book['volumeInfo']['publishedDate'] + " - "

		if 'categories' in book['volumeInfo']:
			outputFile += book['volumeInfo']['categories'][0] + "\n"
		else:
			"\n"

		if 'searchInfo' in book:
			outputFile += book['searchInfo']['textSnippet'] + "\n"
		else:
			"No more information\n"

		if 'averageRating' in book['volumeInfo']:
			outputFile += str(book['volumeInfo']['averageRating']) + "\n\n\n"
		else:
			outputFile += "\n\n\n"

with open("profile.txt", "w") as output:
	output.write(outputFile)

