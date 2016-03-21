<?php

function distance($a, $b)
{
    if (strlen($a) != strlen($b)) {
        throw new InvalidArgumentException('DNA strands must be of equal length.');
    }

    $count = 0;
    for ($i=0; $i < strlen($a); ++ $i) {
        if ($a[$i] != $b[$i]) ++ $count;
    }

    return $count;
}

// function false_if_equal($a_char, $b_char) {
// 	return ($a_char != $b_char);
// }
//
// function distance($a, $b)
// {
// 	// check for equal length sequences
// 	if ( strlen((string)$a) != strlen((string)$b) )
// 		throw new InvalidArgumentException('DNA strands must be of equal length.');
//
// 	$a_array = str_split($a);
// 	$b_array = str_split($b);
// 	$bool_array = array_map('false_if_equal', $a_array, $b_array); // returns array of booleans, true on inequality
//
// 	return array_sum($bool_array);
// }
