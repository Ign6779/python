#!/usr/bin/env python3

# Goal: Generate a report showing disk usage for all mounted drives.

import os
import shutil

def disk_drive_report():
    total, used, free = shutil.disk_usage("/")
    print("total space: ", total)
    print("total used: ", used)
    print("total free: ", free)

disk_drive_report()