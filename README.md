# cs-246-networking-1

Description:

This project is -very- serious; it is a program that translates human text to onomatopoeic textual equivalents of the language spoken by dogs (since they don't actually have a writing system in place. Yet). In actuality, this program just takes in a string from the client, and exchanges the words in the string to a 'ruff' equivalent in dog sound text. 

Requirements:

- Write a program that allows one computer to communicate with another computer using either of the following:
  - Client-Server Model—You will need to write one program for the client and one program for the server. (Done)
  - Peer-to-Peer Model—You will need to write one program for the peer to both send and receive. (N/A)
- The software should implement either a collaboration system, problem solving system, file delivery system, or embedded system. Examples of each of these systems are shown in the Overview section above. The software may be written in any programming language. (Collaboration System, Done)
- Only one kind of request needs to be sent between computers, with the appropriate response. (Done, we got an echoed response, see screenshot below)
- The program can run from the command line (no graphics needed). (Done)
- You can use either TCP or UDP. (TCP, Done)

Environment Setup:

- Windows 10

- Python 3.9.1
    - Project is implemented in Python
    
- PyCharm 2020.3

- Visual Studio 2019 Version 16.8

- git version 2.29.2.windows.2 

Build and Execution Instructions:

- Clone this repository
- Initiate a Git Bash within the 'project' folder within the downloaded repository, two times
- In one terminal, run the command "python server.py"; in the other terminal, run the command "python client.py"

Screenshots:

This is an example of how to run the server and client as a user, without using PyCharm.
Though this example is from an early version of the program, the principle remains the same.

![User Usage Example](https://github.com/jmattgiroux/cs-246-networking-1/blob/main/userUseExample.png)

The two screenshots are from early development for this project, showing a successful test of the client and server recieving and sending to each other.

![screenshot of echo 1](https://github.com/jmattgiroux/cs-246-networking-1/blob/main/echo1.png)

![screenshot of echo 2](https://github.com/jmattgiroux/cs-246-networking-1/blob/main/echo2.png)

Description of Message Structure:

List of Useful Websites:
- Python Server Libraries (official site) https://docs.python.org/3.6/library/socketserver.html 
- Python Socket Libraries (official site) https://docs.python.org/3.6/library/socket.html
- Socket Programming in Python https://realpython.com/python-sockets/
