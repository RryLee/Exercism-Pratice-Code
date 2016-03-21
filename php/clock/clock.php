<?php

class Clock
{
    private $minutes;

    public function __construct($hours, $minutes = null)
    {
        $this->minutes = $minutes == null ?
            60 * $hours :
            60 * $hours + $minutes;
    }

    public function __toString()
    {
        return $this->formatTime();
    }

    public function add($minutes)
    {
        $this->minutes += $minutes;

        return $this;
    }

    public function sub($minutes)
    {
        $this->minutes -= $minutes;

        return $this;
    }

    private function formatTime()
    {
        $this->minutes %= 1440;
        if ($this->minutes < 0) {
            $this->minutes += 1440;
        }
        $hours = $this->minutes / 60;
        $minutes = $this->minutes % 60;

        return sprintf("%02d:%02d", $hours, $minutes);
    }
}
