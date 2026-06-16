comment=input("enter your comment:")
comment=comment.lower()
if( "make a lot of money" in comment or
    "buy now" in comment or
"click this " in comment or 
"subscribe this " in comment):
    print("SPAM")
else:
    print("SAFE")
