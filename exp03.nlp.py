import re
email="samhithasharma1626@gmail.com"
print("the email given is valid:",email if re.match(r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$",email) else "the email is invalid")
