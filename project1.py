import colorama
from colorama import Fore, Back, Style
import random
colorama.init(autoreset=True)

colors = [Fore.RED, Fore.BLUE, Fore.GREEN]
Recently_Added=False
h=3
t=False
y=3
class Places():
	def __init__(self,name,about,link):
		self.name = name
		self.about = about
		self.link = link

SOS = Places("SOS", "SOS Pets was founded in 1979 and has since been working tirelessly for the welfare and rescue of thousands of homeless dogs and cats.\nIf you love animals You too can help our organization in many different ways.\nYou can either volunteer in our adoption days which are being held each weekend serve as a foster home \nfor a dog or for a cat for a short period of time or donate to our organization in different ways.", "https://www.sospets.co.il/volunteer")

Salametkom = Places("Salametkom", "Salametkom (Your Safety) - ‏The organization “Your Safety” started with a simple idea!\nIt is represented in providing assistance to Arab patients in Israeli hospitals, especially in translation!\nBut within a short period, ""Your Safety"" became an important address, and the only one in most cases,in many hospitals in Jerusalem and the Center\nin order to provide assistance to thousands of Palestinian patients from the West Bank and Gaza:\nin medical coverage, transportation, medical equipment and tools, in addition to recreational activities inside and outside hospitals.", "https://salametcom.herokuapp.com/" )

MDA = Places("MDA", "Magen David Adom, in conjunction with the Israel Experience, has the perfect program for you.\nCome make a difference in Israel! Be trained as an ambulance first responder (EMS).\nVolunteer on ambulances throughout Israel.\n Where else in the world can you do this? Be on the forefront of emergencies in Israel!", "https://www.mdais.org/en/volunteers")

Make = Places("Make A Wish", "Come join us in the fulfilment of wishes for children with critical illnesses between the ages of 3-18.\nLet’s transform tears and fear into laughter and joy!\nTogether we can help give these children their innocence and childhood back.","https://makeawish.org.il/en/home-page/")

Latet = Places("Latet","Latet (To Give) - was established in order to reduce poverty, for a better and just society\nby providing assistance to needy populations, mobilizing Israeli civil society towards mutual responsibility\nand leading change in the national priorities.", "https://www.latet.org.il/en/")

Seeds = Places("Seeds Of Humanity", "Seeds of Humanity is a Palestinian organization, was founded by motivated individuals in 2015\ndue to the ongoing refugee crisis in Europe, since then it has been expanded to serve refugees across the globe\nby helping them to fulfill their rights to live a dignified life regardless of color, religion and nationality.","https://www.seedsofhumanity.org/")
class Stories():
	def __init__(self,place,story):
		self.place = place
		self.story = story


Places_Dict={
	1:"sos",
	2:"salametkom",
	3:"mda",
	4:"make a wish",
	5:"latet",
	6:"seeds of humanity",
}
Places_Dict_Check={
	1:"sos",
	2:"salametkom",
	3:"mda",
	4:"make a wish",
	5:"latet",
	6:"seeds of humanity",
	
}

Smda= Stories("MDA", "My name is Roni Tomshof, I'm seventeen years old and I believe MDA is a place where you can constantly grow and develop.\nYou can constantly expand and develop your knowledge, and there are always things to strive to reach.\nThis volunteering never gets repetitive. No case will be exactly like the previous one. This volunteering is special, amazing and very enriching. \nWe reach people in some of the most difficult situations, and we end up bringing them to the hospital with a smile. There is nothing more satisfying than that. \nIt is an organization that deals with saving lives and the very fact that you are a part of it is already a source of pride.")
Ssos= Stories("SOS","My name is Amit Hadar, I'm fifteen years old and volunteering at SOS Pets was one of the best things I've decided to do!\nI've loved animals my whole life so volunteering at SOS Pets was just as enjoyable and meaningful for me as it was for the families that came to adopt our pets.\nI would 10/10 recommend volunteering at SOS Pets for anyone who likes working and having fun with animals.")
Slatet= Stories("Latet","My name is Talia Struminski, I'm fifteen years old and while volunteering at Latet I understood that there is a place for every single person who wants to volunteer. \nWhether it's sorting food, carrying boxes, driving a truck or making phone calls - \nthere's a place for you all! My personal experience was incredible and what made it even better is that after a long day of hard work\nyou sit down and you know that thanks to your work people are going to have something to eat!")
Swish= Stories("Make A Wish", "My name is Hadeel Jaber, I'm eighteen years old and I belive in dreams comming true.\nI remember the first time I came to this place, I was so excited from the children’s excitement and the hard work the organization does for achieving these children’s dreams. \nAt first I thought that children forgot about their patients and only waited for their dreams to come true, but after we achieved their dreams \nI was surprised to see that the children have more hope in life and they look at things in more positive sides. \nSeeing the children’s happiness is the most touching thing I can do. I recommend you to join our family, join Make a wish organization!")
Ssalam= Stories("Salametkom","My name is Nisreen Abu Qtash, I'm eighteen years old and while volunteering at Salametkom I felt the real feeling of hapiness and I how important \nit is to help family's from my culture, people that struggle the same struggles I went through. \nAs a child I remember not knowing to speack hebrew and how hard was it to communicate with other people. \nIt was really important for me to learn hebrew and help people from my society that don't know to talk. \nSeeing the childrens and family's hapiness by giving them and helping them with the simpelest thing makes my day. \nJoin Salametkom to feel the real feeling of happiness! ")

