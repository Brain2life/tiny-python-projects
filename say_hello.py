#!/usr/bin/env python3

"""
Author: Maxat Akbanov
Description: Simple program to output "Hello World" into stdout
Usage: ./hello_world.py --name [your_name]
"""

import argparse


# -------------------------------------------------------------------
def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(description="Greet the person")
    parser.add_argument(
        "-n", "--name", metavar="[person_name]", default="Maxat", help="Person's name"
    )
    return parser.parse_args()


# -------------------------------------------------------------------
def main():
    args = get_args()
    print("Hello, " + args.name + "!")


# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
