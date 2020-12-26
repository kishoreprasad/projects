#!/usr/bin/python
import sys
import os
import datetime
#print (os.getcwd())
#todo_file = open(cwd+"/todo.txt",'a+')
cwd=str(os.getcwd())
def add(content):
	todo_file = open(cwd+"/todo.txt",'a+')
	if todo_file.tell()==0:
		todo_file.write("txt\n\n")
	todo_file.write(content+"\n\n")
	print('''Added todo: "'''+content+'''"''')
	todo_file.close()
def ls():
	if os.path.isfile("todo.txt"):
		todo_file=open(cwd+"/todo.txt",'r').read().split("\n\n")
		todo_file.remove("txt")
		todo_file.pop()
		if len(todo_file)==0:
			print("There are no pending todos!")
		else:
			todo_file.reverse()
			for i in range(len(todo_file)):
				print ("["+str(len(todo_file)-i)+"] "+todo_file[i])
	else:
		print("There are no pending todos!")
def delete(index):
	todo_file=open(cwd+"/todo.txt",'r').read().split("\n\n")
	todo_file.remove("txt")
	todo_file.pop()
	todo_file.reverse()
	if int(index)==0 or len(todo_file)<int(index):
		print ("Error: todo #"+index+" does not exist. Nothing deleted.")
	else:
		todo_file.pop(len(todo_file)-int(index))
		todo_file.reverse()
		todofile = open(cwd+"/todo.txt",'w+')
		todofile.write("txt\n\n")
		for todo in todo_file:
			todofile.write(todo+"\n\n")
		print("Deleted todo #"+index)


def done(index):
	todo_file=open(cwd+"/todo.txt",'r').read().split("\n\n")
	todo_file.remove("txt")
	todo_file.pop()
	todo_file.reverse()
	done_file = open(cwd+"/done.txt",'a+')
	if done_file.tell()==0:
		done_file.write("txt\n\n")
	if int(index)==0 or len(todo_file)<int(index):
		print ("Error: todo #"+index+" does not exist.")
	else:
		done_file.write("x "+datetime.datetime.today().strftime('%Y-%m-%d ')+todo_file.pop(len(todo_file)-int(index))+"\n\n")
		todo_file.reverse()
		todofile = open(cwd+"/todo.txt",'w+')
		todofile.write("txt\n\n")
		for todo in todo_file:
			todofile.write(todo+"\n\n")
		print("Marked todo #"+index+" as done.")

def help():
	print ('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')

def report():
	if os.path.isfile("todo.txt"):
		todo_file=open(cwd+"/todo.txt",'r').read().split("\n\n")
		todo_file.remove("txt")
		todo_file.pop()
		done_file=open(cwd+"/done.txt",'r').read().split("\n\n")
		done_file.remove("txt")
		done_file.pop()
		print(datetime.datetime.today().strftime('%Y-%m-%d')+ " Pending : "+str(len(todo_file))+" Completed : "+str(len(done_file)))
	else:
		print(datetime.datetime.today().strftime('%Y-%m-%d')+ " Pending : 0"+" Completed : 0")
if len(sys.argv)==1:
	help()
elif sys.argv[1]=="add":
	if len(sys.argv)<3:
		print("Error: Missing todo string. Nothing added!")
	else:
		add(sys.argv[2])
elif sys.argv[1]=="ls":
	ls()
elif sys.argv[1]=="del":
	if len(sys.argv)<3:
		print("Error: Missing NUMBER for deleting todo.")
	else:
		delete(sys.argv[2])
elif sys.argv[1]=="done":
	if len(sys.argv)<3:
		print("Error: Missing NUMBER for marking todo as done.")
	else:
		done(sys.argv[2])
elif sys.argv[1]=="help":
	help()
elif sys.argv[1]=="report":
	report()
else:
	help()