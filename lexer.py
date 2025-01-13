from utils import read_string,read_number,read_literal

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
                tokens.append(self.create_token("STRUCTURE",char))
                
            elif char.isalpha(): 
                literal = read_literal(self,char)
                tokens.append(self.create_token("LITERAL",literal))
            elif char == '"':
                string_value = read_string(self)
                tokens.append(self.create_token("STRING",string_value))
            elif char.isnumeric() or char == '-': 
                number = read_number(self,char)
                tokens.append(self.create_token("NUMBER",number))
            else:
                raise ValueError(f"Invalid Character: {char}")
        return tokens 

    def create_token(self,token_type,value):
        return {"type":token_type,"value":value}




