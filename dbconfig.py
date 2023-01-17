import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("C:/Users/LENOVO/Desktop/les/firebase-sdk.json")
firebase_admin.initialize_app(cred,
{
  'databaseURL':'https://les-attendance-default-rtdb.firebaseio.com/'
})

ref = db.reference('/') #referring to root of db

# mname = str(input("Please enter member name: "))
# date = str(input("Date: "))
# Attendance = int(input("Absent(0)/Present(1): "))

# aref = ref.child(date)


# aref.push( #generates a unique key for each document and doesn't overwrite data
#   {
#       "Member Name": mname,
#       "Attendance": Attendance
#   }
# )

#sname = str(input("Enter membername: "))


a = ref.get() # to get all data
#ask user for meeting date
sample = a['1-1-1']
#print all members attendance on that date
for key in sample: #got ittt,
  print("Name:"+sample[key]['Member Name'] ," ","Attendance:",sample[key]['Attendance']) #+ for string and , for int


