# Citim datele despre cuvinte și din dicționarului din fișiere
with open('data.txt', 'r', encoding='utf-8') as f:
    words_data = f.read()

with open('dictionar.txt', 'r', encoding='utf-8') as f:
    dictionary_content = f.read()

# Inițializăm variabilele de urmărire
total_tries = 0
alphabet_order = "AĂEIRTOCNLSMNUPDGFVZBHȚȘÂJXÎKYWQ"

# Pregătim datele 
word_rows = words_data.strip().split("\n")
dictionary_words = [word.upper() for word in dictionary_content.strip().split("\n")]

# Procesarea cuvintelor
for row in word_rows:
    letter_index = 0
    row_number, masked_word, actual_word = row.split(";")
    current_guess = masked_word

    # Filtrăm cuvintele din dicționar după lungime
    potential_words = [word for word in dictionary_words if len(word) == len(actual_word)]

    # Filtrăm cuvintele pe baza literelor dezvăluite din cuvânt
    potential_words = [word for word in potential_words if all(
        current_guess[i] == "*" or current_guess[i] == word[i] for i in range(len(current_guess))
    )]

    tries_for_this_word = 0
    while current_guess != actual_word:
        print(f"Current Guess: {current_guess}, Next Letter: {alphabet_order[letter_index]}, Tries: {tries_for_this_word}")

        # După procesele de mai sus, verificăm dacă există o singură posibilitate de cuvânt rămasă
        if len(potential_words) == 1:
            current_guess = potential_words[0]
            tries_for_this_word += 1
            print(f"Guessed the word: {current_guess} in {tries_for_this_word} tries!")
            break

        # Sărim peste dacă litera a fost deja gasită in cuvânt
        if alphabet_order[letter_index] in current_guess:
            print(f"Letter already guessed: {alphabet_order[letter_index]}")
            letter_index += 1
            continue

        # Verificăm dacă litera curentă se află în vreun cuvânt posibil
        if not any(alphabet_order[letter_index] in word for word in potential_words):
            tries_for_this_word += 1
            print(f"Letter {alphabet_order[letter_index]} is not in the word.")
            letter_index += 1
            continue

        # Actualizăm cuvântul dacă litera găsită se potrivește
        updated_guesses = []
        for idx in range(len(actual_word)):
            if current_guess[idx] == "*" and actual_word[idx] == alphabet_order[letter_index]:
                updated_guesses.append(idx)

        if updated_guesses:
            tries_for_this_word += 1
            for idx in updated_guesses:
                current_guess = current_guess[:idx] + alphabet_order[letter_index] + current_guess[idx + 1:]
                print(f"Added letter: {alphabet_order[letter_index]}, Current Tries: {tries_for_this_word}")

        # Trecem la următoarea literă din alfabet
        letter_index += 1

    # Adăugăm încercarea respectivă la numărul total de încercări
    total_tries += tries_for_this_word
    print("____________________")

# Afișăm toate încercările
print(f"Total tries: {total_tries}")
 