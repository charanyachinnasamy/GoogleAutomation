import re
def add_user_error_count(line):
    user_error_count={}
    pattern_error_user=r'\(.*'
    result = re.search(pattern_error_user,line)
    return result.group().split('(')[1]


print(add_user_error_count("May 27 11:45:40 ubuntu.local ticky:ERROR:Timeout while retrieving information (user03"))
