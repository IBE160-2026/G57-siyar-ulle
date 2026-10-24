def calculate_score(user_answers, correct_answers):
    if len(user_answers) != len(correct_answers):
        raise ValueError("Antall svar må være likt antall fasitsvar.")

    score = 0

    for user_answer, correct_answer in zip(user_answers, correct_answers):
        if user_answer == correct_answer:
            score += 1

    return score