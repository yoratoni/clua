# Central coordinator:
- Read clua.config.yaml file (superset properties) (JSON replaced by YAML)
- Read diagnostic_messages.yaml file (diagnostic messages) (JSON replaced by YAML)
- Pre-process files (follow imports to discover all possible files)
- Tokenize & Parse (converts text to a syntax tree)
- Binder (converts identifiers in syntax tree to symbols)
- Type Check (use binder & syntax tree to look for issues in code)
- Transform (changes the syntax tree to match cluaconfig options)
- Emit (prints the syntax tree into native lua files)


## (Abstract) Syntax Tree:
    Separated into two parts, the scanner and the parser.
    - The scanner is responsible to the conversion from text into tokens.
    - The parser brings context to the scanner, it works in tandem with the scanner.


## Scanner:
    Example: const msg: string = "Hello, world"
    Separated with whitespaces, colons, semi-colons, colons.

    Diagnostics:
        Defines a bunch of rules/errors based on the correct syntax.
        Theses rules should be clear as these situations cannot appears
        with the valid syntax.


## Parser:
    Note: the parser can ask the scanner to verify the code again.
    Converts the scanner tokens into a valid syntax tree.

    Diagnostics:
        More specific than the scanner.
        It treats with errors such as a keyword used as a var identifier.
