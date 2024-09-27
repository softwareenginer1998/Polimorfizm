class Harorat:
    def __init__(self, qiymat, birlik):
        self.qiymat = qiymat
        self.birlik = birlik.lower()

    def konvertatsiya_qilish(self):
        if self.birlik == "selsiy":

            farenhayt = (self.qiymat * 9/5) + 32
            return farenhayt, "Farenhayt"
        elif self.birlik == "farenhayt":

            selsiy = (self.qiymat - 32) * 5/9
            return selsiy, "Selsiy"
        else:
            raise ValueError("Noto'g'ri birlik! 'Selsiy' yoki 'Farenhayt' bo'lishi kerak.")


qiymat = float(input("Harorat qiymatini kiriting: "))
birlik = input("O'lchov birligini kiriting (Selsiy/Farenhayt): ")


try:
    harorat = Harorat(qiymat, birlik)
    natija, yangi_birlik = harorat.konvertatsiya_qilish()
    print(f"{harorat.qiymat} {harorat.birlik.capitalize()} = {natija:.2f} {yangi_birlik}")
except ValueError as e:
    print(e)
