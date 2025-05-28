#!/usr/bin/env python3

# Goal: Ping a list of IPs or domain names from a file and report which are reachable.

import os
import subprocess

command = ['ping', '-c', '1', host]

def availability_checker(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                host = line.strip()
                command = ['ping', '-c', '1', host]

                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if result.returncode == 0:
                    print(f"[UP] {host}")
                else:
                    print(f"[DOWN] {host}")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied — try running with sudo.")
    except Exception as e:
        print(f"Error: {e}")

ping_file = input("File with IP's: ).strip()
availability_checker(ping_file)