story_dict = {
	"SOS By- Amit Hadar":(Ssos.story),
	"Latet By- Talia Struminski":(Slatet.story),
	"MDA By- Roni Tomshof":(Smda.story),
	"Make A Wish By- Hadeel Jaber":(Swish.story),
	"Salametkom By- Nisreen Abu Qtash":(Ssalam.story)
	}

class User():
	def __init__(self,name,second,UserName,Password,VolPlace):
		self.UserName= UserName
		self.Password= Password
		self.VolPlace= VolPlace
		self.name= name
		self.second=second
		
	def Change_psw(self):
			
			old= input("Enter your Password to continue:")
			while old!= self.Password and y>0:
				check= input("Sorry, wrong Password, try again!")
				y-=1
				
			if old==self.Password:
				New_Password= input("Type your new Password:")
				check= input("Confirm your new Password:")
				y=3
				while check!=New_Password and y>0:
					check= input("Wrong Password! Confirm your new Password:")
					y-=1
					
					
				if check==New_Password:
					self.Password=New_Password
					print("Password has been changed!")
					print(Fore.GREEN +"\n______________________________________________________\n")
					
	def Change_User(self):
		check= input("Enter your Password to continue:")
		
		while check!= self.Password:
			check= input("Sorry, wrong Password, try again!")
			
		if check==self.Password:
			New_UserName=input("Type your new UserName:").lower()
			self.UserName=New_UserName
			print("UserName has been changed!" + self.UserName)
			print(Fore.GREEN +"\n______________________________________________________\n")	


