#! /usr/bin/env python3


from gw2api import GuildWars2Client
#import GuildWars2Client
import time

global MAX_GOAL
MAX_GOAL=100


class gwClient:
	"""
	A class to fetch achievment information for Guildwars 2

	@Attributes
		client : GuildWars2Client
			GuildWars2Client API Class - external 
		current: int 
			Save the current vlaue status for the desired achievment
		counter: int
			TODO
		achievment_list: list
			Fetch all achievments IDs into the list
		achievmentName: str
			Filter the Name of the achievment with the IDs
		selected_achievment: str
			Save the current vlaue status for the desired achievment
	"""
	client=GuildWars2Client
	current=-1
	counter=0
	achievment_list=""
	achievmentName=""
	selected_achievment=""
	initValue=0
	def __init__(self,clientGoal,APIKey,username):
		self.clientGoal=clientGoal
		self.APIKey=APIKey
		self.username=username
	def APIConnect(self):
		self.client = GuildWars2Client(api_key=self.APIKey)
	def setAchvievmentYakslapper(self):
		#id=0 fetch all achievemnts from useraccount; api required
		self.achievment_list=self.client.accountachievements.get(id=0)
		for i in self.achievment_list:
			# client.achievements.get(id=288) 
			#id 288== Yakslapper
			if(i['id']==288):
				self.selected_achievment=i
				self.name_selected_achievment=self.client.achievements.get(id=288)
				self.achievmentName=self.name_selected_achievment['name']
				self.current=self.selected_achievment['current']
				self.clientGoal=self.current+self.clientGoal
	def setInitialValue(self):
		self.achievment_list=self.client.accountachievements.get(id=0)
		for i in self.achievment_list:
			# client.achievements.get(id=288) 
			#id 288== Yakslapper
			if(i['id']==288):
				self.selected_achievment=i
				self.name_selected_achievment=self.client.achievements.get(id=288)
				self.initValue=self.selected_achievment['current']
	def getvars(self):
		print(self.username)
		print("Achievmentname is %s" %(self.achievmentName))
		print("selected Achievmentname is %s" %(self.selected_achievment))
		print("Current Value is %s" %(self.current))
		print("Desired value is %s" %(self.clientGoal))

#def menu():

def calculon(clients):
	achievmentCounter=0
	notCompleted=1
	TESTVAL=800
	while(notCompleted):

		for client in clients:
			client.setAchvievmentYakslapper()
			#overview
			print("User %s: current stats for achievment %s (id: %d) are %d" %  (client.username, client.name_selected_achievment['name'],int(client.name_selected_achievment['id']),int(client.current)) )
			
			#debugging
			#or client in clients:
			#print("User %s: current stats for achievment %s (id: %d) are %d" %  (client.username, client.name_selected_achievment['name'],int(client.name_selected_achievment['id']),int(client.current)) )
			#if(client.initValue<TESTVAL):
			
			#check the clientX.current value is incremented
			#if the value incremented add +1 to counter counter
			if(client.initValue+achievmentCounter<client.current):
				achievmentCounter=achievmentCounter+1
			if(achievmentCounter>=MAX_GOAL):
				print("Mission Completed")
				notCompleted=0
			TESTVAL=TESTVAL+20
			client.setAchvievmentYakslapper()
		print("current status is: %d"% (achievmentCounter) )
		time.sleep(10)	
# F4D84FF4-CB06-EA46-8547-B9BD3459B93F618E5D07-0F20-48A4-A525-AA41CB029463
# E53C7004-62EA-FA44-9B8D-BCBA01EB7A13C3BEEDEF-54F9-4E5F-B2E0-6DFA2F64B711

