# Automata Conversion App

This project serves as the final exam submission for the Automata Theory and Formal Languages course. This application is designed to provide a comprehensive solution for converting regular expressions into their equivalent deterministic finite automata (DFA), context-free grammars (CFG), and pushdown automata (PDA). By providing conversions to these three different formal language representations, this application empowers users to choose the most suitable representation for their specific needs. Whether it's efficient pattern matching with a DFA, advanced language analysis with a CFG, or context-sensitive processing with a PDA, this application serves as a valuable tool for transforming regular expressions into their equivalent representations in various formal languages.

## How to use:
1. Download the Python file.
2. Run the Python file on any IDE.
3. Input any string of A's and B's.
4. Enjoy!

## Usage Guidelines:

### Selecting a Regular Expression:
* From the tabs above, click on the desired regular expression to begin the conversion process.
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/55226807-3de7-4293-a12a-aa7e5e81d643)
* Additionally, you can use the buttons below to directly navigate to the desired RegEx tab.
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/e35fe566-bf1f-440b-9d8c-65883ef6532e)
* When the buttons below or on the tabs above are clicked, it will proceed to the DFA Simulator of the chosen Regular Expression.
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/b52f1256-438a-43c6-aa26-5594b33c0588)

### Validating a String:
* Enter a string in the provided input field.
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/ed1aa8c8-e615-49b5-9472-6d3650338c82)
* Click the "Validate" button to check if the entered string is valid.
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/ec3f1bb8-eaa9-4d3e-8b75-91adab077746)
* The program will verify the validity of the string by traversing through each state.
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/dfe0b5b6-2f81-4d84-8f35-f3c6f8d2be24)
* When the program is valid, each state will light up to the final state. (See example in the previous section.)

### Displaying of CFG and PDA:
* If the string is valid, the application will show the equivalent CFG and PDA of the chosen regular expression.
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/4879ae3e-184e-4244-91a8-4c2461c650d7)

## Regular Expression Examples:
* (bab+bbb) a* b* (a*+b*)(ba) + (aba)(bab+aba)+bb(a+b)*(bab+aba)(a+b)*
* (1+0)*1*0*(101+01+000)(1+0)*(101+00)*(111+00+101)(1+0)*

## Deterministic Finite Automata Examples:
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/2161a695-0243-45a4-ac1c-f0afd12646ac)
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/9f851846-5d06-4410-9ca3-7ff3d579754d)

## Context Free Grammar Examples:
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/b5f2225a-4394-4b92-af31-969d655ceb36)

## Push Down Automata Examples:
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/b49bc204-f955-451e-9dfb-73bf5a672b28)
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/0bc2f64e-094a-48da-998b-ba6632f0e86e)

## Sample Outputs:
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/abe9cb6e-698f-4949-bf40-6f9fb921a3b2)
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/ae9aee6c-cfee-4b28-87ea-7764c80e7219)
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/db3f1948-04ab-4407-9d3d-e8a60ac12b11)
![image](https://github.com/10sth01/automata-conversion-app/assets/87160948/9f42fbcb-74b6-4819-a310-a216dbae66e5)

## Overview of the Concepts:
### Regular Expressions:
Regular expressions, commonly known as regex, are a potent and succinct 
tool utilized for pattern matching and manipulating text. They comprise a blend 
of literal characters, metacharacters, character classes, quantifiers, and 
anchors. Regular expressions enable users to define intricate patterns and 
accomplish various tasks such as validation, searching and replacing, 
extracting data, and parsing text. By matching specific characters, groups, or 
repetitions, regular expressions offer a versatile and streamlined approach to 
efficiently process and manipulate strings. 

### Deterministic Finite Automata
A Deterministic Finite Automaton (DFA) is a finite-state machine utilized in 
formal language theory to recognize patterns. It comprises a set of states, 
transitions based on input symbols, and accepting states. DFAs operate 
deterministically, meaning each input symbol leads to a unique next state. They 
are extensively employed for language recognition, where strings are accepted 
or rejected based on predefined rules. DFAs are graphically represented through state diagrams and find practical applications in compilers, string 
matching, and network protocol analysis. In essence, DFAs offer an effective 
and organized approach for processing and identifying patterns in strings.

### Context-Free Grammar
Context-Free Grammar (CFG) is a formal method used to describe the 
structure of languages. It involves non-terminal symbols representing 
language categories, terminal symbols representing basic units, production 
rules defining symbol replacements, and a start symbol initiating the derivation 
process. By repeatedly applying production rules, CFG enables the generation 
of valid sentences. This framework is crucial for tasks such as parsing, syntax 
tree generation, and language analysis in fields like compiler design and 
natural language processing. CFG provides a precise and structured approach 
to describe language syntax and the relationships between its components.

### Push Down Automata
A Pushdown Automaton (PDA) is an automaton that extends the capabilities of 
a finite automaton by incorporating a stack or memory tape. It is used to 
recognize and process context-free languages. PDAs consist of states, an 
input alphabet, and a stack that operates on a last-in, first-out (LIFO) principle. 
Transitions define how the PDA moves between states based on the input 
symbol and the top of the stack. PDAs can accept or reject strings based on 
defined acceptance criteria. They are used in areas such as compiler design 
and language processing to analyze and manipulate context-free languages. 
PDAs provide a formal and systematic approach to language recognition and 
manipulation by leveraging stack-based memory.

## Creators
* Janella Masongsong
* Svetlan Mauleon
* Adrian Lord Saflor
* Samantha Sampot

