from tkinter import *
from tkinter import messagebox
import requests
import json
import requests
import threading
from threading import *
import tkinter as tk
import sys
import cv2, imutils, socket
import numpy as np
import time
from PIL import Image, ImageTk
from multiprocessing import Process
import tkinter.font as tkFont
import numpy as np 
import pandas as pd
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sta=""
dis=""
statef="ii"
dist1="kk"
mon=""
mont="vv"
def predictcrop():
	ws= Tk()
	ws.title('Crop Prediction')
	ws.geometry('600x400')
	ws.config(bg='#F2B90C')
	def recomend(stat,dist,mont):
		gi = Tk()
		gi.title('Recommended Crops')
		gi.geometry("1350x700+0+0")
		gi.configure(bg='white')
		lb4 = Label(gi,text = "Your Results are here",fg= "red").place(x=425,y=10)
		lb4= ("times new roman", 100, "bold")
		import pandas as pd
		import numpy as np
		cropdt = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\sai\miniproject\crop_production.csv")
		cropdt.head()
		import pandas as pd
		import numpy as np
		spdt = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\sai\miniproject\Superdataset.csv")
		spdt.head()
		cropdt["produceperarea"]=(cropdt["Production"]/cropdt["Area"])
		cropdt.head()
		state=stat		
		district=dist.upper()
		month=mont.capitalize()
		
		season=""
		season1=""
		season2=""
		season4=""
		if(month=="January" or month=="December" or month=="November" or month=="February" or month=="March"):
		  season='Rabi       '
		if(month=="October" or month=="November"):
		   season1='Autumn     '
		if(month=="June" or month=="July" or month=="August" or month=="September"):
		   season2='Kharif     '
		if(month=="March" or month=="April" or month=="May"):	
		   season4='Summer     '
		season3='Whole Year '
		a=cropdt.loc[(cropdt['State_Name']==state)&(cropdt['District_Name']==district)&((cropdt['Season']==season)|(cropdt['Season']==season1)|(cropdt	['Season']==season2)|(cropdt['Season']==season4))]
		#print(a)
		wy=cropdt.loc[(cropdt['State_Name']==state)&(cropdt['District_Name']==district)&(cropdt['Season']==season3)]
		#print(wy)
		a=a.sort_values(by ="produceperarea")
		x1=a["produceperarea"].max()
		y=a.loc[(a["produceperarea"]==x1)]
		z=y["Crop"].values
		print(z)
		x2=wy["Production"].max()
		#z2=a["produceperarea"].max
		y1=wy.loc[(wy["Production"]==x2)]
		z1=y1["Crop"].values
		z1
		print(z1)

		import pandas as pd
		import numpy as np
		soildt = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\sai\miniproject\Crop_recommendation.csv")
		soildt.head()

		"""state="West Bengal"
		district="PURULIA"
		i"""

		cropdt["Season"].unique()
		print("The following crop could be sown  according to your input month for better results:",z)
		
		lb22 = Label(gi,text = "In "+str(district)+"  district"+" in "+str(state)+"  state",fg= "black").place(x=425,y=25)
		lb22= ("times new roman", 10000, "bold")
		lb5 = Label(gi,text = "The following crops could be sown  according to your input month:"+str(month)+" is  :"+str(z),fg= "black").place(x=425,y=50)
		lb5= ("times new roman", 10000, "bold")
		#lb6 = Label(gi,text ="The Highly recommended crop for all the seasons throughout the year is :"+str(z1),fg= "black").place(x=425,y=100)
		#lb6= ("times new roman", 10000, "bold")
		print("The Highly recommended crop for all the seasons is :",z1)
		print("This crop can give good produce throughout the year\n")
		avgt=spdt["Temp"].mean()
		lb7 = Label(gi,text ="The best produce can be expected if the Temperature is around :"+str(avgt),fg= "black").place(x=425,y=100)
		lb7= ("times new roman",10000, "bold")
		print("The best produce can be expected if the Temperature is :",avgt)
		#cumtr=spdt["Annual_rainfall"].mean()
		#print("The best produce can be expected if the Rainfall is around :",cumtr)
		soilph=soildt["ph"].mean()
		lb9 = Label(gi,text ="The produce will be more if the ph of the soil is around : "+str(soilph),fg= "black").place(x=425,y=150)
		lb9= ("times new roman", 10000, "bold")
		print("The produce will be more if the ph of the soil is : ",soilph)
		hmdt=soildt["humidity"].mean()
		lb10 = Label(gi,text ="The  best produce can  be expected if the humidity of the soil is around: "+str(hmdt),fg= "black").place(x=425,y=200)
		lb10= ("times new roman", 10000, "bold")
		print("The  best produce can  be expected if the humidity of the soil is : ",hmdt)
		raindt=soildt["rainfall"].mean()
		lb8 = Label(gi,text ="The best produce can be expected if the Rainfall is :"+str(raindt)+" cm",fg= "black").place(x=425,y=250)
		lb8= ("times new roman", 10000, "bold")
		
		print("The  best produce can  be expected if the rainfall of the region is : ",raindt)
	def distf(stats):
		global statef
		statef=stats
		if(statef=='Andaman and Nicobar Islands'):
			districts=['NICOBARS', 'NORTH AND MIDDLE ANDAMAN', 'SOUTH ANDAMANS']
		elif(statef=='Andhra Pradesh'):
			districts=['ANANTAPUR', 'CHITTOOR', 'EAST GODAVARI', 'GUNTUR', 'KADAPA','KRISHNA', 'KURNOOL', 'PRAKASAM', 'SPSR NELLORE','SRIKAKULAM',
				'VISAKHAPATANAM', 'VIZIANAGARAM', 'WEST GODAVARI']
		elif(statef== 'Arunachal Pradesh'):
			districts=['ANJAW', 'CHANGLANG', 'DIBANG VALLEY', 'EAST KAMENG', 'EAST SIANG','KURUNG KUMEY', 'LOHIT', 'LONGDING', 'LOWER DIBANG VALLEY',
				'LOWER SUBANSIRI', 'NAMSAI', 'PAPUM PARE', 'TAWANG', 'TIRAP',
				'UPPER SIANG', 'UPPER SUBANSIRI', 'WEST KAMENG', 'WEST SIANG']
		elif(statef== 'Assam'):
			districts=['BAKSA', 'BARPETA', 'BONGAIGAON', 'CACHAR', 'CHIRANG', 'DARRANG',
       'DHEMAJI', 'DHUBRI', 'DIBRUGARH', 'DIMA HASAO', 'GOALPARA',
       'GOLAGHAT', 'HAILAKANDI', 'JORHAT', 'KAMRUP', 'KAMRUP METRO',
       'KARBI ANGLONG', 'KARIMGANJ', 'KOKRAJHAR', 'LAKHIMPUR', 'MARIGAON',
       'NAGAON', 'NALBARI', 'SIVASAGAR', 'SONITPUR', 'TINSUKIA',
       'UDALGURI']
		elif(statef== 'Bihar'):
			districts=['ARARIA', 'ARWAL', 'AURANGABAD', 'BANKA', 'BEGUSARAI', 'BHAGALPUR',
       'BHOJPUR', 'BUXAR', 'DARBHANGA', 'GAYA', 'GOPALGANJ', 'JAMUI',
       'JEHANABAD', 'KAIMUR (BHABUA)', 'KATIHAR', 'KHAGARIA',
       'KISHANGANJ', 'LAKHISARAI', 'MADHEPURA', 'MADHUBANI', 'MUNGER',
       'MUZAFFARPUR', 'NALANDA', 'NAWADA', 'PASHCHIM CHAMPARAN', 'PATNA',
       'PURBI CHAMPARAN', 'PURNIA', 'ROHTAS', 'SAHARSA', 'SAMASTIPUR',
       'SARAN', 'SHEIKHPURA', 'SHEOHAR', 'SITAMARHI', 'SIWAN', 'SUPAUL',
       'VAISHALI']
		elif(statef== 'Chandigarh'):
			districts=['CHANDIGARH']
		elif(statef== 'Dadra and Nagar Haveli'):
			districts=['DADRA AND NAGAR HAVELI']
		elif(statef== 'Goa'):
			districts=['NORTH GOA', 'SOUTH GOA']
		elif(statef== 'Gujarat'):
			districts=['AHMADABAD', 'AMRELI', 'ANAND', 'BANAS KANTHA', 'BHARUCH',
       'BHAVNAGAR', 'DANG', 'DOHAD', 'GANDHINAGAR', 'JAMNAGAR',
       'JUNAGADH', 'KACHCHH', 'KHEDA', 'MAHESANA', 'NARMADA', 'NAVSARI',
       'PANCH MAHALS', 'PATAN', 'PORBANDAR', 'RAJKOT', 'SABAR KANTHA',
       'SURAT', 'SURENDRANAGAR', 'TAPI', 'VADODARA', 'VALSAD']
		elif(statef== 'Haryana'):
			districts=['AMBALA', 'BHIWANI', 'FARIDABAD', 'FATEHABAD', 'GURGAON', 'HISAR',
       'JHAJJAR', 'JIND', 'KAITHAL', 'KARNAL', 'KURUKSHETRA',
       'MAHENDRAGARH', 'MEWAT', 'PALWAL', 'PANCHKULA', 'PANIPAT',
       'REWARI', 'ROHTAK', 'SIRSA', 'SONIPAT', 'YAMUNANAGAR']
		elif(statef== 'Himachal Pradesh'):
			districts=['BILASPUR', 'CHAMBA', 'HAMIRPUR', 'KANGRA', 'KINNAUR', 'KULLU',
       'LAHUL AND SPITI', 'MANDI', 'SHIMLA', 'SIRMAUR', 'SOLAN', 'UNA']
		elif(statef== 'Jammu and Kashmir '):
			districts=['ANANTNAG', 'BADGAM', 'BANDIPORA', 'BARAMULLA', 'DODA',
       'GANDERBAL', 'JAMMU', 'KARGIL', 'KATHUA', 'KISHTWAR', 'KULGAM',
       'KUPWARA', 'LEH LADAKH', 'POONCH', 'PULWAMA', 'RAJAURI', 'RAMBAN',
       'REASI', 'SAMBA', 'SHOPIAN', 'SRINAGAR', 'UDHAMPUR']
		elif(statef== 'Jharkhand '):
			districts=['BOKARO', 'CHATRA', 'DEOGHAR', 'DHANBAD', 'DUMKA', 'EAST SINGHBUM',
       'GARHWA', 'GIRIDIH', 'GODDA', 'GUMLA', 'HAZARIBAGH', 'JAMTARA',
       'KHUNTI', 'KODERMA', 'LATEHAR', 'LOHARDAGA', 'PAKUR', 'PALAMU',
       'RAMGARH', 'RANCHI', 'SAHEBGANJ', 'SARAIKELA KHARSAWAN', 'SIMDEGA',
       'WEST SINGHBHUM']
		elif(statef== 'Karnataka'):
			districts=['BAGALKOT', 'BANGALORE RURAL', 'BELGAUM', 'BELLARY',
       'BENGALURU URBAN', 'BIDAR', 'BIJAPUR', 'CHAMARAJANAGAR',
       'CHIKBALLAPUR', 'CHIKMAGALUR', 'CHITRADURGA', 'DAKSHIN KANNAD',
       'DAVANGERE', 'DHARWAD', 'GADAG', 'GULBARGA', 'HASSAN', 'HAVERI',
       'KODAGU', 'KOLAR', 'KOPPAL', 'MANDYA', 'MYSORE', 'RAICHUR',
       'RAMANAGARA', 'SHIMOGA', 'TUMKUR', 'UDUPI', 'UTTAR KANNAD',
       'YADGIR']
		elif(statef== 'Kerala'):
			districts=['ALAPPUZHA', 'ERNAKULAM', 'IDUKKI', 'KANNUR', 'KASARAGOD',
       'KOLLAM', 'KOTTAYAM', 'KOZHIKODE', 'MALAPPURAM', 'PALAKKAD',
       'PATHANAMTHITTA', 'THIRUVANANTHAPURAM', 'THRISSUR', 'WAYANAD']
		elif(statef== 'Madhya Pradesh'):
			districts=['AGAR MALWA', 'ALIRAJPUR', 'ANUPPUR', 'ASHOKNAGAR', 'BALAGHAT',
       'BARWANI', 'BETUL', 'BHIND', 'BHOPAL', 'BURHANPUR', 'CHHATARPUR',
       'CHHINDWARA', 'DAMOH', 'DATIA', 'DEWAS', 'DHAR', 'DINDORI', 'GUNA',
       'GWALIOR', 'HARDA', 'HOSHANGABAD', 'INDORE', 'JABALPUR', 'JHABUA',
       'KATNI', 'KHANDWA', 'KHARGONE', 'MANDLA', 'MANDSAUR', 'MORENA',
       'NARSINGHPUR', 'NEEMUCH', 'PANNA', 'RAISEN', 'RAJGARH', 'RATLAM',
       'REWA', 'SAGAR', 'SATNA', 'SEHORE', 'SEONI', 'SHAHDOL', 'SHAJAPUR',
       'SHEOPUR', 'SHIVPURI', 'SIDHI', 'SINGRAULI', 'TIKAMGARH', 'UJJAIN',
       'UMARIA', 'VIDISHA']
		elif(statef== 'Maharashtra'):
			districts=['AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED',
       'BHANDARA', 'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI',
       'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR',
       'MUMBAI', 'NAGPUR', 'NANDED', 'NANDURBAR', 'NASHIK', 'OSMANABAD',
       'PALGHAR', 'PARBHANI', 'PUNE', 'RAIGAD', 'RATNAGIRI', 'SANGLI',
       'SATARA', 'SINDHUDURG', 'SOLAPUR', 'THANE', 'WARDHA', 'WASHIM',
       'YAVATMAL']
		
		elif(statef== 'Manipur'):
			districts=['BISHNUPUR', 'CHANDEL', 'CHURACHANDPUR', 'IMPHAL EAST',
       'IMPHAL WEST', 'SENAPATI', 'TAMENGLONG', 'THOUBAL', 'UKHRUL']
		elif(statef== 'Meghalaya'):
			districts=['EAST GARO HILLS', 'EAST JAINTIA HILLS', 'EAST KHASI HILLS',
       'NORTH GARO HILLS', 'RI BHOI', 'SOUTH GARO HILLS',
       'SOUTH WEST GARO HILLS', 'SOUTH WEST KHASI HILLS',
       'WEST GARO HILLS', 'WEST JAINTIA HILLS', 'WEST KHASI HILLS']
		elif(statef== 'Mizoram'):
			districts=['AIZAWL', 'CHAMPHAI', 'KOLASIB', 'LAWNGTLAI', 'LUNGLEI', 'MAMIT',
       'SAIHA', 'SERCHHIP']
		elif(statef== 'Nagaland'):
			districts=['DIMAPUR', 'KIPHIRE', 'KOHIMA', 'LONGLENG', 'MOKOKCHUNG', 'MON',
       'PEREN', 'PHEK', 'TUENSANG', 'WOKHA', 'ZUNHEBOTO']
		elif(statef== 'Odisha'):
			districts=['ANUGUL', 'BALANGIR', 'BALESHWAR', 'BARGARH', 'BHADRAK', 'BOUDH',
       'CUTTACK', 'DEOGARH', 'DHENKANAL', 'GAJAPATI', 'GANJAM',
       'JAGATSINGHAPUR', 'JAJAPUR', 'JHARSUGUDA', 'KALAHANDI',
       'KANDHAMAL', 'KENDRAPARA', 'KENDUJHAR', 'KHORDHA', 'KORAPUT',
       'MALKANGIRI', 'MAYURBHANJ', 'NABARANGPUR', 'NAYAGARH', 'NUAPADA',
       'PURI', 'RAYAGADA', 'SAMBALPUR', 'SONEPUR', 'SUNDARGARH']
		elif(statef== 'Puducherry'):
			districts=['KARAIKAL', 'MAHE', 'PONDICHERRY', 'YANAM']
		elif(statef== 'Punjab'):
			districts=['AMRITSAR', 'BARNALA', 'BATHINDA', 'FARIDKOT', 'FATEHGARH SAHIB',
       'FAZILKA', 'FIROZEPUR', 'GURDASPUR', 'HOSHIARPUR', 'JALANDHAR',
       'KAPURTHALA', 'LUDHIANA', 'MANSA', 'MOGA', 'MUKTSAR', 'NAWANSHAHR',
       'PATHANKOT', 'PATIALA', 'RUPNAGAR', 'S.A.S NAGAR', 'SANGRUR',
       'TARN TARAN']
		elif(statef== 'Rajasthan'):
			districts=['AJMER', 'ALWAR', 'BANSWARA', 'BARAN', 'BARMER', 'BHARATPUR',
       'BHILWARA', 'BIKANER', 'BUNDI', 'CHITTORGARH', 'CHURU', 'DAUSA',
       'DHOLPUR', 'DUNGARPUR', 'GANGANAGAR', 'HANUMANGARH', 'JAIPUR',
       'JAISALMER', 'JALORE', 'JHALAWAR', 'JHUNJHUNU', 'JODHPUR',
       'KARAULI', 'KOTA', 'NAGAUR', 'PALI', 'PRATAPGARH', 'RAJSAMAND',
       'SAWAI MADHOPUR', 'SIKAR', 'SIROHI', 'TONK', 'UDAIPUR']
		elif(statef== 'Sikkim'):
			districts=['EAST DISTRICT', 'NORTH DISTRICT', 'SOUTH DISTRICT',
       'WEST DISTRICT']
		elif(statef== 'Tamil Nadu'):
			districts=['ARIYALUR', 'COIMBATORE', 'CUDDALORE', 'DHARMAPURI', 'DINDIGUL',
       'ERODE', 'KANCHIPURAM', 'KANNIYAKUMARI', 'KARUR', 'KRISHNAGIRI',
       'MADURAI', 'NAGAPATTINAM', 'NAMAKKAL', 'PERAMBALUR', 'PUDUKKOTTAI',
       'RAMANATHAPURAM', 'SALEM', 'SIVAGANGA', 'THANJAVUR',
       'THE NILGIRIS', 'THENI', 'THIRUVALLUR', 'THIRUVARUR',
       'TIRUCHIRAPPALLI', 'TIRUNELVELI', 'TIRUPPUR', 'TIRUVANNAMALAI',
       'TUTICORIN', 'VELLORE', 'VILLUPURAM', 'VIRUDHUNAGAR']
		elif(statef== 'Telangana '):
			districts=['ADILABAD', 'HYDERABAD', 'KARIMNAGAR', 'KHAMMAM', 'MAHBUBNAGAR',
       'MEDAK', 'NALGONDA', 'NIZAMABAD', 'RANGAREDDI', 'WARANGAL']
		elif(statef== 'Tripura'):
			districts=['DHALAI', 'GOMATI', 'KHOWAI', 'NORTH TRIPURA', 'SEPAHIJALA',
       'SOUTH TRIPURA', 'UNAKOTI', 'WEST TRIPURA']
		elif(statef== 'Uttar Pradesh'):
			districts=['AGRA', 'ALIGARH', 'ALLAHABAD', 'AMBEDKAR NAGAR', 'AMETHI',
       'AMROHA', 'AURAIYA', 'AZAMGARH', 'BAGHPAT', 'BAHRAICH', 'BALLIA',
       'BALRAMPUR', 'BANDA', 'BARABANKI', 'BAREILLY', 'BASTI', 'BIJNOR',
       'BUDAUN', 'BULANDSHAHR', 'CHANDAULI', 'CHITRAKOOT', 'DEORIA',
       'ETAH', 'ETAWAH', 'FAIZABAD', 'FARRUKHABAD', 'FATEHPUR',
       'FIROZABAD', 'GAUTAM BUDDHA NAGAR', 'GHAZIABAD', 'GHAZIPUR',
       'GONDA', 'GORAKHPUR', 'HAMIRPUR', 'HAPUR', 'HARDOI', 'HATHRAS',
       'JALAUN', 'JAUNPUR', 'JHANSI', 'KANNAUJ', 'KANPUR DEHAT',
       'KANPUR NAGAR', 'KASGANJ', 'KAUSHAMBI', 'KHERI', 'KUSHI NAGAR',
       'LALITPUR', 'LUCKNOW', 'MAHARAJGANJ', 'MAHOBA', 'MAINPURI',
       'MATHURA', 'MAU', 'MEERUT', 'MIRZAPUR', 'MORADABAD',
       'MUZAFFARNAGAR', 'PILIBHIT', 'PRATAPGARH', 'RAE BARELI', 'RAMPUR',
       'SAHARANPUR', 'SAMBHAL', 'SANT KABEER NAGAR', 'SANT RAVIDAS NAGAR',
       'SHAHJAHANPUR', 'SHAMLI', 'SHRAVASTI', 'SIDDHARTH NAGAR',
       'SITAPUR', 'SONBHADRA', 'SULTANPUR', 'UNNAO', 'VARANASI']
		elif(statef== 'Uttarakhand'):
			districts=['ALMORA', 'BAGESHWAR', 'CHAMOLI', 'CHAMPAWAT', 'DEHRADUN',
       'HARIDWAR', 'NAINITAL', 'PAURI GARHWAL', 'PITHORAGARH',
       'RUDRA PRAYAG', 'TEHRI GARHWAL', 'UDAM SINGH NAGAR', 'UTTAR KASHI']
		elif(statef== 'West Bengal'):
			districts=['24 PARAGANAS NORTH', '24 PARAGANAS SOUTH', 'BANKURA', 'BARDHAMAN',
       'BIRBHUM', 'COOCHBEHAR', 'DARJEELING', 'DINAJPUR DAKSHIN',
       'DINAJPUR UTTAR', 'HOOGHLY', 'HOWRAH', 'JALPAIGURI', 'MALDAH',
       'MEDINIPUR EAST', 'MEDINIPUR WEST', 'MURSHIDABAD', 'NADIA',
       'PURULIA']
		def display_selected1(choice):
			choice = variable.get()
			#print(choice)
			global dist1
			dist1=choice
			print(dist1)
			#data(statef,dist1)
		lab1= Label(ws, text= "Select  month", font= ("", 10))
		lab1.pack(pady=30)
		variable = StringVar()
		variable.set("select District")
		dropdown = OptionMenu(ws,variable,*districts,command=display_selected1)
		dropdown.pack(expand=True,pady=60)
		dropdown.place(x=300,y=150)
	def display_selected(choice):
		choice = variable.get()
		#print(choice)
		stats=choice
		print(stats)
		distf(stats)
	states = ['Andaman and Nicobar Islands', 'Andhra Pradesh',
       'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
       'Chhattisgarh', 'Dadra and Nagar Haveli', 'Goa', 'Gujarat',
       'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir ', 'Jharkhand',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
       'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana ',
       'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
	lab= Label(ws, text= "Select state", font= ("", 10))
	lab.pack(pady=30)
	variable = StringVar()
	variable.set("select state")
	dropdown = OptionMenu(ws,variable,*states,command=display_selected)
	dropdown.pack(expand=True,pady=60)
	dropdown.place(x=300,y=60)
	def display_selected2(choice):
		choice = variable1.get()
		#print(choice)
		global mont
		mont=choice
		print(mont)
		rec(mont)
	months=['January','February','March','April','May','June','July','August','September','October','November','December']
	lab2= Label(ws, text= "Select District", font= ("", 10))
	lab2.pack(pady=30)
	variable1 = StringVar()
	#variable.set("select Month")
	dropdown = OptionMenu(ws,variable1,*months,command=display_selected2)
	dropdown.pack(expand=True,pady=60)
	dropdown.place(x=300,y=240)
	def monthdt(mon3):
		mnt4=mon3
	#def data(statef,dist1):
		#monthname=mont
		#rec(statename,distname,monthname)
	def rec(mont2):
		statename=statef
		distname=dist1
		monthname=mont2
		recomend(statename,distname,monthname)
		print('**',statename,distname,monthname)
	ws.mainloop()	
	
	
	

	
	
gui = Tk()
gui.title('Crop Recommendation')
gui.geometry("1350x700+0+0")
gui.configure(bg='black')
bg = PhotoImage(file = "wa.png")
label1 = Label(gui, image = bg,height=70000,width=70000)
label1.place(x = 0,y = 0)
label1.pack()
lbl = Label(gui,text = "which crop to grow?",fg= "red").place(x=425,y=10)
lbl= ("times new roman", 100, "bold")
bt = Button(gui,text="predict crop",command=predictcrop,font=("times new roman", 15, "bold"),activeforeground = "red",activebackground = "pink",pady=10,height=3, width=10)    
bt.place(x=425,y=120)
gui.mainloop()