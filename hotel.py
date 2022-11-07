#Project-'Hotel Management'
def hotelmanagement():
    import random as r
    x=1
    def bill(rec,feed,feed1,l):
        cust=input('Enter the customer name:')
        ph=int(input('Enter the phone number:'))
        cus=cust.title()
        if cus not in rec:
            print('Name not found')
            return rec , feed1,l
        else:
            x=rec.get(cus)
            print(x)
            y=x.get('Room number:')
            for i in x.values():
                if i!=ph:
                    print('Wrong number entered')
                    return rec , feed1,l
                else:
                    print('Charges:')
                    print('a.Stay per day=Rs.750\nb.Pick and drop service=Rs.200')
                    print('c.Tourist Guide charge(per day)=Rs.200')
                    days=int(input('Enter the days of stay:'))
                    g_days=int(input('Enter the days with guide(if not included enter 0):'))
                    drop=input('Pick and Drop service is included (yes/no):')
                    if drop =='yes' or 'Yes':
                        cost=(days*750)+(g_days*200)+200
                    else:
                        cost=(days*750)+(g_days*200)
                    print('Amount to be pay=Rs.',cost)
                    print('Thank you for visiting us!!!')
                    rate=int(input('Please rate our services out of 5:'))
                    feedback=input('Please give your feedback:')
                    del rec[cus]
                    feed.append(ph)
                    feed.append(rate)
                    feed.append(feedback)
                    feed1[cus]=feed
                    l.remove(y)
                   
                    return rec , feed1 ,l
            
    def phno(rec,whose):
        phn=int(input('Enter the new phone number:'))
        x=rec[whose]
        d={'Ph number:':phn}
        x.update(d)
        print('Changed successfully')
        return  rec                 

    def room(rec,whose,l):
        old=int(input('Please confirm your old room number:'))
        print('Room available are: ',end='')
        for i in range(1,11):
            if (i not in l )and (old!=i):
                print(i,end=',')
        print()
        rono=int(input('Which room do you want?'))
        x=rec[whose]
        d={'Room number:':rono}
        x.update(d)
        l.append(rono)
        l.remove(old)
        print('Changed successfully')
        return   rec,l 
    
    def book(rec,l):
        detail={}
        if len(l)==10:
            print('Sorry, no room is available')
            return (rec,l)
        name=input("Enter the customer's name:")
        name=name.title()
        ph=int(input("Enter the customer's ph. number:"))
        while  True:
            r_no=r.randint(1,10)
            if r_no not in l:
                l.append(r_no)
                break
        
        print('Your booking is done! Your room number is',r_no)
        detail['Ph number:']=ph
        detail['Room number:']=r_no
        rec[name]=detail
        return (rec,l)
        
    def start2(opt,rec,l,feed,feed1,st):
                x=0
                if opt==1:
                     rec,l=book(rec,l)
                     print()
                     y_n=input('Do you want to explore more?')
                     yn=y_n.title()
                     if yn =='Yes':
                         option(rec,l,x,feed,feed1,st)
                        
                elif opt==2:
                   print(rec)
                   for x,y in rec.items():
                       print('Customer name:',x)
                       for a,b in y.items():
                               print(a,':',b)
                   y_n=input('Do you want to explore more?')
                   yn=y_n.title()
                   if yn =='Yes':
                       option(rec,l,x,feed,feed1,st)

                elif opt==3:
                    rec,feed1,l=bill(rec,feed,feed1,l)
                    print(feed1)
                    y_n=input('Do you want to explore more?')
                    yn=y_n.title()
                    if yn =='Yes':
                        option(rec,l,x,feed,feed1,st)

                elif opt==4:
                    whose=input('Whose id you want to change?')
                    whose=whose.title()
                    for a,b in rec.items():
                        if whose not in rec:
                            print('.',end='')
                        else:
                            print('Current Status:')
                            print('Customer name:',whose)
                            x=rec.get(whose)
                            break
                    for p,q in x.items():
                            print(p,q)    
                    wh=int(input('What you want to change?(1-ph number 2-room)'))
                    if wh==1:
                        rec=phno(rec,whose)
                        y_n=input('Do you want to explore more?')
                        yn=y_n.title()
                        if yn =='Yes':
                                option(rec,l,x,feed,feed1,st)

                    elif wh==2:
                        rec,l=(room(rec,whose,l))
                        y_n=input('Do you want to explore more?')
                        yn=y_n.title()
                        if yn =='Yes':
                               option(rec,l,x,feed,feed1,st) 

                elif opt==5:
                    st=opt5(opt,rec,l,st,feed,feed1)
                    y_n=input('Do you want to explore more?')
                    yn=y_n.title()
                    if yn =='Yes':
                               print('You are requested to login again')
                               start_for5(st)
                             
    def opt5(opt,rec,l,st,feed,feed1):
                if opt==5:
                        guest=input('Please type your name first to type your complaint:')
                        guest=guest.title()
                        if guest in rec:
                            feed=input('Please enter your complaint here:')
                            print('Your complaint has been registered in the name of',guest)
                            com=guest+'-'+feed
                            st.append(com)
                            print(st)
                        else:
                            print('Only our guests can type their complaints here.')
                            print('You are requested to login again')
                            x=1
                            start_for5(st)
                        
                return (st)            

    def start_for5(st):
            x=0
            username = input("Enter username: ")
            password = input("Enter password: ")
            if(username=="admin" and password =="12345"):
                print('Login Successful')
                print()
                option(rec,l,x,feed,feed1,st)
            else:
                print('Account Blocked')
        
    def start(opt,rec,l,feed,feed1,st):
        if opt<5:
            print('You have to login in to use this function')
            username = input("Enter username: ")
            password = input("Enter password: ")
            if(username=="admin" and password =="12345"):
                print('Login Successful')
                print()
                a=1
            else:
                a=0
                print('Account Blocked')
            if a==1:
                x=0
                start2(opt,rec,l,feed,feed1,st)
        else:
            opt5(opt,rec,l,st,feed,feed1)
                             
    def option(rec,l,x,feed,feed1,st):
        print('    '*16,'Welcome To Dream Hotel !!!')
        print('How can I help you?')
        print()
        print('1.Booking of a room')
        print("2.Guest's information")
        print("3.Bill")
        print("4.Updating")
        print("5.Complaint/Feedback")
        print("6.Exit")
        opt=int(input('Please enter a vaild number:'))
        if x==1 and opt<5:
            start(opt,rec,l,feed,feed1,st)
        else:
            start2(opt,rec,l,feed,feed1,st)           

    rec={}
    l=[]
    feed=[]
    feed1={}
    st=[]
    option(rec,l,x,feed,feed1,st)

