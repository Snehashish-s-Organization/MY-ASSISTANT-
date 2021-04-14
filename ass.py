import json
import webbrowser
import smtplib, ssl
import pywhatkit
import pyjokes
import wikipedia


with open("data.json", "r") as file:
    data = json.load(file)
with open("data2.json", "r") as file2:
	data2 =  json.load(file2)

def play():
	song = input("enter the name of the song: \n")
	print("playong"+song)
	pywhatkit.playonyt(song)
def joke():
	print(pyjokes.get_joke())

def search():
	item = input("enter what you wanna search: \n")
	info = wikipedia.summary(item, 10)
	print(info)
def send_mail():
	sender = "snehashish.laskar@sahyadrischool.org"
	reciever = input("enter the reciever of your mail: \n")
	message = input("enter enter the message: \n")
	port = 465
	print("sending....")
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context= context) as server:
		server.login(sender, "snehashish08036")
		server.sendmail(sender, reciever, message)
		print("done!")
def add_note():
    subject = input("what is the subject of your note: \n")
    print("ok!")
    print("enter your note bellow: \n")
    note = input()
    with open("data.json", "w") as file:
        data[subject] = note
        json.dump(data, file)
    print("Added the note!")
def look_for_note():
    subject = input("what was the subject of your note?: \n")
    for i,j in data.items():
        if i == subject:
            print(j)


def list_todo():
	for i in data2:
		print(i+"\n")
def add_todo():
	item = input("enter what what you want to add: \n")
	with open("data2.json", "w") as file:
		data2.append(item)
		json.dump(data2, file)
	print("DOne")
def remove_todo():
	item = input("enter what you want to remove: \n")
	with open("data2.json", "w") as file:
		data2.remove(item)

	print("done")

def github():
	webbrowser.open("https:///github.com/")

def mail():
	webbrowser.open("https://mail.google.com")

def discord():
	webbrowser.open("https://discord.com/app")

def main():
    commands = {
            "add a note":add_note,
            "add todo": add_todo,
            "look up note": look_for_note,
            "list todo": list_todo,
            "remove a todo": remove_todo, 
            "open github":github, 
            "open discord": discord,
            "open mail":mail, 
            "hi":"Hey there!",
            "Hey!":"HI!",
            "Hi": "Heyy!",
            "sup":"nothing much i am just a bot!",
            "bye":"Bye!! See yaa!",
            "Bye":"Byeeeeee hope i can Ttyl",
            "go away":exit,
            "get lost":exit,
            "nice":"thanx!",
            "write an email": send_mail,
            "play a song":play,
            "search on wikipedia": search,
            "tell me a joke":joke,
            "thanx":"Welcome!"
            }
    while True:
	    in1 = input("->")
	    for i,j in commands.items():
	        if i in in1:
	         	if type(j) == str:
	         		print(j)
	         	else:
	         		j()
main()
