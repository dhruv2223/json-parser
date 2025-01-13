def read_number(lexer, char):
    num = char
    while lexer.peek_next_char() and (lexer.peek_next_char().isdigit() or lexer.peek_next_char() in 'Ee.+-'):
        num += lexer.get_next_char()
    try:
        if 'E' in num or 'e' in num or '.' in num:
            return float(num)
        else:
            return int(num)
    except ValueError:
        raise ValueError(f"Invalid number {num}") 

def read_string(lexer):
    string_value = ""
    while True:
        char = lexer.get_next_char()
        if char == '"':
            break
        if char == '\\': 
            escaped_char = lexer.get_next_char()
            string_value += handle_escape_sequence(escaped_char)
        else:
            string_value += char

    return string_value


def handle_escape_sequence(escape_char):
    escape_dict = {
        '"': '"',
        '\\': '\\',
        '/': '/',
        'b': '\b',
        'f': '\f',
        'n': '\n',
        'r': '\r',
        't': '\t',
    }
    if escape_char in escape_dict:
        return escape_dict[escape_char]
    raise ValueError(f"Invalid escape sequence: \\{escape_char}")


def read_literal(lexer,char):
    literal = char 
    while lexer.peek_next_char() and lexer.peek_next_char().isalpha(): 
        literal += lexer.get_next_char()
    if not literal in ["true","false","null"]:
        raise ValueError("Invalid Literal")
    return literal


