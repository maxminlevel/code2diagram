# Code to UML Diagram
## Why ?

<img src="docs/images/reason.png" alt="Reason"/>


## How ?

### Data structure:

#### abstract class FileContent

(Define how content read from file is stored)
- concrete class TextFileContent
- concrete class CSVFileContent
- concrete class JSONFileContent
- concrete class XMLFileContent

#### [class Position](https://codemaster138.github.io/blog/creating-an-interpreter-part-1-lexer/)

(Keep track of positioning information of our parsing code process.)

#### abstract class Token

(Contain information about each token of our language)
- concrete class ArrowToken
- concrete class ActorToken
....


#### class UMLGraph
Contain information about our uml diagram relationships


#### interface Converter 
- Define a template to convert a file content to uml diagram (Template design pattern):
    - Read file and get its content.
    - Create a lexer parse the content into list of tokens.
    - Create parser convert these tokens into a graph.
    - Convert the graph to uml diagram.

--> Others can freely create their own Converter


### IO:
    class Reader (define how content is read with different file formats)
        - Read file module applied Flexible object (format - stategy to read). 
        - Input: file name
        - Output: instance of FileContent
        - Use Strategy design pattern to read the file (based on its extension).
    --> Others can freely create a Reader for new file format

### Parse code:
    Create class Lexer parse codes to tokens:
        - Input: Code content (FileContent)
        - Output: List of tokens 
        - For applying Visitor pattern, we use FileContent concrete classes as visitors
        - Has different overload parse methods for every FileContent concrete class
    
    Create class Parser parse list of tokens into a graph represent our diagrams:
        - Input: List of tokens
        - Output: A graph:
            - Node: Actor, usecase, class
            - Edges: Different kinds of arrow


### Export to UML diagram

Add to_uml method to UMLGraph to export a graph in [DOT language with graphviz](https://pypi.org/project/graphviz/?fbclid=IwAR3bsmvtZV3OnTI6pB7ix31h5I4MrgY5z8eFH1KN29g7EFmWOIpzlsHCTpA).

## Contributor


