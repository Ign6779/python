#!/usr/bin/env python3

# Goal: List all processes using psutil. Print CPU and memory usage.

import os
import psutil

def process_list():
    processes = psutil.process_iter()

    for process in processes:
        print(f"Process ID: {process.pid}, Name: {process.name()}, CPU: {process.cpu_percent(interval=1.0)}, Memory: {process.memory_info().rss}")

process_list()