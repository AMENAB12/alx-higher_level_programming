#!/usr/bin/python3


import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # exclude the program name itself
    
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"arguments: {num_args}.")
    
    if num_args > 0:
        print("Arguments:")
        for i in range(num_args):
            print(f"{i+1}: {sys.argv[i+1]}")
