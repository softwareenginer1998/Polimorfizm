import random

class Savol:
    def __init__(self, matn, variantlar, togri_javob):
        self.matn = matn
        self.variantlar = variantlar
        self.togri_javob = togri_javob

    def tekshirish(self, foydalanuvchi_javob):
        return foydalanuvchi_javob == self.togri_javob

class Test:
    def __init__(self):
        self.savollar = []

    def savol_qoshish(self, savol):
        self.savollar.append(savol)

    def test_olish(self):
        if not self.savollar:
            print("Savollar mavjud emas.")
            return

        random.shuffle(self.savollar)
        ball = 0

        for savol in self.savollar:
            print(savol.matn)
            for idx, variant in enumerate(savol.variantlar):
                print(f"{idx + 1}. {variant}")
            foydalanuvchi_javob = int(input("Javobingizni tanlang (raqam): ")) - 1

            if savol.tekshirish(foydalanuvchi_javob):
                print("To'g'ri!")
                ball += 1
            else:
                print("Noto'g'ri! To'g'ri javob:", savol.togri_javob + 1)
            print()

        self.ballni_korsh(ball)

    def ballni_korsh(self, ball):
        print(f"Sizning ballingiz: {ball}/{len(self.savollar)}")

# Misol uchun test yaratamiz
test = Test()
test.savol_qoshish(Savol("Dunyoning eng katta okeani qaysi?", ["Tinch okeani", "Atlantika okeani", "Hind okeani"], 0))
test.savol_qoshish(Savol("Piyoda yo'lidan o'tayotganda qanday harakat qilish kerak?", ["Yurgan holda", "Tez yugurish", "To'xtab kutish"], 2))
test.savol_qoshish(Savol("Qaysi rang to'rtburchakda eng ko'p uchraydi?", ["Qizil", "Ko'k", "Yashil"], 1))

# Testni o'tkazamiz
test.test_olish()
