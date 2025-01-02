"""
Project Name: Hangman
Description: A fun and educational Hangman game where players guess programming-related terms.
              Each wrong guess costs a life, with 6 chances to save the man and learn new terms.
Author: Dharshan .S
Date Completed: [1/1/2025]
"""

import requests, time, random

# Hangman Structure Ascii Art
hangman = [fr'''
          +---+
          |   |
              |
              |
              |
              |
        =========''', fr'''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', fr'''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', fr'''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', fr'''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', fr'''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', fr'''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']



# Game Logo Hangman
print()
logo = [
f"\t██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗",
f"\t██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║",
f"\t███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║",
f"\t██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║",
f"\t██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║",
f"\t╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝",
]
for u in logo:
    print(f"\t{u}")
    time.sleep(0.3)

# Game Welcome menu and Description
welcome_menu = fr"""
         _____                                                        _____ 
        ( ___ )------------------------------------------------------( ___ )
         |   |                                                        |   | 
         |   |         𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐓𝐇𝐄 𝐇𝐀𝐍𝐆𝐌𝐀𝐍 𝐆𝐀𝐌𝐄                    |   | 
         |   |                                                        |   | 
         |   |  1 This game is about 'Guessing words'.                |   | 
         |   |  2 The words are terms commonly used in the            |   |
         |   |                          programming field.            |   |  
         |   |  3 You will have 6 chances to guess the word.          |   | 
         |   |  4 Each wrong answer will cost you "1" life.           |   | 
         |   |  5 Save the man and learn something new along the way! |   | 
         |   |                                                        |   | 
         |___|                              Created by - 𝐃𝐡𝐚𝐫𝐬𝐡𝐚𝐧 .𝐒  |___| 
        (_____)------------------------------------------------------(_____)
    """
print(welcome_menu)

# Dictionary of Coding Terms which are mostly used in daily life.
words = {
    "algorithm":"A set of instructions to perform a task or solve a problem.",
    "api":"A set of rules that allows different software entities to communicate with each other.",
    "array":"A collection of elements, all of the same type, stored in a single variable.",
    "variable":"A container used to store data values.",
    "loop":"A programming structure that repeats a block of code while a condition is true.",
    "function":"A block of code designed to perform a specific task.",
    "class":"A blueprint for creating objects in object-oriented programming.",
    "object":"An instance of a class, containing both data and methods.",
    "method":"A function that is defined inside a class and operates on objects of that class.",
    "inheritance":"A feature of object-oriented programming where a class can inherit attributes and methods from another class.",
    "polymorphism":"The ability of a single function or method to operate on different types of data.",
    "encapsulation":"The concept of bundling data and methods that operate on the data into a single unit, i.e., a class.",
    "debugging":"The process of identifying and fixing errors in code.",
    "compilation":"The process of translating source code into machine code that a computer can execute.",
    "syntax":"The set of rules that defines the structure of valid code in a programming language.",
    "binary":"A number system that uses two digits, 0 and 1, to represent data.",
    "bit":"The smallest unit of data in computing, represented by 0 or 1.",
    "byte":"A group of 8 bits, commonly used to represent a character or small data unit.",
    "stack":"A data structure where elements are added or removed in a last-in, first-out (LIFO) order.",
    "queue":"A data structure where elements are added or removed in a first-in, first-out (FIFO) order.",
    "recursion":"A technique where a function calls itself to solve a problem.",
    "hashing":"The process of converting data into a fixed-size value for quick lookups.",
    "hashmap":"A data structure that stores key-value pairs for fast data retrieval.",
    "database":"A structured collection of data that can be accessed, managed, and updated.",
    "sql":"A language used to manage and query relational databases.",
    "nosql":"A non-relational database model used for handling large amounts of unstructured data.",
    "csv":"A file format that stores tabular data in plain text, using commas to separate values.",
    "json":"A lightweight data-interchange format that is easy for humans to read and write.",
    "xml":"A markup language used to encode documents in a format that is both human-readable and machine-readable.",
    "http":"The protocol used for transferring data over the web.",
    "https":"A secure version of HTTP, using encryption for secure data transfer.",
    "html":"A markup language used to structure content on the web.",
    "css":"A stylesheet language used to describe the presentation of web pages.",
    "javascript":"A programming language used to create interactive effects within web browsers.",
    "nodejs":"A JavaScript runtime built on Chrome's V8 engine, used for building server-side applications.",
    "express":"A web application framework for Node.js, used to build APIs and server-side applications.",
    "frontend":"The part of web development that deals with the user interface and user experience.",
    "backend":"The part of web development that deals with the server, database, and application logic.",
    "fullstack":"A developer who is proficient in both front-end and back-end development.",
    "authentication":"The process of verifying the identity of a user or system.",
    "authorization":"The process of granting or denying access to resources based on permissions.",
    "oauth":"A standard for access delegation commonly used for token-based authentication.",
    "session":"A temporary connection between a user and a web application, used to maintain state across requests.",
    "cookie":"A small piece of data stored in the browser that can hold user preferences or session data.",
    "jwt":"JSON Web Token, a compact and self-contained way to represent information between parties.",
    "docker":"A platform used to automate the deployment and management of applications in containers.",
    "kubernetes":"An open-source platform for automating the deployment, scaling, and management of containerized applications.",
    "cloudcomputing":"The delivery of computing services (e.g., storage, processing) over the internet.",
    "saas":"Software as a Service, a model where software is hosted on the cloud and accessed via the internet.",
    "iaas":"Infrastructure as a Service, a model where users rent computing infrastructure from a cloud provider.",
    "paas":"Platform as a Service, a cloud computing model that provides a platform for building and deploying applications.",
    "machinelearning":"A type of artificial intelligence where computers learn from data and improve their performance over time.",
    "deeplearning":"A subset of machine learning that uses neural networks with many layers to analyze large amounts of data.",
    "neuralnetwork":"A system of algorithms designed to recognize patterns, modeled after the human brain.",
    "datascience":"The field that combines computer science, statistics, and domain knowledge to extract insights from data.",
    "bigdata":"Large, complex datasets that traditional data-processing software cannot handle efficiently.",
    "datamining":"The process of discovering patterns and knowledge from large datasets.",
    "datavisualization":"The representation of data in graphical form to help understand and interpret it.",
    "git":"A distributed version control system used to track changes in source code during software development.",
    "github":"A platform for hosting and sharing Git repositories.",
    "gitlab":"A platform for Git repository management and continuous integration/continuous deployment.",
    "unittest":"A test that verifies the functionality of a specific part of the code (usually a function or method).",
    "integrationtest":"A test that verifies the interactions between different components of the system.",
    "agile":"A methodology for software development that emphasizes flexibility, collaboration, and rapid iterations.",
    "scrum":"An agile framework for managing projects with iterative progress and regular feedback.",
    "kanban":"A project management method that uses visual boards to track work in progress.",
    "devops":"A set of practices that combines software development and IT operations to automate and improve the software lifecycle.",
    "versioncontrol":"The process of managing changes to source code over time, using systems like Git.",
    "containerization":"The process of packaging an application and its dependencies into a container for consistent execution across environments.",
    "virtualization":"The creation of virtual instances of hardware or software for efficient resource management.",
    "firewall":"A security system that monitors and controls incoming and outgoing network traffic.",
    "encryption":"The process of converting data into a secure format to prevent unauthorized access.",
    "decryption":"The process of converting encrypted data back into its original format.",
    "ssl":"Protocols for securing communication over the internet, commonly used for encrypting web traffic.",
    "httprequest":"A message sent from a client to a server to request resources or perform an action.",
    "rest":"Representational State Transfer, an architectural style for designing networked applications using stateless communication.",
    "soap":"Simple Object Access Protocol, a messaging protocol used for exchanging structured information between systems.",
    "rpc":"Remote Procedure Call, a protocol for executing code on a remote server.",
    "middleware":"Software that connects different applications or services, providing common functionality like authentication.",
    "cloudstorage":"The online storage of data that can be accessed and managed through the internet.",
    "cdn":"Content Delivery Network, a system of distributed servers that deliver content to users based on their geographic location.",
    "scalability":"The ability of a system to handle an increasing amount of work or to be enlarged to accommodate growth.",
    "latency":"The time delay between sending a request and receiving a response.",
    "throughput":"The amount of data transmitted or processed by a system in a given period of time.",
    "vpn":"Virtual Private Network, a technology that creates a secure, encrypted connection between a user and a network over the internet.",
    "proxy":"A server that acts as an intermediary between a client and another server to control requests and responses.",
    "dns":"Domain Name System, a system that translates domain names into IP addresses.",
    "ipaddress":"A unique identifier assigned to each device on a network to enable communication.",
    "subnet":"A segment of a larger network, created by dividing an IP address into smaller parts for more efficient routing."
}

# Main class
class Game:
    def __init__(self,u_name):
        self.u_name = u_name

    # Random motivational quote generator
    @staticmethod
    def motivational_quotes(u_name):
        url = fr"https://zenquotes.io/api/random"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            reply = f"{u_name}! {quote}\t- {author}"
            print(f"╭{'-'*(len(reply)+2)}╮\n│ ",end='')
            for a in reply:
                print(a, end='')
                time.sleep(0.03)
            print(f" │\n╰{'-'*(len(reply)+2)}╯", end='')
        else :
            for b in f"{u_name}! You are more than you think!":
                print(b, end='')
                time.sleep(0.03)

    # Actual game start here
    def start_game(self):
        key_word = random.choice(list(words.keys()))
        value_word = words[key_word]
        underscore_word = []
        underscore_word += '_'*len(key_word)
        count = 6

        # Display hangman and life's
        def display():
            print(f"\t┌{'━'*(len(underscore_word)+2)}┐")
            print(f"\t│ ",end='')
            for ch in range(len(underscore_word)): print(underscore_word[ch], end='')
            print(f" │\n\t└{'━' * (len(underscore_word)+2)}┘")
            print(hangman[6 - max(count, 0)])
            print(f"\nLIFE'S = {'❤'*count}\n{'-' * 40}")

        # Game end decision
        def decide():
            if underscore_word == list(key_word):
                print(f"\n{self.u_name} 🥳🎉 You won the game\n")
                end_cards()
                Game.motivational_quotes(self.u_name)
                exit()
            elif count < 1:
                print(f"\n{self.u_name} 😔😟 You lost the game\nTHE WORD WAS = [ '{key_word}' ]\n")
                end_cards()
                Game.motivational_quotes(self.u_name)
                exit()

        # End cards of the game
        def end_cards():
            print(f"  ➥ What is {key_word} ?")
            print(f"\t'{key_word.upper()} ' : {value_word}\n\n")
            print(f"{'⇢'*20}{'✦✧✦✧✦✧':^10}{'⇠'*20}\n")
            print(f'{"𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝐟𝐨𝐫 𝐩𝐥𝐚𝐲𝐢𝐧𝐠 𝐭𝐡𝐞 𝐠𝐚𝐦𝐞! 𝐇𝐞𝐫𝐞'𝐬 𝐚 𝐪𝐮𝐨𝐭𝐞 𝐟𝐨𝐫 𝐲𝐨𝐮":^10}')

        print(f"\n\t{self.u_name}! Guess this word 😉: ", end="")
        for l in underscore_word:
            print(l, end='')
            time.sleep(0.2)

        # Game control loop
        while True:
            decide()
            letter = input("\n\t𝐄𝐧𝐭𝐞𝐫 𝐚 𝐥𝐞𝐭𝐭𝐞𝐫 : ").casefold().strip()

            if not letter.isalpha():
                print(f"\t['{letter}'] : is Invalid Character Try again please")
                continue
            elif len(letter) > 1:
                print(f"\t['{letter}'] : is Invalid 'Only single Character is allowed'")
                continue
            elif letter in underscore_word:
                print(f"\t['{letter}'] : is already Guessed")
                display()
                continue
            elif letter not in key_word:
                count -= 1
                print(f"\t['{letter}'] : is Wrong Guess, You will loose 1 life")
                display()
                continue
            print(f"\t['{letter}'] : is a Correct Guess")
            for i in range(len(key_word)):
                if letter == key_word[i]: underscore_word[i] = key_word[i]
            display()

# object of game
name = input("\t𝐄𝐧𝐭𝐞𝐫 𝐲𝐨𝐮 𝐧𝐚𝐦𝐞 : ")
quotes = Game(name)
quotes.start_game()

