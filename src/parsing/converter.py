# interface Converter 
# - Define a template to convert a file content to uml diagram (Template design pattern):
#     - Read file and get its content.
#     - Create a lexer parse the content into list of tokens.
#     - Create parser convert these tokens into a graph.
#     - Convert the graph to uml diagram.