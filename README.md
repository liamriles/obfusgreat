# Obfusgreat

Obfusgreat is a Python-based command-line tool designed to obfuscate strings using substitution rules defined in a JSON method file. 

## Installation
Clone this repository:
```bash
git clone https://github.com/liamriles/obfusgreat.git
cd obfusgreat
```

## Usage
Run the tool with the following command:
python obfusgreat.py -m [method_file] -c "[command_to_obfuscate]"

### Parameters:
- `-m, --method`: Specifies the method file that contains the substitution rules.
- `-c, --command`: Specifies the string that needs to be obfuscated.

Example
Create a method JSON file named methods.json with the following content:

```json
{
  " ": "+",
  ";": "${LS_COLORS:10:1}",
  "/": "${PATH:0:1}",
  "\\": "$env:HOMEPATH[0]",
  "`": "$IFS",
  "ls": "{ls,-la}",
  "echo": "printenv",
  "\"": "${IFS:0:1}",
  "'": "${IFS:0:1}",
  "$@": "`",
  "^": "`",
  "\n": "%0a",
  "\t": "%09",
  "CMD": "echo %HOMEPATH:~6,-11%",
  "PS": "Get-ChildItem Env:"
}
```

## Run the tool:
python obfusgreat.py -m linux -c "cat /flag.txt"

Output:
'c'a't'%09${PATH:0:1}flag.txt
