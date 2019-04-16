
import re

class string_mods:
    
    def __init__(self):
        #self.email = email_raw or None
        self.email = ''
    
    def remove_dot_from_name(self):
        try:
            input_string_array = self.email.split('@')
            email_name = input_string_array[0]
            email_name = re.sub('\.', '', email_name)
            email_server = '@' + input_string_array[1]
            return(email_name + email_server)
        except:
            print("hmm, that doesnt look like a normal email address...")
            return(self.email)
    
    def set_email(self):
        self.email = input("Input email address with dot name: ") or None
        if self.email is None:
            self.email = 'max.perez@gmail.com'
            
            
# get email address from user or use default
#default_email = ''
str1 = string_mods()
str1.set_email()
print("email address entered is " + str1.email)
result = str1.remove_dot_from_name()
print('cleaned name is: ' + result)
