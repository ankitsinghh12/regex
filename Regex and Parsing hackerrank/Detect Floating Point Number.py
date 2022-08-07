# Enter your code here. Read input from STDIN. Print output to STDOUTimport re

from re import match, compile

pattern = compile('^[-+]?\d*\.\d+$')
for _ in range(int(input())):
    print(bool(pattern.match(input())))