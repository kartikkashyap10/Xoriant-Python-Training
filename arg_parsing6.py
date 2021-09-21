import argparse

class Employee:
    def __init__(self, no_of_employee):
        self.no_of_employee = no_of_employee
        print('No. of Employees: ', no_of_employee)

    def add(self, a, b):
        print(a + b)

    def sub(self, a, b):
        print(a - b)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('no_of_employee', help='employee', type=int)

    parser.add_argument('a', help='employee', type=int)
    parser.add_argument('b', help='employee', type=int)

    args = parser.parse_args()

    e1 = Employee(args.no_of_employee)
    e1.add(args.a, args.b)
    e1.sub(args.a, args.b)