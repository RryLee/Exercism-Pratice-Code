<?php

class Game
{
    private $rolls = [];

    public function roll($pins)
    {
        $this->rolls[] = $pins;
    }

    public function score()
    {
        $this->fillRolls();

        $score = 0;
        $roll = 0;

        for ($frame = 1; $frame <= 10; ++ $frame) {
            if ($this->isStrike($roll)) {
                $score += 10 + $this->getStrikeScore($roll);
                $roll ++;
                continue;
            }

            $score += $this->isSquare($roll) ? $this->getSquareScore($roll) : $this->getDefaultScore($roll);
            $roll += 2;
        }

        return $score;
    }

    private function fillRolls()
    {
        for ($roll = 0; $roll < 20; ++ $roll) {
            if (! isset($this->rolls[$roll])) {
                $this->rolls[$roll] = 0;
            }
        }
    }

    private function isStrike($roll)
    {
        return $this->rolls[$roll] == 10;
    }

    private function isSquare($roll)
    {
        return $this->rolls[$roll] + $this->rolls[$roll + 1] == 10;
    }

    private function getDefaultScore($roll)
    {
        return $this->rolls[$roll] + $this->rolls[$roll + 1];
    }

    public function getSquareScore($roll)
    {
        return 10 + $this->rolls[$roll + 2];
    }

    private function getStrikeScore($roll)
    {
        return $this->rolls[$roll + 1] + $this->rolls[$roll + 2];
    }
}
