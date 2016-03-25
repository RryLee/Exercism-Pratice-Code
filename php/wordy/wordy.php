<?php

const OPERATOR_REGEX = '/(plus|minus|multiplied|divided)/';
const NUM_REGEX      = '/(-?\d)+/';

function calculate($string) {
    preg_match_all(OPERATOR_REGEX, $string, $operators);

    if (! $operators[0]) {
        throw new InvalidArgumentException;
    }

    preg_match_all(NUM_REGEX, $string, $nums);

    if (count($nums[0]) != count($operators[0]) + 1) {
        throw new InvalidArgumentException;
    }

    for ($i = 1, $j = 0; $i < count($nums[0]); ++ $i, ++ $j) {
        $nums[0][$i] = $operators[0][$j]($nums[0][$i - 1], $nums[0][$i]);
    }

    return $nums[0][count($nums[0]) - 1];
}

function plus($a, $b) {
    return $a + $b;
}

function minus($a, $b) {
    return $a - $b;
}

function multiplied($a, $b) {
    return $a * $b;
}

function divided($a, $b) {
    return $a / $b;
}
