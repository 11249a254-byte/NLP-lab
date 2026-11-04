a="abc"
state=0
for c in a:
    if state==0 and c=="a": state=1
    elif state==1 and c=="b": state=2
    elif state==2 and c=="c": state=3
    else: state=-1
print("Accepted" if state==3 else "Rejected")