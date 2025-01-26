
contacts={}

while True:
     print("\nWelcome to  Contact Book App .")
     print("1.Create Contact ")
     print("2.View Contact ")
     print("3.Update Contact ")
     print("4.Delete Contact ")
     print("5.Search Contact ")
     print("6.Count Contact ")
     print("7.Exit  ")


     choice=input("Enter your Choice : ")
     if choice =='1':
          name=input("Enter Your name to create contact : ")
          if name in contacts:
               print(f'Contact Name : {name} already exists')
          else:
               age=input("Enter  age : ")
               email=input("Enter email  : ")  
               mobile=input("Enter mobile  : ")
               contacts[name]={'age': int(age),'email': {email}, 'mobile' : {mobile} }
               print(f'Contact Name {name} has been created successfully !!') 

     elif choice== '2':
          name=input("Enter name to view contact : ") 
          if name in contacts:
              contact=contacts[name]
              print(f'Contact name {name},age: {age}, email: {email}, mobile : {mobile}')
          else:
               print(f'Contact Name {contact} does not exist')

     elif choice== '3':
          name=input("Enter a name to update contact ")
          if name in  contacts:
               age=input("Enter  upated age : ")
               email=input("Enter updated email  : ")
               mobile=input("Enter updated mobile  : ")
               contacts[name]={f'age: {age}, mobile: {mobile}, email:{email}'}

          else:
               print(f'Contact not found')     

     elif choice =='4':
          name=input("Enter name to delete contact  ")
          if name in contacts:
               del contacts[name]
               print(f'Contact Name {name}  has been deleted successfully !!')
          else:
                    print(f'Contact Name {name} does not exist')

     elif choice== '5':
               search_name=input("Enter name to search contact ")
               found=False
               for contact,name in contacts.items():
                    if search_name.lower() in name.lower():
                         print(f'Found - Name {name}, Age:{age}, Mobile: {mobile}')
                         found=True
                    if not found:
                         print(f'Contact Name {search_name} does not exist')

     elif choice== '6':
                 print(f' Total Contact in Your Contact Book : {len(contacts)}')

     elif choice=='7':
          print("Good bye... Closing the program")    
          break                     
     else:
          print("Invalid input ")