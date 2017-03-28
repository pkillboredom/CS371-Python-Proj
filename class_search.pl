# This Perl script takes 2 command line arguments and uses
# Mechanize to query webadvisor. Make no changes to this script.
# Your Python project script must call this Perl script to
# interact with webadvisor.

use WWW::Mechanize;

my $mech = WWW::Mechanize->new();

# Specify term and subject on commandline
$term    = $ARGV[ 0 ]; # e.g. "16/SP"
$subject = $ARGV[ 1 ]; # e.g. CS

# Grabs webadvisor search page
$mech->get('http://www2.monmouth.edu/muwebadv/wa3/search/SearchClassesV2.aspx');

# Populates the term drop box
$mech->field("_ctl0:MainContent:ddlTerm", $term);

# Populates subject drop box
$mech->field("_ctl0:MainContent:ddlSubj_1", $subject);

# works: clicks the submit button
$mech->click_button(name => "_ctl0:MainContent:btnSubmit");

# Returns HTML content in $page
my $page = $mech->content;
print $page;
