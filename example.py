user_input = input("Enter your Name : ")
message = "Hello %s"% user_input
message = f"Hello {user_input}"
print(message)
print(" ")

print("for multiple string formatting")

name = input("Enter your First Name : ")
surname = input("Enter your Surname : ")

msg = "Hello %s %s"% (name,surname)
print(msg.capitalize())
print(" ")

print("arbitary function output")
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
