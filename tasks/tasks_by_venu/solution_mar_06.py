class MyFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with MyFile('myfile.txt', 'w') as f:
        f.write('Hello, world!')

import smtplib    
from email.mime.multiparst import MIMEMultipart
from email.mime.text import MIMEText

admin_email = 'admin@yourcompany.com'
customer_email = 'customer@example.com'
cc_emails = ['cc1@example.com', 'cc2@example.com']

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Goods Arrival Notification'
msg['From'] = admin_email
msg['To'] = customer_email
msg['Cc'] = ', '.join(cc_emails)


html = """\
<html>
    <head></head>
    <body>
        <p>Dear customer,</p>
        <p>We are pleased to inform you that your goods have arrived and are ready for pickup.</p>
        <p>Thank you for choosing our company.</p>
    </body>
</html>
"""

msg.attach(MIMEText(html, 'html'))
smtp_obj = smtplib.SMTP('smtp.yourcompany.com', 587)
smtp_obj.starttls()
smtp_obj.login(admin_email, 'yourpassword')
smtp_obj.sendmail(admin_email, [customer_email] + cc_emails, msg.as_string())
smtp_obj.quit()

# 26. You are given a string S. Your task is to find the indices of the start and end of string k in 
# S
# The first line contains the string S.The second line contains the string k. 
# Print the tuple in this format: (start _index, end _index). If no match is found, print (-1, 
# -1). 
# Sample Input 
# Sample Output
# aaadaa
# aa
# (0, 1)
# (1, 2)
# (4, 5)

def get_substr_pos(main_str, sub_str):
    count = 0
    len_of_mstr = len(main_str)
    len_of_substr = len(sub_str)

    for index in range(len_of_mstr):
        if  main_str[index:index + len_of_substr] == sub_str:
            print((index, index + len_of_substr - 1))
            count += 1

    if not count:
        print((-1, -1))

S = input()
k = input()

get_substr_pos(S, k)



# 27. Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid 
# but "[)", "({[)]" and "{{{" are invalid.
def check_valid_parentheses(brackets):
    valid = {')': '(', '}': '{', ']': '['}
    res = [] 
    left_brackets = ['(', '{', '[']
    right_brackets = [')', '}', ']']

    for bracket in brackets:
        if bracket in right_brackets:
            if len(res) == 0:
                return (False)
                break
            elif res[-1] == valid[bracket]:
                res.pop(-1)
            elif res[-1] != valid[bracket]:
                return (False)
                break
        elif bracket in left_brackets:
            res += bracket

    return len(res) == 0

print(check_valid_parentheses("[]{}()"))

print(check_valid_parentheses("["))
print(check_valid_parentheses("[)"))
print(check_valid_parentheses(""))
print(check_valid_parentheses("[({})]"))


# 28. Write a Python program to remove the parenthesis area in a string using Regular 
# Expression 
# Sample data : ["example (.com)", "MSys", "github (.com)", "keka (.com)"] 
# Expected Output: 
# Example 
# MSys 
# github 
# keka 


import re

data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]

for s in data:
    s = re.sub(r'\([^)]*\)', '', s)
    print(s.strip())


# 29. Write a regular expression to find the html tags that are more than 4 letters. 
# Note: Html tags can be found inside <> characters and closing html tags can be found in 
# the same format after / character. </> 
# i.e.: <param> </param> 

html = '''
<head>
    <title>Python Re</title>
</head>
<body>
    <header>
        <h1>Find all tags with more than 5 character</h1>
    </header>
    <article>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, cumque!</p>
    </article>
    <footer>
        <h3>End of body.</h3>
    </footer>
</body>
</html>
'''

pattern = re.compile("\<[^/][^>][a-z]*\>|\<\/[^>][a-z]*\>")
result = pattern.findall(html)

for tag in result:
    print(tag)