print(Back.BLUE + "\nHello there! this is VAS, our volunteering Assistance Program! \nHere you can take a quiz regarding your personality and in return recive a volunteering place which suits your personality!\nIn addiotion, you can read inforamtion about different places to volunteer at, also, you can read stories from people who volunteered in those places!\nnote: navigating in this app  in most cases is done by writing number, have fun:)\n")
print(Fore.GREEN + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
Up= input(str("\n\nDon't have an acount? Press 1 to sign up!\n\nAlready have an acount? press 2 to sign in!\n\nTo Exit type 3!\n"))
print(Fore.GREEN + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

x=4
if Up=="1":
	UserName=(input("Create a UserName!\n\n")).lower()
	Psw=input("\nCreate a password!\n\n")
	name=input("\nwhat is your name?\n\n")
	second=input("\nwhat is your second name?\n\n")
	i=True	
	print(Fore.GREEN + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

	user= input("what is your username?\n\n")
	while user!=UserName:
		print("I don't know this UserName, try again!")
		user= input("\nwhat is your username?\n\n")
	if user==UserName:
		word= input("\nWhat is you Password?\n\n")
		print(Fore.GREEN + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

		while word!=Psw and x>0:
			print("\nWrong password, try again! you only have " + str(x) + " more tries")
			word= input("\nWhat is you Password?\n")
			x=x-1
			i=False
		if word== Psw:
			i=True
			New= User(name,second,UserName,Psw,"volunteering place is yet to be determend, Take a quiz!(:")		
elif Up=="2":	
	user= input("\nwhat is your username?\n")
	while user!=UserName:
		print("\nI don't know this UserName, try again!")
		user= input("\nwhat is your username?\n")
		print(Fore.GREEN + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

	if user==UserName:
		word= input("\nWhat is you Password?\n")
		
		while word!=Psw and x>0:
			print("\nWrong password, try again! you only have " + str(x) + " more tries" )
			word= input("\nWhat is you Password?\n")
			print(Fore.GREEN + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

			x=x-1
			i=False
		while word== Psw :
			print(Fore.GREEN + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

			i=True	
			New= User(name,second,UserName,Psw,"Volunteering Place Is Yet To Be Determined, Take A Quiz!(:",0)
elif Up=="3":
	i=False

FullName= New.name+" "+New.second
while i==True:	

	fun= input("\nWhat would you like to do now?\n1.Take A Quiz!\n2.Read About Us!\n3.Read About Places To volunteer In!\n4.Read Stories From People!\n5.Acount Managment \n6.Share a story about your volunteering experience!\n7.Add A Volunteering Place!\n8.Exit;(\n")
	
	if fun == "1":
		start=input("Hi "+ New.name + " Welcome To Our Quiz! Are You Ready?(Yes/No)\n").lower()
		if start=="yes":
			print("Lest's start!(Make sure to type the *number* of the answer!)\n")
			print(Fore.GREEN +"\n______________________________________________________\n")
			def check():
				Qsos=1
				Qmda=1
				Qsalam=1
				Qwish=1
				Qlatet= 1
				Qseeds=1
				Q1= int(input("1)Do you speak Hebrew?\n1.Yes\n2.Partly\n3.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q2= int(input("2)Do you speak Arabic?\n1.Yes\n2.Partly\n3.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q3= int(input("3)Would you like to work with pets?\n1.Yes\n2.I'm not sure\n3.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q4= int(input("4)Can you handle working under pressure?\n1.Yes\n2.I'm not sure\n3.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q5= int(input("5)Would you like to work with kids?\n1.Yes\n2.I'm not sure\n3.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q6= int(input("6)Would you like to work with your hands?\n1.Yes\n2.I'm not sure\n3.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q7= int(input("7)Can you handle witnessing difficult medical situastions?\n1.Yes\n2.I'm not sure\n3.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q8= int(input("8)Are you willing to take a course beforehand?\n1.Yes\n2.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q9= int(input("9)Would you rather work alone or with other people?\n1.Alone\n2.I don't have a prefrence\n3.Other people\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q10= int(input("10)Would you like to volunteer as a driver?\n1.Yes\n2.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				Q11= int(input("11)Would you be willing to go aboard for a period of time?\n1.Yes\n2.No\n"))
				print(Fore.GREEN +"\n______________________________________________________\n")
				if Q1== 3:
					Qmda= Qmda-10
					Qlatet= Qlatet-10
				if Q2==1: 
					Qsalam=Qsalam+1
					Qseeds=Qseeds+1
				elif Q2==3:
					Qsalam=Qsalam-1
					Qseeds=Qseeds-10
				if Q3==1:
					Qsos= Qsos+2

				elif Q3==3:
					Qsos= Qsos-10

				if Q4==1:
					Qmda=Qmda+1
				elif Q4==3:
					Qmda=Qmda-2
				if Q5==1:
					Qwish==Qwish+1
					Qseeds==Qseeds+1
				elif Q5==3:
					Qwish==Qwish-5
					Qseed=Qseeds-1
				if Q6==1:
					Qlatet=Qlatet+1
				elif Q6==3:
					Qlatet=Qlatet-1
				if Q7==1:
					Qmda==Qmda+1
					Qsalam==Qsalam+1
				elif Q7==3:
					Qmda=Qmda-5
					Qsalam=Qsalam-5
				
				if Q8==1:
					Qmda=Qmda+1
				elif Q8==2:
					Qmda=Qmda-10

				if Q9==1:
					Qsos=Qsos+1
					Qlatet=Qlatet-1
					Qsalam=Qsalam-1
					Qseeds=Qseeds-3
					Qwish=Qwish-3
					Qmda=Qmda-3
				elif Q9==3:
					Qmda=Qmda+1
					Qwish=Qwish+1
					Qsalam=Qsalam+1
					Qseeds=Qseeds+1

				if Q10==1:
					Qmda=Qmda+1
					Qsalam=Qsalam+1
				if Q11==1:
					Qseeds=Qseeds+3
				elif Q11==2:
					Qseeds=Qseeds-10

				bvalue= -1000
				bplace= "yo"
				info="_"

				if Qsos>bvalue:
					bvalue=Qsos
					bplace="SOS"
					info=SOS.about

				if Qmda>bvalue:
					bvalue=Qmda
					bplace="MDA"
					info=MDA.about
				if Qwish>bvalue:
					bvalue=Qwish
					bplace="Make A Wish"
					info=Make.about

				if Qlatet>bvalue:
					bvalue=Qlatet
					bplace="Latet"
					info=Latet.about
				if Qsalam>bvalue:
					bvalue=Qsalam
					bplace="Salametkom"
					info=Salametkom.about
				if Qseeds>bvalue:
					bvalue=Qseeds
					bplace="Seeds Of Humanity"
					info=Seeds.about

				New.VolPlace= bplace
				print("Congratulations! your volunteering place is " + bplace+"! here is some information about this place:\n\n"+Fore.GREEN +"\n______________________________________________________\n\n" + info+Fore.GREEN +"\n______________________________________________________\n" + " \nIn addition, you can go to the Stories From People tab to read a story from someone who volunteered in " + bplace+ "\n")
				print(Fore.GREEN +"\n______________________________________________________\n")
			check()

		
	elif fun=="2":

		print(Fore.GREEN +"\n______________________________________________________\n")
		print(random.choice(colors) + "\nWho are we?\nWe are a team of students from a program named Meet. Meet is a program which combines Israeli and Palestinian students in order to \nlearn Computer science and entrepreneurship.\nDuring our yearly program, we were given an assignment in which we had to find a solution to a problem that bothers us.\nWhat bothered us the most is the lack of people who volunteer around us! \nThis is why we created a website where every person who wants to volunteer but doesn't know where- \ncan find the perfect place for them to have fun and give back to their community!\n\n")
		print(Fore.GREEN +"\n______________________________________________________\n")
		print(random.choice(colors) + "\nWhat is our vision?\nWe believe that volunteering is extremelty important in every community, but is often over looked. \nWe believe that by making volunteering accessable, people would volunteer more.\nWe hope that through our website people will be able to find the place most suitable for them, \nthus making volunteering something enjoyable! Something people want to do.\n")
		print(Fore.GREEN +"\n______________________________________________________\n")
		print(random.choice(colors) + "\n\nHow does it work?\nTake a short quiz about your personality and prefrences and in result get information and a way to contact the place that suits you the most.\nIn adittion, you can read stories from people who volunteered in that place.\n")

		print(Fore.GREEN +"\n______________________________________________________\n")

	while fun=="3" and Recently_Added==True:
		which=input("\nWhich place would you like to read about?\n1.SOS\n2.Salametkom\n3.MDA\n4.Make A Wish\n5.Latet\n6.Seeds of Humanity\n7.Recently Added Places!\n8.Home Page\n")

		if which=="1":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.GREEN+ "\n" + SOS.name + "\n\n" + SOS.about + "\n\n" + SOS.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="2":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+"\n" + Salametkom.name + "\n\n" + Salametkom.about + "\n\n" +Salametkom.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="3":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.RED+"\n" + MDA.name + "\n\n"+ MDA.about +  "\n\n" + MDA.link)
			print(Fore.GREEN +"\n______________________________________________________\n")
		
		elif which=="4":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.GREEN+"\n" + Make.name + "\n\n"+ Make.about + "\n\n" + Make.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="5":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+"\n" + Latet.name + "\n\n"+ Latet.about+  "\n\n" + Latet.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="6":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.RED+ "\n" + Seeds.name + "\n\n" +Seeds.about+  "\n\n" + Seeds.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="7":
			for key,value in Places_Dict.items():
				if key>6:
					print(Fore.GREEN +"_____________________________________________________\n")
					print(value)
					print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="8":

			fun="not 3 lmao"
			print(Fore.GREEN +"\n______________________________________________________\n")

	while fun=="3":
		which=input("\nWhich place would you like to read about?\n1.SOS\n2.Salametkom\n3.MDA\n4.Make A Wish\n5.Latet\n6.Seeds of Humanity\n7.Home Page\n")

		if which=="1":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+ "\n" + SOS.name + "\n\n" + SOS.about + "\n\n" + SOS.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="2":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+"\n" + Salametkom.name + "\n\n" + Salametkom.about + "\n\n" +Salametkom.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="3":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+"\n" + MDA.name + "\n\n"+ MDA.about +  "\n\n" + MDA.link)
			print(Fore.GREEN +"\n______________________________________________________\n")
		
		elif which=="4":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+"\n" + Make.name + "\n\n"+ Make.about + "\n\n" + Make.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="5":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+"\n" + Latet.name + "\n\n"+ Latet.about+  "\n\n" + Latet.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="6":
			print(Fore.GREEN +"\n______________________________________________________\n")
			print(Back.BLUE+ "\n" + Seeds.name + "\n\n" +Seeds.about+  "\n\n" + Seeds.link)
			print(Fore.GREEN +"\n______________________________________________________\n")

		elif which=="7":

			fun="not 3 lmao"
			print(Fore.GREEN +"\n______________________________________________________\n")
	if fun=="5":
		
		print(Fore.GREEN +"\n______________________________________________________\n")
		print(Fore.RED + "\n" + "Name:" + New.name + " "+ New.second + "\n" + "UserName:" + New.UserName + "\n" +"Volunteering Place:"+ New.VolPlace + "\n" + "Password:" + len(New.Password) * "*")
		print(Fore.GREEN +"\n______________________________________________________\n")


		Change= input("\nAcount Managment\n1.Change UserName\n2.Change Password\n3.Home Page\n4.Exit\n")
		print(Fore.GREEN +"\n______________________________________________________\n")

		if Change=="1":

			New.Change_User()	

		elif Change=="2":
			New.Change_psw()
		
		elif Change=="3":
			print("")
			
		elif Change=="4":
			i=False
	while fun=="6":

		submit=input("\nWould you like to sumbit a story?\n1.yes\n2.no\n")
		if submit=="1":
			print(Fore.GREEN +"\n______________________________________________________\n")
			NewP= input("Where did you volunteer?\n")
			if str(NewP + " By- " + FullName ) in story_dict:
				print(Back.GREEN + "\nSorry! You Allready Submited A Story About This Place!")
				break
			NewS= input("Great! Share your story!\n")
			print("Thanks for sharing your story!\n")
			print(Fore.GREEN +"\n______________________________________________________\n")
			
			Dictionary_key = NewP + " By- " + FullName 
			NewStory= Stories(NewP,NewS)
			story_dict[Dictionary_key] = NewS
			fun="not 6 lmao"
			
		elif submit=="2":
			fun="not 6 lmao"

		elif submit=="2":
			print("")
	
	if fun=="4":
		
			for key,value in story_dict.items():
				print("")
				print(Fore.GREEN +"\n______________________________________________________\n")
				print(Back.RED + key +"\n\n" + value + "\n") 

				print(Fore.GREEN +"\n______________________________________________________\n")
		
	
	while fun=="7":
		print(Fore.GREEN +"\n______________________________________________________\n")
		New_Place= input("What Is The Name Of The Place?\n").lower()
		if New_Place in Places_Dict_Check.values():
			print(Back.GREEN + "\nSorry, This Place Has Already Been Submited!")
			print(Fore.GREEN + "\n______________________________________________________\n")
			break 
		New_About= input("Tell Us A Little Bit About This Place!\n")
		New_Link=input("Share a link to the place's website!(if there isn't a link type 'no')\n")
		
		

		print("Thanks you for submiting a place!\n")
		print(Fore.GREEN + "\n______________________________________________________\n")
		if New_Link.lower()=="no":

			Places_Dict[max(Places_Dict)+1]= Back.BLUE +"\n"+ New_Place + "\n\n" + New_About + "\n\n" + "Sorry, there is no link for this place!"
			Places_Dict_Check[max(Places_Dict_Check)+1]= New_Place

			Recently_Added= True

		else:
			Places_Dict[max(Places_Dict)+1]= Back.BLUE +"\n\n"+ New_Place + "\n\n" + New_About + "\n\n" + New_Link
			Places_Dict_Check[max(Places_Dict_Check)+1]= New_Place
			Recently_Added= True



		if New_Link.lower() == "no":

			New_Volplace= Places(New_Place,New_About,"Sorry, there is no link for this place!")
		else:
			New_Volplace= Places(New_Place,New_About,New_Link)
		fun="not 7 lmao"


	if fun=="8":
		i=False
	
	







	
	

			



