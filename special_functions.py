class complex:
    def __init__(self,real,complex):
        self.real=real
        self.complex=complex
    def __add__(self,others):
        if isinstance(others,complex):
            return complex(self.real+others.real,self.complex+others.complex)
        else:
            raise TypeError("Unsupported operant")
    def __str__(self):
        return f"{self.real} + {self.complex}i"
i=complex(5,5)
j=complex(4,8)
print(i+j)