# https://pl.spoj.com/problems/ROWNANIE/
import sys

#INPUT
# def data_reader_test_input():
#     data = list(map(float, input().split()))
#     return data
def data_reader(text):
    data = list(map(float, text.split()))
    return data
#LOGIC
def calculate_delta(a_coeff,b_coeff,c_coeff):
    return b_coeff**2 - 4*a_coeff*c_coeff

def calculate_number_of_roots(coeff):
    delta = calculate_delta(coeff[0],coeff[1],coeff[2])
    if delta>0:
        return 2
    elif delta<0:
        return 0
    else:
        return 1

#OUTPUT
def result_writer(result):
    print(result)

#Main
# def run():
def run(text):
    # data = data_reader_test_input()
    for t in text.strip().split('\n'):
        data = data_reader(t)
        result = calculate_number_of_roots(data)
        result_writer(result)
text = sys.stdin.read()
run(text)