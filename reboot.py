#!/usr/bin/env python
#  Reboot all PI 
import paramiko
import time
from flask import jsonify

def rb(host, port, username, password, keyfilepath, keyfiletype, command):
    ssh = None
    key = None
    try:
        if keyfilepath is not None:
            # Get private key used to authenticate user.
            if keyfiletype == 'DSA':
                # The private key is a DSA type key.
                key = paramiko.DSSKey.from_private_key_file(keyfilepath)
            else:
                # The private key is a RSA type key.
                key = paramiko.RSAKey.from_private_key(keyfilepath)
 
        # Create the SSH client.
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
        # Connect to the host.
        if key is not None:
            # Authenticate with a username and a private key located in a file.
            ssh.connect(host, port, username, None, key)
        else:
            # Authenticate with a username and a password.
            ssh.connect(host, port, username, password)
 
        # Send the command (non-blocking)
        stdin, stdout, stderr = ssh.exec_command(command)
 
        # Wait for the command to terminate
        while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
            time.sleep(1)
 
        stdoutstring = stdout.readlines()
        stderrstring = stderr.readlines()
        return stdoutstring, stderrstring
    finally:
        if ssh is not None:
            # Close client connection.
            ssh.close()
 
 

def rb2():
    host = ''
    port = 22
    username = '<PI USERNAME>'
    password = '<PI PASSWORD>'
    keyfile_path = 'private_key_file'
    pis = open("pis.txt").read().split('\n')
    for line in pis:
        rb(line, port, username, password, None, None, "sudo reboot")
    return "success"
