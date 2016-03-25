<?php


function raindrops($num) {
    $string = '';
    $flag = false;

    if ($num % 3 == 0) {
        $flag = true;
        $string .= 'Pling';
    }
    if ($num % 5 == 0) {
        $flag = true;
        $string .= 'Plang';
    }
    if ($num % 7 == 0) {
        $flag = true;
        $string .= 'Plong';
    }

    return $flag ? $string : (string) $num;
}
