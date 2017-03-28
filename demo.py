# Demo program: Call Perl script from Python script with 2 command line arguments,
#               store output of Perl script in string

from subprocess import Popen, PIPE, STDOUT


term = "17/SP"
subject = "DA"

# Call Perl script; store output and errors from Perl script in pipe:
pipe = Popen(["perl", "class_search.pl", term, subject], stdout=PIPE, stderr = STDOUT)

# Get output and errors from pipe:
[class_search_results, errors] = pipe.communicate()

# Print stored output from Perl script:
print (class_search_results)