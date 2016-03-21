<?php

const DNATORNA = [
    'C' => 'G',
    'G' => 'C',
    'T' => 'A',
    'A' => 'U'
];

function toRNA($dna) {
    $rna = '';

    foreach (str_split($dna) as $letter) {
        if (array_key_exists($letter, DNATORNA)) {
            $rna .= DNATORNA[$letter];
        }
    }

    return $rna;
}

echo toRNA('AAAABB');
