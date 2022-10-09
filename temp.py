import pandas as pd
import matplotlib.pyplot as plt
colnames=['city','hotel code','Room code','cost','Status']
Hotel_Database=pd.read_csv("C:\\Users\\siddh\\Downloads\\IP IP.csv",names=colnames,header=None)
bookings =pd.read_csv("C:\\Users\\siddh\\Downloads\\bookings.csv")
Hotel_Databasei=Hotel_Database.set_index('Room code')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth',None)
dec=input('Please enter DEL or Del or del if you would like to delete a booking,if not please enter Start or START or start')
   
def Hotelpicker():
    print('What hotel would you like to book? ')
    print('please choose from the options below: ')
    print(Hotel_Databasei)
    hotel=input('Enter Room code of the hotel you would like to book: ')
    status=Hotel_Databasei.at[hotel,'Status']
    if status=='BOOKED':
         print('This hotel is already booked, please try again...')
         Hotelpicker()
    else:
        name = input("Enter your name: ")
        day = int((input('The number of days you would like to stay: ')))
        price= int(Hotel_Databasei.at[hotel,'cost'])
        print('The amount needed is',price*day)
        bookings['Sales'] = [name]
        bookings['Days'] = [day]
        bookings['Amount paid'] =[price*day]
        bookings['Hotel'] = [hotel]
        print('Your booking details are\n',bookings[bookings['Sales']==name])
        Hotel_Databasei.loc[hotel,'Status']=['BOOKED']

    
    
def deleter():
    y=input('Please enter Del or DEL or del to cancel a booking')
    if y=='DEL' or y=='Del' or y=='del':
        c=input('Enter your name exactly as it was entered prior')
        bookings.drop(bookings.index[bookings['Sales']==c])
        print('your booking has been sucessfully deleted')
        
    else:
        print('Please try again')
def sales():
    yes=input("Would u like to see our current sales data, Enter yes if u do, If you would like to see our year 1 sales data enter q1\n Enter no if otherwise")
    if yes=='yes'or yes=='YES'or yes=='Yes':
        SALES=[2300000,1100000,40000000,90000000]
        Months=['Quarter 1','Quarter 2','Quarter 3','Quarter 4']
        type=input('Enter bar if you would like to see it as a bar graph\nEnter line if you would like to see it as a line graph\nEnter scatter if you would like to see it as a scatter chart')
        if type=='bar'or type=='Bar' or type=='BAR':
            plt.bar(Months,SALES)
            plt.show()
        elif type=='line'or type=='LINE'or type=='Line':
            plt.plot(Months,SALES)
            plt.show()
        elif type=='scatter'or type=='SCATTER' or type=='Scatter':
            plt.scatter(Months,SALES)
            plt.show()
        elif yes=='no' or yes=='NO' or yes=='No':
            print('Thank you for booking with us')
        
if dec=='DEL'or dec=='del' or dec=='Del':
    deleter()
elif dec=='Start'or dec=='START' or dec=='start':
    Hotelpicker()
    sales()
    bookings.to_csv("C:\\Users\\siddh\\Downloads\\bookings.csv")
      
else:
    print('Enter a valid input')
