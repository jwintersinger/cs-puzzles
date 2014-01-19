#!/bin/sh
# Usage: python create_problem.py <n> <|R|> | python soln2.py [-d]
python3 create_problem.py 62 1000 | python3 soln2.py $1
