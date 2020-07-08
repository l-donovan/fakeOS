# fakeOS

## Requirements
* `python3`
* `antlr4`

## Setup
`pip install antlr4-python3-runtime`

`antlr4 -Dlanguage=Python3 FunctionCall.g4`

## Run
`python main.py`

## Fun example
    $ set pi 3.14159265
    $ set tau (mul (get pi) 2.0)
    $ print (format "Tau is equal to {}" (get tau))
    Tau is equal to 6.2831853
