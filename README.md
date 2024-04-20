# Obfusgreat

Obfusgreat is a simple Python CLI tool designed for obfuscating strings using predefined substitution rules defined in a method file.

## Installation
Clone this repository:
git clone https://github.com/yourusername/obfusgreat.git
cd obfusgreat

## Usage
Run the tool with the following command:
python obfusgreat.py -m [method_file] -c "[command_to_obfuscate]"

### Parameters:
- `-m, --method`: Specifies the method file that contains the substitution rules.
- `-c, --command`: Specifies the string that needs to be obfuscated.

### Example
Create a method file named `linux` with the following content:
';' = '${LS_COLORS:10:1}'
'ls' = '"l"s'
' ' = '%09'

Run the tool:
python obfusgreat.py -m linux -c "ls flag.txt;"
Output:
"l"s%09flag.txt${LS_COLORS:10:1}


## Creating Method Files
Method files should contain one substitution rule per line in the format:
Ensure each character and replacement is enclosed in single quotes and separated by an equals sign.
