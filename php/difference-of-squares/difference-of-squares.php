<?php

function square($n) {
    return $n * $n;
}

function sumOfSquares($n) {
    return array_sum(array_map('square', range(1, $n)));
}

function squareOfSums($n) {
    return pow(array_sum(range(1, $n)), 2);
}

function difference($n) {
    return squareOfSums($n) - sumOfSquares($n);
}
