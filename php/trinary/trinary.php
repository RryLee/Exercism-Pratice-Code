<?php

const VALIDNUMS = ['0', '1', '2'];

function toDecimal($s) {
    $result = 0;
    $length = strlen($s);

    foreach (str_split($s) as $i => $digit) {
        if (! in_array($digit, VALIDNUMS)) {
                return 0;
        }

        $result += $digit * pow(3, $length - 1 - $i);
    }

    return $result;
}
