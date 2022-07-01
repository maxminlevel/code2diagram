import argparse
from ast import arg

def hello():
    print()

parser = argparse.ArgumentParser(description='Code to diagram')
parser.add_argument('-i','--input', help='Input file describe diagram (json, xml, csv, txt, ...)', required=True)
parser.add_argument('-t','--token', help='Describe custom token', required=False)
parser.add_argument('-o','--output', help='Output file diagram as image(jpeg, jpg, png) or text formate', required=False)
parser.add_argument('-fi','--format-input', help='Describe custom input format file', required=False)
parser.add_argument('-fo','--format-output', help='Describe custom output format file', required=False)
args = vars(parser.parse_args())

if (args['token']):
    # Generate new type token at here
    # Input: File
    # Output: New Class
    # Advice: With each class create an instance then add it to dict of abstrac Token Class
    # When new token need to create, deep copy the instance
    pass

if (args['output']):
    # Pass output type to Converter
    # Input: type
    # Output: Setting parser output
    pass

# Create new converter then setup and run with input file path
