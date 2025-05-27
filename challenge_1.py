#!/usr/bin/env python3

# Goal: Create a script that deletes files older than X days in a given directory.
import os
import time

def delete_files_by_age(directory, days):

    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        st = os.stat(filepath)
        file_age = time.time() - st.st_mtime

        if file_age > days:
            if os.path.isfile(filepath):
                os.remove(filepath)

directory = input("directory: ")
days = float(input("file days: ")) * 86400
delete_files_by_age(directory, days)
    