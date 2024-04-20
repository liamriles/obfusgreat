import sys
import argparse
import json

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = json.load(file)
    return dictionary

def obfuscate_string(input_string, dictionary):
    for key, value in sorted(dictionary.items(), key=lambda x: -len(x[0])):
        input_string = input_string.replace(key, value)
    return input_string

def main():
    parser = argparse.ArgumentParser(description='Obfuscate strings based on a methods file.')
    parser.add_argument('-m', '--method', type=str, required=True, help='Path to the method JSON file.')
    parser.add_argument('-c', '--command', type=str, required=True, help='Command to obfuscate.')
    args = parser.parse_args()
    
    dictionary = load_dictionary(args.method)
    obfuscated_command = obfuscate_string(args.command, dictionary)
    print(obfuscated_command)

if __name__ == '__main__':
    main()
