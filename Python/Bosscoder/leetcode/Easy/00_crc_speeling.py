from spellchecker import SpellChecker
     
def correct_spelling_pyspellchecker(input_string):
        """
        Corrects the spelling of a given string using pyspellchecker.
        """
        spell = SpellChecker()
        words = input_string.split()
        corrected_words = []
        for word in words:
            # Get the most likely correction for a misspelled word
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word if corrected_word else word) # Handle cases where no correction is found
        return " ".join(corrected_words)

print(correct_spelling_pyspellchecker("Are you marrrried"))