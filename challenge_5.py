#!/usr/bin/env python3

# Goal: Parse /var/log/auth.log or /var/log/syslog and count failed login attempts.

import os
import re

def failed_login_counter():
	counter = 0
	
	with open('/var/log/auth.log', 'r') as file:
		for line in file:
			if re.search(r"Failed password|authentication failure", line): counter += 1

	print(f"failed login attempts: {counter}")

failed_login_counter()