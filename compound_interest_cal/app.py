# compound interest calculator
# formula used A = p(1 + r/n)^nt
# where A = total amount that accumulates. P = original principal; that's the money we start with. The r = interest rate. and t = time (in years).

import math

# input information
unknown = input(
    'Select unknown \nA. A = total amount that accumulates \nB. P = original principal \nC. r = interest rate \nD. t = time (in years):\n\n')


def solve_A():
    n = input(
        'Select n \nA. Daily (360) \nB. Daily (365) \nC. Monthly \nD. Quarterly \nE. Annually:\n\n')
    p = input('Input P (original principal): ')
    r = input('Input r (interest rate): ')
    t = input('Input t (time (in years)): ')

    # n value
    n_value = 0
    if (n.upper() == 'A'):
        n_value = 360
    elif (n.upper() == 'B'):
        n_value = 365
    elif (n.upper() == 'C'):
        n_value = 12
    elif (n.upper() == 'D'):
        n_value = 4
    elif (n.upper() == 'E'):
        n_value = 1
    else:
        print('Please select from A-E:\n\n')
        solve_A()

    r = round(int(r)/100, 5)
    r_n = r/n_value
    n_t = n_value * int(t)
    A = int(p) * ((1 + r_n) ** n_t)
    print(f'your total amount that accumulates (A) is {round(A, 3)}')


def solve_B():
    n = input(
        'Select n \nA. Daily (360) \nB. Daily (365) \nC. Monthly \nD. Quarterly \nE. Annually:\n\n')
    a = input('Input A (total amount that accumulates): ')
    r = input('Input r (interest rate):')
    t = input('Input t (time (in years)):')

    # n value
    n_value = 0
    if (n.upper() == 'A'):
        n_value = 360
    elif (n.upper() == 'B'):
        n_value = 365
    elif (n.upper() == 'C'):
        n_value = 12
    elif (n.upper() == 'D'):
        n_value = 4
    elif (n.upper() == 'E'):
        n_value = 1
    else:
        print('Please select from A-E:\n\n')
        solve_B()

    r = round(int(r)/100, 5)
    r_n = r/n_value
    n_t = n_value * int(t)
    p = int(a) / ((1 + r_n) ** n_t)
    print(f'your original principal is {round(p, 3)}')


def solve_C():
    n = input(
        'Select n \nA. Daily (360) \nB. Daily (365) \nC. Monthly \nD. Quarterly \nE. Annually:\n\n')
    a = input('Input A (total amount that accumulates): ')
    p = input('Input P (original principal):')
    t = input('Input t (time (in years)):')

    # n value
    n_value = 0
    if (n.upper() == 'A'):
        n_value = 360
    elif (n.upper() == 'B'):
        n_value = 365
    elif (n.upper() == 'C'):
        n_value = 12
    elif (n.upper() == 'D'):
        n_value = 4
    elif (n.upper() == 'E'):
        n_value = 1
    else:
        print('Please select from A-E:\n\n')
        solve_C()

    n_t = n_value * int(t)
    a_p = (int(a)/int(p)) ** (1/n_t)
    r = n_value * a_p
    print(f'your interest rate is {round(r, 2)}%')


def solve_D():
    n = input(
        'Select n \nA. Daily (360) \nB. Daily (365) \nC. Monthly \nD. Quarterly \nE. Annually:\n\n')
    a = input('Input A (total amount that accumulates):')
    p = input('Input P (original principal):')
    r = input('Input r (interest rate):')

    # n value
    n_value = 0
    if (n.upper() == 'A'):
        n_value = 360
    elif (n.upper() == 'B'):
        n_value = 365
    elif (n.upper() == 'C'):
        n_value = 12
    elif (n.upper() == 'D'):
        n_value = 4
    elif (n.upper() == 'E'):
        n_value = 1
    else:
        print('Please select from A-E:\n\n')
        solve_D()

    a_p = (int(a)/int(p))
    r_n = 1 + (int(r)/int(n_value))
    log_a_p = math.log10(a_p)
    log_r_n = math.log10(r_n)
    t = log_a_p / (n_value * log_r_n)

    print(f' {log_r_n}')

    print(f'your time (in years) is {round(t, 2)} years')


def start():
    if (unknown.upper() == 'A'):
        print('Calculate total amount that accumulates\n\n')
        solve_A()
    elif (unknown.upper() == 'B'):
        print('Calculate original principal\n\n')
        solve_B()
    elif (unknown.upper() == 'C'):
        print('Calculate interest rate\n\n')
        solve_C()
    elif (unknown.upper() == 'D'):
        print('Calculate time (in years)\n\n')
        solve_D()
    else:
        print('Please select from A-D\n\n')
        start()


start()
