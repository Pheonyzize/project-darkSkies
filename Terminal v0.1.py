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
        "Courier 6": {
            "message": "Welcome back. We were waiting eagerly for your return to the Terminal.",
            "password": "deliverer"
        },
    }

def password_check(username, tries=3):
    for i in range(tries):
        user_pass = input("Enter your password: ")
        if user_pass == interface.special_user[user_name]["Password"]:
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

end = input('press enter key to exit')
