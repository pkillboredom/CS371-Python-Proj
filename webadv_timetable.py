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



args = sys.argv
term = ""
subject = ""

for eacharg in args:
	if (re.search('-.*$', eacharg)):
		if (eacharg == "-help"):
			print ("  * Term          : which Term (semester) the class is in, e.g. \"17/SP\"")
			print ("  * Subject       : which Subject the class is in (2 letter abbreviation), e.g. \"EN\" (English)")
			print ("  * -help         : display a help screen and sample usage")
			print ("  * -terms        : list currently available Terms")
			print ("  * -subjects     : list currently available Subjects")
		elif (eacharg == "-terms"):
			print ("TERMS PLACEHOLDER")
		elif (eacharg == "-subjects"):
			print ("SUBJECTS PLACEHOLDER")
		else:
			sys.exit("Invalid option")
	elif (eacharg != os.path.basename(__file__)): #The first param will be the script name
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