def menu():

	#lists for class gwClient
	clients=[]
	while(True):
		choice ='0'
		while choice =='0':
			print("Main Choice: Choose 1 of 5 choices")
			print("1. Connect new API Key")
			print("2. show connected API Keys")
			print("3. disconnect API Key")
			print("4. show stats ")
			print("5. Choose 5 to go to another menu")
			print("6. run achievment picker")

			choice = input ("Please make a choice: ")

			if choice == "5":
				print("Go to another menu")
				#second_menu()
			elif choice == "6":
				calculon(clients)
			elif choice == "4":
				print("4. show stats")
				for client in clients:
					client.setAchvievmentYakslapper()
					print("User %s: current stats for achievment %s (id: %d) are %d" %  (client.username, client.name_selected_achievment['name'],int(client.name_selected_achievment['id']),int(client.current)) )
					counter=0
			elif choice == "3":
				counter=0
				print("3. disconnect API Key")
				#TODO disconnect ; remove API key from list
				for client in clients:
					print("[%d] %s" % (counter,client.username))
					print("under construction :> \n")
					counter=counter+1
				#menuRemoveAPIKey = int(input ("Insert APIKEY to remove APIKEY: "))
				#int(menuRemoveAPIKey)
				#clients.remove(client[menuRemoveAPIKey])
			elif choice == "2":
				print("2. show connected API Keys")
				for client in clients:
					print (client.client.api_key)
					print()		
			elif choice == "1":
				print("Connect new API Key")
				
				#menuInputAPIKey = input ("Insert API Key: ")
				#menuInputUserName = input ("Insert Username : ")
				#debugging
				clients.append( gwClient ( 1,'F4D84FF4-CB06-EA46-8547-B9BD3459B93F618E5D07-0F20-48A4-A525-AA41CB029463','david') )
				clients.append( gwClient ( 1,'E53C7004-62EA-FA44-9B8D-BCBA01EB7A13C3BEEDEF-54F9-4E5F-B2E0-6DFA2F64B711','ivan') )
				#debugging
				#clients.append( gwClient(MAX_GOAL,menuInputAPIKey,menuInputUserName) )
				for client in clients:
					client.APIConnect()
					client.setAchvievmentYakslapper()
					client.setInitialValue()
				#clients[classIterator]=gwClient(MAX_GOAL,menuInputAPIKey,menuInputUserName)

			else:
				print("I don't understand your choice.")

def main():

	#start menu
	menu()
	##############################################################################################################################
	#TESTS																														 #
	# F4D84FF4-CB06-EA46-8547-B9BD3459B93F618E5D07-0F20-48A4-A525-AA41CB029463													 #
	# E53C7004-62EA-FA44-9B8D-BCBA01EB7A13C3BEEDEF-54F9-4E5F-B2E0-6DFA2F64B711													 #
	#TODO MENU 																													 #
	#TODO ADD/REMOVE/SHOW API Keys																								 #
	#client1=gwClient(MAX_GOAL,'F4D84FF4-CB06-EA46-8547-B9BD3459B93F618E5D07-0F20-48A4-A525-AA41CB029463','david')				 #
	#client2=gwClient(MAX_GOAL,'E53C7004-62EA-FA44-9B8D-BCBA01EB7A13C3BEEDEF-54F9-4E5F-B2E0-6DFA2F64B711','ivan')				 #
	#client4=gwClient(MAX_GOAL,'F4D84FF4-CB06-EA46-8547-B9BD3459B93F618E5D07-0F20-48A4-A525-AA41CB029463')						 #
	#client3=gwClient(MAX_GOAL,'F4D84FF4-CB06-EA46-8547-B9BD3459B93F618E5D07-0F20-48A4-A525-AA41CB029463')						 #
	#client1.APIConnect()	#client1.client.guildsearch.get(name='Mythical Realms')												 #
	#client1.setAchvievmentYakslapper()																							 #
	#client2.APIConnect()																										 #	
	#client2.client.guildsearch.get(name="Licht des Nordens")																	 #
	#client2.client.guildsearch.get(name='Mythical Realms')																		 #
	#client2.setAchvievmentYakslapper()																							 #
	#client1.getvars()																											 #
	#client2.getvars()																											 #
	#getAchvievmentYakslapper(client1)																							 #
	##############################################################################################################################
if __name__ == "__main__":
	main()