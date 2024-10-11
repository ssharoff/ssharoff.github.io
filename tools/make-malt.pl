#!/usr/bin/perl
#Serge Sharoff, April 2011
#The script converts the output of Treetagger to the CoNLL format expected by Malt
#STDERR collects the offsets for 

$i=0;
while (<>) {
    $i++;
    if (/^</) {
	if (/<text id="(.+?)"(.*)>/) {
	    print STDERR "$i\t$1\t$2\n";
	    print "\n";
	    $i++;
	}
    } else {
	chomp; 
	($w,$p,$l)=split /\t/,$_;
	if (defined $l) {
	    $t=substr($p,0,1); 
	    $out="1\t$w\t$l\t$t\t$t\t$p\n";
	    print $out;
	    if ($p eq 'SENT') {
		print "\n";
		$i++;
	    };
	}
    }
}
