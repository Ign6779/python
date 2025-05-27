#!/usr/bin/env python3

# Goal: Compress and back up a given folder daily.

import os.path
import tarfile
import schedule
import datetime
import time

def folder_compression(output_filename, source_dir):
	with tarfile.open(output_filename, "w:gz") as tar:
		tar.add(source_dir, arcname=os.path.basename(source_dir))
	
def daily_compression(output_filename, source_dir, scheduled_time):
	schedule.every().day.at(scheduled_time).do(folder_compression, output_filename, source_dir)

	while True:
		schedule.run_pending()
		time.sleep(1)
		
# alternative
		
# def daily_compression(output_filename, source_dir, scheduled_time):
#     print(f"Waiting to run daily backup at {scheduled_time}... (CTRL+C to exit)")
#     last_run_date = ""

#     while True:
#         now = datetime.now()
#         current_time = now.strftime("%H:%M")

#         if current_time == scheduled_time and now.date().isoformat() != last_run_date:
#             folder_compression(output_filename, source_dir)
#             last_run_date = now.date().isoformat()

#         time.sleep(30)

output_filename = input("output filename: ")
source_dir = input("source directory: ")
time = input("time: ")
daily_compression(output_filename, source_dir, time)