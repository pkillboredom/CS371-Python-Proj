#########################################################################################
# Python Project                                                                        #
# Use Python 3                                                                          #
# Authors :                                                                             #
#   Luke Tomkus                                                                         #
#   Tom Reilley                                                                         #
#########################################################################################

from subprocess import Popen, PIPE, STDOUT

import re
import sys
import os
import bs4
import requests


args = sys.argv
term = ""
subject = ""

#parse for terms and subjects
url = requests.get("http://www2.monmouth.edu/muwebadv/wa3/search/SearchClassesV2.aspx")
content = url.text
search_page_soup = bs4.BeautifulSoup(content, "lxml")
terms = search_page_soup.find('select', {'id': '_ctl0_MainContent_ddlTerm'}).select('option')
subjects = search_page_soup.find('select', {'id': '_ctl0_MainContent_ddlSubj_1'}).select('option')

for eacharg in args:
	if (re.search('-.*$', eacharg)):
		if (eacharg == "-help"):
			print ("  * Term          : which Term (semester) the class is in, e.g. \"17/SP\"")
			print ("  * Subject       : which Subject the class is in (2 letter abbreviation), e.g. \"EN\" (English)")
			print ("  * -help         : display a help screen and sample usage")
			print ("  * -terms        : list currently available Terms")
			print ("  * -subjects     : list currently available Subjects")
		elif (eacharg == "-terms"):
			print ("!!! The term to be used is before the dash !!!")
			for eachterm in terms:
				print(eachterm.getText())
			print ("!!! The term to be used is before the dash !!!")
		elif (eacharg == "-subjects"):
			print ("!!! The code to be used is in parenthesis !!!")
			for eachsubject in subjects:
				print (eachsubject.getText())
			print ("!!! The code to be used is in parenthesis !!!")
		else:
			sys.exit("Invalid option")
	elif not (os.path.basename(__file__)) in eacharg: #The first param will be the script name
												      #and we dont want that.
		if (term == ""):
			term = eacharg
		elif (subject == ""):
			subject = eacharg
		else:
			sys.exit ("Too many parameters")

if "" in [term, subject]:
	sys.exit ("Not enough parameters")

#print ("##DEBUG## term: " + term + ". sub: " + subject)

pipe = Popen(["perl", "class_search.pl", term, subject], stdout=PIPE, stderr = STDOUT)
[class_search_results, errors] = pipe.communicate()

class_search_soup = bs4.BeautifulSoup(class_search_results, "lxml")

class_table = class_search_soup.find ('table', {'id': '_ctl0_MainContent_dgdSearchResult'})

print(class_table)