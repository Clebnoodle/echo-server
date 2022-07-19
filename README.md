# Overview

This program has two parts, a client side and a server side. Once the server is running, the client side can be run to connect to the server and send it a message. The server receives the message, prints it, and then sends it back to the client.

I wrote this program to learn the basics of programming over a network.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This program uses a client/server architecture with a TCP protocol. It uses port 1234 to ensure it does not interfere with other processes. The messages are sent using utf-8.

# Development Environment

I used Visual Studio Code to develop this software.

This software uses Python with the [socket](https://docs.python.org/3/library/socket.html) library.

# Useful Websites

I found [Youtube](https://www.youtube.com/) to be the most helpful with this project. There are many videos explaining the basics of network programming.

# Future Work

* Allow the client to send multiple messages on a single connection