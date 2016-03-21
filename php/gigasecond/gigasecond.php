<?php

function from(DateTime $date) {
    $interval = new DateInterval("PT1000000000S");

    return $date->add($interval);
}
