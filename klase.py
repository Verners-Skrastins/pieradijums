class Auto:
    def __init__(self, marka, modelis):
        self.marka = marka
        self.modelis = modelis

    def izvadit_informaciju(self):
        print(f"Auto: {self.marka}  {self.modelis}")
        
# Izveidojam objektu, pamatojoties uz klases "Auto"

mans_auto = Auto("Toyota", "Camry")

 

# Piekļūstam objekta īpašībām

print(f"Mana automašīna ir {mans_auto.marka} {mans_auto.modelis}")

 

# Izsaucam objekta metodi

mans_auto.izvadit_informaciju()