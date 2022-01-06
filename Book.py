import datetime  #importing date and time
class library:             #start of class
    #Inserting book name, price, author name and quantity in list
    global time
    time = datetime.datetime.now() 
    global name
    global author
    global price
    global quantity
    name = []
    author = []
    price = []
    quantity = []


    #when user borrow
    def borrowing():
        
        fnam= input("\nEnter the borrower first name: ")
        lnam= input("Enter the borrower last name: ")
        temp = 0
        
        #opening/making file name after username
        t = open(fnam+lnam+"_bor.txt", "a")
        t.write("\nTime: "+str(time)+"\nBorrower Name: "+fnam+" "+lnam)
        
        print("\nThe available books are: ")
        #printing all available book in stock
        for i in range(len(name)):
            print(i,name[i])
            
        #starting loop until someone complete their borrowing task
        while True:
            #trying to catch any error inside
            try: 
                bor = int(input("\nEnter the book number: "))
                #checking if given value is positive or not
                if bor>=0:
                    #checking if book is in stock or not
                    if (int(quantity[bor])>0):
                        
                        t.write("\nBook name: "+name[bor])    #recording borrowed book in file
                        temp = float(float(price[bor])+temp)  #total price
                        quantity[bor] = quantity[bor]-1    #reducing quantity of book from stock
                        
                        #creating file of borrower which contains book and price
                        m=open(fnam+lnam+"price.txt", "a")
                        m.write(name[bor]+":"+price[bor]+"\n")
                        m.close()
                        
                        print(fnam,lnam,"has successfully borrowed",name[bor])
                        
                        #starting loop to ask if they want to borrow more book or not
                        while True:
                            again = input("\nWould you like to borrow another book?(Yes or No) :")
                            if again.lower() == "yes":                     #if they want to borrow again
                                break
                            elif again.lower() == "no":                    #if they don't want to borrow again
                                t.write("\nTotal Price: "+str(temp)+"\n----------------------------------------------------\n")
                                t.close()
                                break
                            else:                                          #if they used wrong command
                                print("PLease type Yes or No")

                        #Breaking loop if user didn't wanted to borrow any more books        
                        if again.lower()=="no":
                            break

                    #if book was not in stock
                    else:
                        print("Book is not in stock")

                #if user gave negative number
                else:
                    print("Please enter the positive number.")
                    
            #if any error occurs
            except:
                print("\nPlease type correct number.")

        #updating stock after they borrow
        o=open("stock.txt","w")
        for i in range(len(name)):
            o.write(name[i]+","+author[i]+","+str(quantity[i])+","+str(price[i])+"\n")

    #if user wants to check stock
    def stock():
        print("The available books are:")
        #printing all book and their quantity
        for i in range(len(name)):
            print(name[i]+":  "+str(quantity[i]))
            
    #wgen user wants to return
    def ret():
        bname=[]
        bprice=[]
        bp=0
        pen=''
        test = 0
        #asking for returner name
        firstnam= input("\nEnter the returner first name: ")
        lastnam= input("Enter the returner last name: ")
        file=(firstnam+lastnam+"_ret.txt")           #creating borrower file name

        try:                                    #trying to catch any error inside
            #opening borrower price log to search for borrowed book and price
            p=open(firstnam+lastnam+"price.txt")
            temp = p.readlines()
            p.close()
            #recording all borrowed book and price in list
            temp=[x.strip('\n') for x in temp]
            for line in temp:
                currentline = line.split(":")
                bname.append(currentline[0])
                bprice.append(currentline[1])

            #starting loop until borrower complete the transaction
            while True:
                
                #checking if file is emtpy or not
                if len(bname):
                    print("\nWhich book would you like to return?")
                    #listing all borrowed books
                    for i in range(len(bname)):
                        print(i,bname[i])
                        
                    #asking for book number to return
                    ret=int(input("\nEnter the number: "))
                    
                    try:                                #to catch any error inside

                        #checking if given value is positive or negative
                        if ret>=0:
                            bp = float(float(bprice[ret])+bp)   #calculating price of book
                            
                            #increasing qunatity of book from stock
                            for i in range(len(name)):
                                if(name[i]==bname[ret]):
                                    quantity[i]=quantity[i]+1
                                    break
                            #checking if borrower name and time is already recorded or not
                            if(test==0): #if it is not recorded
                                t = open(firstnam+lastnam+"_ret.txt", "a")
                                t.write("\nTime: "+str(time)+"\nReturner Name: "+firstnam+" "+lastnam)
                                test=1
                            #inserting book name in returner file
                            t.write("\nBook name: "+bname[ret])
                            #removing borrowed book nd price
                            bname.remove(bname[ret])
                            bprice.remove(bprice[ret])

                            #Starting loop to ask if user wants to return more book or not
                            while True:
                                more=input("\nWould you like to return more? [Y/N]: ")
                                if more.lower()=='y': #if they say yes
                                    if not len(bname): #if there are no books they can return
                                        print("\nAll book has been returned.")
                                        more='n'
                                    break
                                elif more.lower()=='n': #if they say no
                                    break
                                else:  #if they used wrong command
                                    print("Please enter either Y or N.")
                                    
                            #if they did not want to return more book/have more books        
                            if more.lower()=='n':
                                #starting loop to ask if there is any penalty or not 
                                while True:
                                    pen= input("\nIs there any penalty? [Y/N]:")
                                    if pen.lower() == 'y':  #if there is penalty
                                        bp=bp+2
                                        print("\nYour total price is "+str(bp)+"\n")
                                        t.write("\nTotal Price: "+str(bp)+"\n----------------------------------------------------\n")
                                        t.close()
                                        break
                                    elif pen.lower()=='n':  #if there is no penalty
                                        print("\nYour total price is "+str(bp)+"\n")
                                        t.write("\nTotal Price: "+str(bp)+"\n----------------------------------------------------\n")
                                        t.close()
                                        break
                                    else:   #if user give wrong command
                                        print("\nPlease enter either Y or N.")

                            #breaking loop after price is printed
                            if pen.lower() == 'y' or pen.lower()== 'n':
                                break

                        #if user give negative number
                        else:
                            print("Please enter positive number.")

                    #if user give wrong value
                    except IndexError:
                        print("Please enter the correct number.")    
                    
                #if there is no data in returner file        
                else:
                    print("\n"+firstnam+" has not borrowed any book.")
                    break

            #updating 
            o=open("stock.txt","w")
            f=open(firstnam+lastnam+"price.txt","w")
            #for borrower file
            if len(bname):
                for i in range(len(bname)):
                    f.write(bname[i]+":"+bprice[i]+"\n")
            #for stock
            for i in range(len(name)):
               o.write(name[i]+","+author[i]+","+str(quantity[i])+","+str(price[i])+"\n")

        #if there is no file of borrower
        except FileNotFoundError:
            print("\n"+firstnam+" has not borrowed any book.")



    try:
        o=open("stock.txt","r")
        temp = o.readlines()
        temp=[x.strip('\n') for x in temp]
        for line in temp:
            currentline = line.split(",")
            name.append(currentline[0])
            author.append(currentline[1])
            quantity.append(int(currentline[2]))
            price.append(currentline[3])
            
        #Program display
        print("WELCOME TO LIBRARY MANAGEMENT SYSTEM\n")
        print("Available commads: ")
        print("Borrow = To borrow books")
        print("Return = To return books")
        print("Stock = To check available books")
        print("Quit = To close program\n")
        
        #starting loop until user decide to close
        while True:
            print("What would you like to do? ")
            command = str(input("> "))

            #if user wants to quit 
            if command.lower()=="quit":
                print("Program is closing.....\nPress any enter to continue.....")
                input()
                break

            #if user wants to borrow, calling borrowing method
            elif command.lower() == "borrow":
                borrowing()
                print("\n")
                
            #if user wants to check stock, calling stock method    
            elif command.lower() == "stock":
                stock()
                print("\n")
                
            #if user wants to return, calling ret method    
            elif command.lower() == "return":
                ret()
                print("\n")

            #if user use wrong command            
            else:
                print("Please enter the valid command.\n")

        
    except FileNotFoundError:
        print("stock file not found. Please read readme for more information.");