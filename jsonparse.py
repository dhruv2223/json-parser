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
            else:
                raise ValueError(f"Invalid Character: {char}")
        return tokens



    def read_literal(self,char):
        literal = char 
        while self.peek_next_char() and self.peek_next_char().isalpha(): 
            literal += self.get_next_char()
        if not literal in ["true","false","null"]:
            raise ValueError("Invalid Literal")
        return literal


input_json = '{"key": true, "value": null}'
lexer = Lexer(input_json)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
                
                
    
            
