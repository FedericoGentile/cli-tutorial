import argparse

def add_numbers(a, b):
    return a + b
    
def subtract_numbers(a, b):
    return a - b
    
def multiply_numbers(a, b):
    return a * b
    
def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: you cannot divide by 0!"
        
def main():
    parser = argparse.ArgumentParser(description="CLI Calculator")
    parser.add_argument('operation', choices=['add','substract','multiply','divide'], help="Math operation to perform")
    parser.add_argument('a', type=float, help="First number")
    parser.add_argument('b', type=float, help="Second number")
    args = parser.parse_args()
    
    if args.operation == 'add':
        r = add_numbers(args.a, args.b)
    elif args.operation == 'substract':
        r = subtract_numbers(args.a, args.b)
    elif args.operation == 'multiply':
        r = multiply_numbers(args.a, args.b)
    elif args.operation == 'divide':
        r = divide_numbers(args.a, args.b)
        
    print("Result:", r)
    
if __name__ == '__main__':
    main()