from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

def easy_question():
    questions = [
        ("ง่าย (2 + 2) เท่ากับเท่าไหร่?", 4),
        ("ง่าย (10 - 3) เท่ากับเท่าไหร่?", 7),
        ("ง่าย (5 * 4) เท่ากับเท่าไหร่?", 20),
        ("ง่าย (8 / 2) เท่ากับเท่าไหร่?", 4),
        ("ง่าย (9 + 6) เท่ากับเท่าไหร่?", 15),
        ("ง่าย (1 + 1) เท่ากับเท่าไหร่?", 2),
        ("ง่าย (7 + 2) เท่ากับเท่าไหร่?", 9),
        ("ง่าย (4 + 4) เท่ากับเท่าไหร่?", 8),
        ("ง่าย (3 + 2) เท่ากับเท่าไหร่?", 5),
        ("ง่าย (10 + 6) เท่ากับเท่าไหร่?", 16),
         #เพิ่ม 5 ข้อ
        ("ง่าย (23 + 45) เท่ากับเท่าไหร่?", 68),
        ("ง่าย (63 + 29) เท่ากับเท่าไหร่?", 92),
        ("ง่าย (56 + 43) เท่ากับเท่าไหร่?", 99),
        ("ง่าย (56 + 78) เท่ากับเท่าไหร่?", 134),
        ("ง่าย (105 - 48) เท่ากับเท่าไหร่?",57),
    ]
    return random.choice(questions)

def medium_question():
    questions = [
        ("กลาง (10 * 5) เท่ากับเท่าไหร่?", 50),
        ("กลาง (20 ÷ 4) เท่ากับเท่าไหร่?", 5),
        ("กลาง (15 + 8) เท่ากับเท่าไหร่?", 23),
        ("กลาง (18 - 7) เท่ากับเท่าไหร่?", 11),
        ("กลาง (25 * 4) เท่ากับเท่าไหร่?", 100),
        ("กลาง (42 ÷ 6) เท่ากับเท่าไหร่?", 7),
        ("กลาง (96 ÷ 8) เท่ากับเท่าไหร่?", 12),
        ("กลาง (16 + 19) เท่ากับเท่าไหร่?", 35),
        ("กลาง (7 * 2) เท่ากับเท่าไหร่?", 14),
        ("กลาง (8 * 3) เท่ากับเท่าไหร่?", 24),
        #เพิ่ม 5 ข้อ
        ("กลาง (11 * 4) เท่ากับเท่าไหร่?", 44),
        ("กลาง (3 * 12) เท่ากับเท่าไหร่?", 36),
        ("กลาง (7 * 9) เท่ากับเท่าไหร่?", 63),
        ("กลาง (36 ÷ 6) เท่ากับเท่าไหร่?", 6),
        ("กลาง (10 * 3) เท่ากับเท่าไหร่?",30),
    ]
    return random.choice(questions)

def hard_question():
    questions = [
        ("ยาก (25 * 3) เท่ากับเท่าไหร่?", 75),
        ("ยาก (48 ÷ 8) เท่ากับเท่าไหร่?", 6),
        ("ยาก (11 * 7) เท่ากับเท่าไหร่?", 77),
        ("ยาก (63 ÷ 9) เท่ากับเท่าไหร่?", 7),
        ("ยาก (7 * 7) เท่ากับเท่าไหร่?", 49),
        ("ยาก (5 * 3) เท่ากับเท่าไหร่?", 15),
        ("ยาก (3 * 6) เท่ากับเท่าไหร่?", 18),
        ("ยาก (10 ÷ 2) เท่ากับเท่าไหร่?", 5),
        ("ยาก (80 ÷ 2) เท่ากับเท่าไหร่?", 40),
        ("ยาก (90 ÷ 3) เท่ากับเท่าไหร่?", 30),
        #เพิ่ม 5 ข้อ
        ("ยาก (543 + 876) เท่ากับเท่าไหร่?", 1419),
        ("ยาก (723 - 486) เท่ากับเท่าไหร่?", 36),
        ("ยาก (789 - 234) เท่ากับเท่าไหร่?", 555),
        ("ยาก (654 + 321) เท่ากับเท่าไหร่?", 975),
        ("ยาก (20 * 3) เท่ากับเท่าไหร่?",60), 
    ]
    return random.choice(questions)

def get_question():
    global difficulty
    if difficulty == "easy":
        return easy_question()
    elif difficulty == "medium":
        return medium_question()
    elif difficulty == "hard":
        return hard_question()

def start_game():
    global score, difficulty, current_question, question_number
    score = 0
    difficulty = "medium"
    current_question = get_question()
    question_number = 1

start_game()

def check_game_completion():
    global score
    if score == 10:
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    global score, current_question, difficulty, question_number
    if request.method == 'GET':
        if check_game_completion():
            return render_template('completion.html', score=score)
        return render_template('index.html', question=current_question[0], score=score, difficulty=difficulty, question_number=question_number)

    elif request.method == 'POST':
        user_answer = int(request.form['answer'])
        correct_answer = current_question[1]

        if user_answer == correct_answer:
            score += 1
            update_difficulty_on_correct()
        else:
            update_difficulty_on_incorrect()

        current_question = get_question()
        question_number += 1

        if question_number > 10:  # ตรวจสอบว่าทำข้อสอบครบ 10 ข้อหรือไม่
            return render_template('completion.html', score=score)

        return render_template('index.html', question=current_question[0], score=score, difficulty=difficulty, question_number=question_number)



@app.route('/start', methods=['POST'])
def start_new_game():
    start_game()
    return redirect('/')



    
def update_difficulty_on_correct():
    global difficulty
    if difficulty == "hard":
        return
    elif difficulty == "medium":
        difficulty = "hard"
    elif difficulty == "easy":
        difficulty = "medium"

def update_difficulty_on_incorrect():
    global difficulty
    if difficulty == "hard":
        difficulty = "medium"
    elif difficulty == "medium":
        difficulty = "easy"
    elif difficulty == "easy":
        pass

if __name__ == '__main__':
    app.run(debug=True)