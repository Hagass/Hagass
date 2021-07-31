from faker import Faker
from colorama import Fore,init
init()

print(Fore.BLUE+'''Hi Welcome To Fake Details Generator
My TelegramID:@Hagaso_o
Join us: @Account_Config
App_version:1.0
Thanks For using:''')

while True:
    login=input('''
For start/or continue to get info please write(start):
''')
    fake=Faker()
    def details(Name , Address , Credit_Card ,Cc_Expiry , Cvv , Mail ,Job , Country_code , Phone_Number,User):
        print(Name,fake.first_name())
        print(Address,fake.address())
        print(Credit_Card,fake.credit_card_number())
        print(Cc_Expiry,fake.credit_card_expire())
        print(Cvv,fake.credit_card_security_code())
        print(Mail,fake.email())
        print(Job,fake.job())
        print(Country_code,fake.country_calling_code())
        print(Phone_Number,fake.msisdn())
        print(User,fake.chrome())
    
    if login =="start":
        
        details('Name is:',
        'Address is:',
    'Credit number is:',
            'Card expires:',
                'Cvv is:',
            'Email is:',
            'Job is :',
            'Country_code is:',
            'Phone_number is :',
            'User_agent is :')
                
    
        
    else:
        print('try again')
        
