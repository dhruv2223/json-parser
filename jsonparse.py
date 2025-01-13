class Lexer:
    def __init__(self,input_string):
        self.input = input_string
        self.position = 0
        self.length = len(input_string)
     
    def get_next_char(self):
        char = self.input[self.position] 
        self.position += 1
        return char
    def peek_next_char(self):
        if self.position<self.length:
            return self.input[self.position]
        else:
            return None
 
    def tokenize(self):
        tokens = [] 
        while self.position<self.length:
            char = self.get_next_char()
            if char in " \t\n\r":
                continue
            if char in "{}[],:":
                tokens.append({"type":"STRUCTURE","value":char})
                
            elif char.isalpha(): 
                literal = self.read_literal(char)
                tokens.append({"type":"LITERAL","value":literal})
            elif char == '"':
                string_value = self.read_string(char)
                tokens.append({"type":"STRING","value":string_value})
            elif char.isnumeric() or char == '-': 
                number = self.read_number(char)
                tokens.append({"type":"NUMBER","value":number})
            else:
                raise ValueError(f"Invalid Character: {char}")
        return tokens
    
    def read_number(self,char):
        num = char
        while self.peek_next_char() and (self.peek_next_char().isdigit() or self.peek_next_char() in 'Ee.+-'): 
            num += self.get_next_char()
        try:
            if 'E' in num or 'e' in num or '.' in num:
                return float(num)
            else:
                return int(num)
        except ValueError:
            raise ValueError(f"Invalid number {num}")
                
     
    def read_string(self,char):
        string_value = ""
        while True:
            char = self.get_next_char()
            if char == '"':
                break
            if char == '\\':
                escape_char = self.get_next_char()
                if escape_char == '"':
                    string_value += '"'
                elif escape_char == '\\':
                    string_value += '\\'
                elif escape_char == '/':
                    string_value += '/'
                elif escape_char == 'b':
                    string_value += '\b'
                elif escape_char == 'f':
                    string_value += '\f'
                elif escape_char == 'n':
                    string_value += '\n'
                elif escape_char == 'r':
                    string_value += '\r'
                elif escape_char == 't':
                    string_value += '\t'
                else:
                    raise ValueError(f"Invalid escape sequence: \\{escape_char}")
            else:
                string_value += char

        return string_value

    def read_literal(self,char):
        literal = char 
        while self.peek_next_char() and self.peek_next_char().isalpha(): 
            literal += self.get_next_char()
        if not literal in ["true","false","null"]:
            raise ValueError("Invalid Literal")
        return literal


input_json = '{"key": 123, "value": -4.56e2}'
lexer = Lexer(input_json)
tokens = lexer.tokenize()
for token in tokens:
    print(token) 
