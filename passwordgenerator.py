#beginner
import random
import string

class passwordgenerator1:
   def __init__(self):
       self.lett = string.ascii_lowercase + string.ascii_uppercase
       self.symb = string.punctuation
       self.num = string.digits
       self.pool = self.lett + self.symb + self.num
       self.password = ""

   def generate_password(self):
       # reset password each call
       self.password = ""

       print("-"*8, "Welcome to password generator game", "-"*8)

       # get valid positive integer length
       while True:
           try:
               lent = int(input("Enter how much length should password have: "))
               if lent <= 0:
                   print("Length must be a positive integer.")
                   continue
               break
           except ValueError:
               print("You should enter a number")
               continue

       choice = input(
           "Do you want a specific format? Enter 'yes' for a specific format or 'no' for a combination: "
       )

       if choice.lower() == "yes":
           sy = input("Enter 1 for letters only\n2 for numbers only\n3 for symbols only: ").strip()
           if sy == "1":
               self.password = "".join(random.choices(self.lett, k=lent))
           elif sy == "2":
               self.password = "".join(random.choices(self.num, k=lent))
           elif sy == "3":
               self.password = "".join(random.choices(self.symb, k=lent))
           else:
               print("As you provided wrong information I am creating a random password:")
               self.password = "".join(random.choices(self.pool, k=lent))
       else:
           # ask how many of each and validate inputs
           while True:
               try:
                   numlen = int(input("Enter how many numbers you want in password: "))
                   symlen = int(input("Enter how many symbols you want in password: "))
                   lettlen = int(input("Enter how many letters you want in password: "))
               except ValueError:
                   print("Please enter valid integer counts.")
                   continue

               if numlen < 0 or symlen < 0 or lettlen < 0:
                   print("Counts must be non-negative.")
                   continue

               if numlen + symlen + lettlen != lent:
                   print(
                       "As the selected len of each is not equal to total len I am creating random pass with all three:"
                   )
                   # create roughly equal parts and fill the remainder
                   eachlen = lent // 3
                   parts = []
                   parts += random.choices(self.lett, k=eachlen)
                   parts += random.choices(self.num, k=eachlen)
                   remaining = lent - len(parts)
                   parts += random.choices(self.symb, k=remaining)
                   random.shuffle(parts)
                   self.password = "".join(parts)
                   break
               else:
                   parts = []
                   parts += random.choices(self.lett, k=lettlen)
                   parts += random.choices(self.num, k=numlen)
                   parts += random.choices(self.symb, k=symlen)
                   random.shuffle(parts)
                   self.password = "".join(parts)
                   break

       return self.password

if __name__ == "__main__":
   p = passwordgenerator1()
   generated_password = p.generate_password()
   print(f"Generated Password is: {generated_password}")
