"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    frequencies = {}
    for val in items:
        if str(val) not in frequencies:
            frequencies[str(val)] = 1
        else:
            frequencies[str(val)] += 1
    return frequencies
    