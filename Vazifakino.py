import random


class Film:
    def __init__(self, nom, janr, reyting):
        self.nom = nom
        self.janr = janr
        self.reyting = reyting

    def __str__(self):
        return f"{self.nom} - Janr: {self.janr}, Reyting: {self.reyting}"


class TavsiyaTizimi:
    def __init__(self):
        self.filmlar = []

    def film_qoshish(self, film):
        self.filmlar.append(film)

    def tavsiya_berish(self, afzal_janr):

        mos_filmlar = [film for film in self.filmlar if film.janr.lower() == afzal_janr.lower()]

        if not mos_filmlar:
            print(f"{afzal_janr} janrida film topilmadi.")
            return


        tavsiya_qilingan_film = random.choice(mos_filmlar)
        print("Tavsiya etilgan film:", tavsiya_qilingan_film)



tizim = TavsiyaTizimi()

tizim.film_qoshish(Film("Inception", "Sci-Fi", 8.8))
tizim.film_qoshish(Film("The Godfather", "Crime", 9.2))
tizim.film_qoshish(Film("The Dark Knight", "Action", 9.0))
tizim.film_qoshish(Film("Interstellar", "Sci-Fi", 8.6))
tizim.film_qoshish(Film("Parasite", "Thriller", 8.6))

afzal_janr = input("Qaysi janrni afzal ko'rasiz? ")
tizim.tavsiya_berish(afzal_janr)
