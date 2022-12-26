class Instagram:
    app="Instagram"
    def __init__(self,username,email,password):
        print("i am a constructor")
        self.username=username
        print("i am setting username",self.username)
        self.email=email
        print("i am setting email",self.email)
        self.password=password
        print("i am setting password",self.password)

    def UserDetails(self):
        note="Do not share your password"
        print(f'{self.app},\nUsername is {self.username}\nEmail is {self.email}\n {note}')
user1=Instagram("ark","arkprocoder@gmail.com","******")
print("\n")
user2=Instagram("ria","riainstitute@gmail.com","********")
user1.UserDetails()
print(user2.__dict__)
# print(user1.email)
