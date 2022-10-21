def guess_user_number():
    min_digit = 0
    max_digit = 1000

    user_possibile_answers = ["za dużo", "za mało", "zgadłeś"]

    answer = ""
    counter = 0

    while answer != user_possibile_answers[2]:
        counter += 1
        guess = int((max_digit - min_digit) / 2) + min_digit
        print(f"Zgaduję: {guess}")
        answer = input(f"Zgadłem? (dozwolone odpowiedzi:{', '.join(user_possibile_answers)})\n")

        if answer != user_possibile_answers[2] and counter >= 10:
            print("Nie oszukuj!")
        elif answer == user_possibile_answers[0]:
            max_digit = guess
        elif answer == user_possibile_answers[1]:
            min_digit = guess
        elif answer == user_possibile_answers[2]:
            print("Zgadłem!")
        else:
            print("Nie poprawna odpowiedź!")
            counter -= 1

guess_user_number()
