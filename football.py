import socket
from bs4 import BeautifulSoup as bs
import requests
from tabulate import tabulate
from termcolor import colored
import sys



def connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

Ip=connection()
if(Ip==False):
	print("SCORES NOT ACCESSIBLE")
else:
	arg=sys.argv
	date=arg[1]
	
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
	url='https://www.goal.com/en-in/results/'+date;

	response=requests.get(url,headers=headers)
	soup=bs(response.content,features="lxml")

	away=[]
	k=0
	for i in soup.findAll("div",class_=["competition-matches"]):
		c_name=i.find("div",class_=["competition-name"]).getText()
		print(colored(c_name,"blue"))
		teams=[]
		t_score=[]
		for j in i.findAll("div",class_=["match-data"]):
			h=[]
			h1=j.find("div",class_=["team-home"])
			sc=h1.find("span",class_=["goals"])
			h1=h1.find("span",class_=["team-name"])
			h.append(h1.getText())
			h.append(sc.getText())
			a1=j.find("div",class_=["team-away"])
			sc=a1.find("span",class_=["goals"])
			a1=a1.find("span",class_=["team-name"])
			h.append(sc.getText())
			h.append(a1.getText())

			teams.append(h)

		headers=["team-home","Score","Score","team-away"]
		if(len(teams)==0):
			print("NO MATCHES FOUND FOR THE GIVEN DATE")
		else:
			print(colored(tabulate(teams,headers,tablefmt="grid"),"white"))







