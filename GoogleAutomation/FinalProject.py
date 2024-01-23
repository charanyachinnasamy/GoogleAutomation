#!/usr/bin/env python3
import operator
import re
import csv
error_message_count = {}
user_error_count={}
user_info = {}
#This function will read each line of the syslog.log file and check if it is an error or an info message.
def search_file():
    with open('syslog.log',"r") as myfile:
        for line in myfile:
            if 'ERROR' in line:
                extract_error_msg(line)
                add_user_error_count(line)
            elif 'INFO' in line:
                add_user_info_count(line)

def extract_error_msg(line):
    match = re.search(r'(ERROR [\w \[]*)',line)
    error_message = match.group(0).replace("ERROR ", "").strip()
    if error_message=="Ticket doesn":
        error_message= "Ticket doesn't exist"
    if error_message in error_message_count:
        error_message_count[error_message] = error_message_count[error_message] + 1
    else:
        error_message_count[error_message] = 1

def add_user_error_count(line):
    match = re.search(r'\(.*?\)', line)
    user = match.group(0)
    error_user = user.strip("()")
    if error_user in user_error_count:
        user_error_count[error_user]=user_error_count[error_user]+1
    else:
        user_error_count[error_user]=1


def add_user_info_count(line):
    match = re.search(r'\(.*?\)', line)
    user = match.group(0)
    info_user = user.strip("()")
    if info_user in user_info:
        user_info[info_user]=user_info[info_user]+1
    else:
        user_info[info_user]=1


def error_count_output_csv(error_message_count):
    error_message_count = sorted(error_message_count.items(),key=operator.itemgetter(1),reverse=True)
    with open('error_message_count.csv','w') as output:
        fieldnames = ['Error', 'Count']
        csvw = csv.DictWriter(output,fieldnames=fieldnames)
        csvw.writeheader()
        for key,value in error_message_count:
            csvw.writerow({'Error':key, 'Count':value})
    return

def user_statistics_csv(user_error_count,user_info):
    for key,value in user_error_count.items():
        if key in user_info:
            user_info[key]=user_info[key],value
        else:
            user_info[key]= (0,value)
    for key in user_info.keys():
        if key not in user_error_count:
            user_info[key]=user_info[key],0
    user_info = sorted(user_info.items(),key=operator.itemgetter(0))
    with open('user_statistics.csv','w') as output:
        fieldrows=['Username','INFO','ERROR']
        csvw = csv.DictWriter(output,fieldnames=fieldrows)
        csvw.writeheader()
        for key ,value in user_info:
            csvw.writerow({'Username':key,'INFO':value[0],'ERROR':value[1]})
    return

search_file()
error_count_output_csv(error_message_count)
user_statistics_csv(user_error_count,user_info)







