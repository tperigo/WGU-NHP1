# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# Main.py1

from UserInterface import UserInterface


""" BIG-O Analysis:
This application runs in polynomial time complexity O(n^2)

Each block of code will have their simplified upper-bound big-0 complexity above it in triple quotes. 
"""

'''O(n^2)'''
def main():
    """
    Start the WGUPS program by running the command line interface
    """
    UserInterface()


'''O(1)'''
if __name__ == "__main__":
    main()
