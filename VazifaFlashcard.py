class Flashcard:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

    def show_word(self):
        return f"Word: {self.word}"

    def check_answer(self, user_answer):
        return user_answer.lower() == self.definition.lower()


class FlashcardCollection:
    def __init__(self):
        self.collection = []

    def add_flashcard(self, flashcard):
        self.collection.append(flashcard)

    def view_flashcards(self):
        for idx, flashcard in enumerate(self.collection):
            print(f"{idx + 1}. {flashcard.show_word()}")


# Example usage of the flashcard app
collection = FlashcardCollection()

# Adding flashcards
collection.add_flashcard(Flashcard("Python", "A programming language"))
collection.add_flashcard(Flashcard("API", "Application Programming Interface"))
collection.add_flashcard(Flashcard("HTML", "HyperText Markup Language"))

# Viewing flashcards
print("Flashcards:")
collection.view_flashcards()

# Asking user for definitions
for flashcard in collection.collection:
    print(flashcard.show_word())
    user_answer = input("Enter the definition: ")
    if flashcard.check_answer(user_answer):
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is: {flashcard.definition}")
    print()