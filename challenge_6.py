#!/usr/bin/env python3

# Goal: Script that adds/removes/checks cron jobs.

import os
from crontab import CronTab
import subprocess

jobScheduler = CronTab(user='root')

def add_cronjob(command):
    job = jobScheduler.new(command=command)
    job.hour.every(1)
    job.enable()
    jobScheduler.write()
    print("Job added to run every hour.")

def remove_cronjob(command):
    removed = False
    for job in jobScheduler:
        if job.command == command:
            jobScheduler.remove(job)
            jobScheduler.write()
            print(f"Removed job: {command}")
            removed = True
            break
    if not removed:
        print("Job not found.")

def check_cronjobs():
	for job in jobScheduler:
		print(job)

print("[1] Add cronjob")
print("[2] Remove cronjob")
print("[3] View cronjobs")

choice = input("Choose one: ")

match choice:
    case "1":
        command = input("Write your command: ")
        add_cronjob(command)
    case "2":
        command = input("Enter the command of the job to remove: ")
        remove_cronjob(command)
    case "3":
        check_cronjobs()
    case _:
        print("Not a valid choice.")



	