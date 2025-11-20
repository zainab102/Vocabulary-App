class VocabularyApp:
    def __init__(self):
        # Sample vocabulary list (word, meaning)
        self.vocabulary = [
            ("hello", "a greeting"),
            ("world", "the planet we live on"),
            ("python", "a programming language"),
            ("tkinter", "a GUI library for Python"),
            ("flashcard", "a card used for learning"),
            ("vocabulary", "the set of words used in a language"),
            ("meaning", "the definition of a word"),
            ("correct", "right or accurate"),
            ("incorrect", "wrong or inaccurate"),
            ("progress", "the process of improving")
        ]
        self.current_index = 0
        self.total_words = len(self.vocabulary)

    def run(self):
        print("Welcome to the Vocabulary App!")
        print("Type the meaning of each word. Press Enter to submit.")
        print("=" * 40)

        while self.current_index < self.total_words:
            word, correct_meaning = self.vocabulary[self.current_index]
            print(f"\nWord {self.current_index + 1} of {self.total_words}: {word}")
            user_input = input("Your meaning: ").strip().lower()

            if user_input == correct_meaning.lower():
                print("Correct!")
            else:
                print(f"Incorrect! The correct meaning is: {correct_meaning}")

            input("Press Enter to continue to the next word...")
            self.current_index += 1

        print("\nCompleted all words! Well done.")

if __name__ == "__main__":
    app = VocabularyApp()
    app.run()
