<?php

class Robot
{
    private $name = null;

    public function getName()
    {
        if (! isset($this->name)) {
            $this->name = $this->generateName();
        }

        return $this->name;
    }

    public function reset()
    {
        $this->name = null;
    }

    private function generateName()
    {
        $letters = range('a', 'z');
        shuffle($letters);
        $digits = range(0, 9);
        shuffle($digits);

        return implode('', array_slice($letters, 0, 2))
            . implode('', array_slice($digits, 0, 3));
    }
}
