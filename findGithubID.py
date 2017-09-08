import csv, requests, time

with open('SOIntersectionGithub.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    for row in readCSV:
        githubEmailID = row[1]
        idResponse = requests.get('https://api.github.com/search/users?q=' + githubEmailID + '%20in:email')
        
        try:
            # Print github id from github email
        	print str(githubEmailID) + "->" + str(idResponse.json()['items'][0]['id'])
        except Exception as e:
        	if str(e) == "list index out of range":
        	 	print str(githubEmailID) + " -> User Not Found"
        	else:
        	 	time.sleep(60 * 61)
        	continue