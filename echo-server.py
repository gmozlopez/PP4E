"""
Server side: open a TCP/IP socket on a port
"""

from socket import * 
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind()