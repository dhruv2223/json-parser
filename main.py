from lexer import Lexer
input_json = '''{
  "name": "John Doe",
  "age": 30,
  "isEmployed": true,
  "address": {
    "street": "123 Fake St",
    "city": "Nowhere",
    "zip": "12345"
  },
  "skills": ["Python", "C++", "Machine Learning"],
  "projects": [
    {
      "title": "JSON Parser",
      "completed": false,
      "technologies": ["Python", "Regex"]
    },
    {
      "title": "Web App",
      "completed": true,
      "technologies": ["JavaScript", "React"]
    }
  ],
  "notes": "He said: \\\"Keep it simple.\\\"",
  "pi": 3.14159,
  "scientificNumber": -6.022e23,
  "emptyArray": [],
  "emptyObject": {}
}'''

lexer = Lexer(input_json)
tokens = lexer.tokenize()
for token in tokens:
    print(token) 




