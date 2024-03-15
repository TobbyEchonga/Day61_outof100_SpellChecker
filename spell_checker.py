import enchant

# Initialize the enchant spell checker
spell_checker = enchant.Dict("en_US")

def check_spelling(word):
    return spell_checker.check(word)

def suggest_corrections(word):
    return spell_checker.suggest(word)

if __name__ == "__main__":
    while True:
        word = input("Enter a word to check its spelling (or type 'exit' to quit): ").strip()
        if word.lower() == "exit":
            print("Spell checker terminated.")
            break

        if check_spelling(word):
            print("Spelling is correct!")
        else:
            print("Spelling is incorrect.")
            suggestions = suggest_corrections(word)
            if suggestions:
                print("Suggestions:")
                for suggestion in suggestions:
                    print(suggestion)
            else:
                print("No suggestions available.")
