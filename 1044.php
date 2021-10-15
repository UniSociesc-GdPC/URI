<?php

$pieces = explode(" ",trim(fgets(STDIN)));
$a = $pieces[0];
$b = $pieces[1];

if ($a % $b ==0 || $b%$a==0){ print "Sao Multiplos\n";}
else{ print "Nao sao Multiplos\n";}
?>