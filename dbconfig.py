import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred, {
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
  print("Name: "+sample[key]['Member Name'] ," ","Attendance:",sample[key]['Attendance']) #+ for string and , for int

# # input
# username_to_delete = input("Enter the name of the member to delete: ")
# data = ref.get()
# for key in sample:
#     if (username_to_delete == sample[key]['Member Name']):
#         delete_user_ref = ref.child('1-1-1').child(key) #get the ref to the specific child
#         delete_user_ref.delete() #delete the child


username_to_update = input("Enter the name of the member to update: ")
data = ref.get()
for key in sample:
    if (username_to_update == sample[key]['Member Name']):
        update_user_ref = ref.child('1-1-1').child(key) #get the ref to the specific child
        new_name = input("Enter new name: ")
        new_attendance = input("Enter new attendance (Absent(0)/Present(1)): ")
        update_user_ref.update({
            "Member Name": new_name,
            "Attendance": new_attendance
        })
        
#print the updated attendance
sample = ref.get()['1-1-1']
for key in sample: #got ittt,
  print("Name: "+sample[key]['Member Name'] ," ","Attendance:",sample[key]['Attendance']) #+ for string and , for int


