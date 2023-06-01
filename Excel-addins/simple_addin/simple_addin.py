import sys
import time
import datetime
import dt.user
import dt.excel

addin = dt.excel.Addin('SimpleAddin', 'This is a simple example which can be used to test the Excel addin functionality')

@addin.expose(description='Adds 2 numbers', help='To add 2 numbers give them to the function')
def add(a: int, b: int) -> float:
    return a + b

@addin.expose(description='Subtracts 2 numbers', help='To subtract 2 numbers give them to the function')
def sub(a: int, b: int) -> float:
    return a - b

@addin.expose(description='Adds argument a to an array', help='Give a number to add to an array')
def add_array(a: int) -> list:
    return [[11 + a, 34 + a]]

@addin.expose(description='Adds 2 arrays', help='Give 2 arrays for component wise add')
def add_two_arrays(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError('Not equal length')
    
    result = []
    for count in range(len(a)):
        result.append([])
        for count2 in range(len(a[count])):
            result[count].append(a[count][count2] + b[count][count2])

    return result

@addin.expose(description='Ticks a new value every 500ms', help='Give a seed value to the function', streaming=True)
def tick(queue: dt.excel.Queue, a: int) -> float:
    while True:
        a += 1
        queue.result(a)
        time.sleep(0.5)

@addin.expose(description='Ticks a new value every 1s', help='Give a seed value to the function', streaming=True)
def tick_minus(queue: dt.excel.Queue, a: int) -> float:
    while True:
        a -= 1
        queue.result(a)
        time.sleep(1)

@addin.expose(description='Splits the string by comma and returns the nth element', help='Splits the string by comma and returns the nth element')
def split_string(string: str, n: int) -> str:
    return string.replace(' ', '').split(',')[n]

def __excel_main__(port, debug=False):
     addin.run(port=port)

if __name__ == '__main__':
    __excel_main__(int(sys.argv[1]))
