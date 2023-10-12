class string:
    def __init__(self):
        self.uppercase=0
        self.lowercase=0
        self.vowels=0
        self.consonants=0
        self.space=0
        self.string=" "
    def getstr(self):
        self.string=str(input("ENTER A STRING"))
    def count_upper(self):
        for ch in self.string:
            if (ch.isupper()):
                self.uppercase+=1
    def count_lower(self):
        for ch in self.string:
            if (ch.islower()):
                self.lowercase+=1
    def count_vowels(self):
        for ch in self.string:
            if (ch in('A','a','E','e','I','i','o','O','L','l')):
                self.vowels+=1
    def count_consonants(self):
        for ch in self.string:
            if (ch not in('A','a','E','e','I','i','o','O','L','l')):
                self.consonants+=1
    def count_space(self):
        for ch in self.string:
            if (ch==" "):
                self.space+=1
    def execute(self):
        self.count_upper()
        self.count_lower()
        self.count_vowels()
        self.count_consonants()
        self.count_space()
    def display(self):
        print("THE GIVEN STRING CONTAINS........")
        print("%d UPPERCASE LETTERS"%self.uppercase)
        print("%d LOWERCASE LETTERS"%self.lowercase)
        print("%d VOWELS"%self.vowels)
        print("%d CONSONANATS"%self.consonants)
        print("%d SPACES"%self.space)
s=string()
s.getstr()
s.execute()
s.display()
