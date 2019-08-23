print(f"Welcome to the Terminal.")
class interface():
    special_user = {
        "inquisitor" : {
            "message" : "Welcome back, Grand Inquisitor. We were awaiting your return.",
            "password" : "passinquis"
            },
        "seer" : {
            "message" : "Welcome back, Seer. We awaited your return.",
            "password" : "passseer"
            },
        "05" : {
            "message" : "We seek the truth.",
            "password" : "ohfive05"
            },
        "klencical" : {
            "message" : "The answer is simple: acquire knowledge, expand. Welcome to the interface.",
            "password" : "klencicalpass"
            },
        "courier_6": {
            "message": "Welcome back. We were waiting eagerly for your return to the Terminal.",
            "password": "deliverer"
        },
    }

def password_check(username, tries=3):
    for i in range(tries):
        user_pass = input("Enter your password: ")
        if user_pass == interface.special_user[user_name]["password"]:
            break
        else:
            if i+1 == tries:
                print("You've ran out of tries. Cutting off connection to the interface.")
                exit()
            else:
                print(f"Tries left: {tries-(i+1)}")

raw_user_name = input("Enter your username: ")
user_name = raw_user_name.lower()

if user_name in interface.special_user.keys():
    password_check(user_name)
    print(interface.special_user[user_name]["message"])

else:
    print(f"Hello, {raw_user_name}. Welcome to the Resistance.")
import time
time.sleep(1.5)
choices = {
    "What would you like to do?" : ["Access the Anomaly database","Access Site controls"],
}
answers = [0,1]
response = ["Anomaly database incomplete. Please contact the Seer.", "response2"]
alphabet = list(map(chr, range(97, 123)))
for i, (k,v) in enumerate(choices.items()):
    print(k)
    for i, (x,a) in enumerate(zip(v,alphabet)): print(f"{a}. {v[i]}")
    user_answer = input(f"Choose an answer from {[alphabet[a] for a in range(0,len(v))]}: ").lower()
    c = list(choices.keys()).index(k)
    if user_answer == alphabet[answers[c]]:
        print(response[c])
    else:
        print("Site controls are currently restricted to all users.")


end = input('Press enter key to exit.')
