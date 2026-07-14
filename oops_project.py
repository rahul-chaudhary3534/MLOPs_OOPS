class ChatBook:
    __user_id = 1
    def __init__(self):
        self.__name = "Default user"
        self.id = chatBook.__user_id
        chatBook.__user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()

    @staticmethod
    def get_id(self):
        return chatBook.__user_id
    @staticmethod
    def set_id(self, id):
        chatBook.__user_id = id

    def get_name(self): #getter method
        return self.__name
    
    def set_name(self, name): #setter method
        self.__name = name


    def menu(self):
        user_input = input(
            "Hello, please choose:\n"
            "1. Login\n"
            "2. Sign Up\n"
            "3. Write a Post\n"
            "4. Message\n"
            "Press any other key to Exit\n"
        )

        if user_input == "1":
            self.login()
        elif user_input == "2":
            self.signup()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.msg()
        else:
            exit()

    def signup(self):
        email = input("enter your email ->" )
        pwd = input("password ->" )
        self.username = email
        self.password = pwd
        print("you have signedup successfully")
        print("\n")
        self.menu()

    def login(self):
        if self.username =='' and self.password == '':
            print("please signup please by pressing 2 in the menu")
        else:
            uname = input("username-> ")
            pasw = input("password-> ")
            if self.username == uname and self.password == pasw :
                print("you are successfully loggedin !!")
                self.loggedin = True
            else: print("give correct credentials")
        print("\n")
        self.menu()

    def post(self):
        if self.loggedin == True :
            txt = input("print your msg here--> ")
            print(f"posted content --> {txt}")
        else:
            print("you need to login first")
        
        print("\n")
        self.menu()

    def msg(self):
        if self.loggedin == True :
            txt = input("print your msg here--> ")
            frnd = input("enter your friend name--> ")
            print(f"message sent to {frnd} --> {txt}")
        else:
            print("you need to login first")
        print("\n")
        self.menu()






user1 = ChatBook()