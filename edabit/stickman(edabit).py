# 111220: went onto edabit today and this challenged has disappeared??
# did not complete

def stickman(lst):
    return [stick for stick in "0" + "-" + "|" + "--" + "<"]
    
print(stickman(["-", "O", "<", "|", "--"])) # ["O", "-", "|", "--", "<"]
print(stickman(["O", "|", "--", "-", "<"])) # ["O", "-", "|", "--", "<"]

# Not getting correct output
# Output is '-' '-' instead of '--'
