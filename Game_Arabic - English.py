import tkinter as tk
import random

# =========================
# إعدادات اللعبة
# =========================

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0
draw_score = 0

time_left = 10


# =========================
# إعادة تشغيل الوقت
# =========================

def reset_timer():
    global time_left
    time_left = 10
    update_timer()


# =========================
# تحديث الوقت
# =========================

def update_timer():
    global time_left

    timer_label.config(
        text=f"الوقت المتبقي: {time_left}\nTime Left: {time_left}"
    )

    if time_left > 0:
        time_left -= 1
        window.after(1000, update_timer)

    else:
        time_out()


# =========================
# عند انتهاء الوقت
# =========================

def time_out():
    global computer_score

    computer_score += 1

    result_label.config(
        text="⏰ انتهى الوقت! نقطة للكمبيوتر\n⏰ Time is over! Computer gets 1 point",
        fg="orange"
    )

    score_label.config(
        text=f"اللاعب: {player_score} | الكمبيوتر: {computer_score} | التعادل: {draw_score}\n"
             f"Player: {player_score} | Computer: {computer_score} | Draws: {draw_score}"
    )

    reset_timer()


# =========================
# اللعب
# =========================

def play(player_choice):

    global player_score
    global computer_score
    global draw_score

    computer_choice = random.choice(choices)

    # التعادل
    if player_choice == computer_choice:

        draw_score += 1

        result = (
            f"🤝 تعادل!\n"
            f"أنت اخترت: {player_choice}\n"
            f"الكمبيوتر اختار: {computer_choice}\n\n"
            f"🤝 Draw!\n"
            f"You chose: {player_choice}\n"
            f"Computer chose: {computer_choice}"
        )

        color = "yellow"

    # فوز اللاعب
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):

        player_score += 1

        result = (
            f"✅ أنت فزت!\n"
            f"أنت اخترت: {player_choice}\n"
            f"الكمبيوتر اختار: {computer_choice}\n\n"
            f"✅ You Win!\n"
            f"You chose: {player_choice}\n"
            f"Computer chose: {computer_choice}"
        )

        color = "lightgreen"

    # فوز الكمبيوتر
    else:

        computer_score += 1

        result = (
            f"❌ الكمبيوتر فاز!\n"
            f"أنت اخترت: {player_choice}\n"
            f"الكمبيوتر اختار: {computer_choice}\n\n"
            f"❌ Computer Wins!\n"
            f"You chose: {player_choice}\n"
            f"Computer chose: {computer_choice}"
        )

        color = "red"

    # تحديث النتيجة
    result_label.config(text=result, fg=color)

    # تحديث السكور
    score_label.config(
        text=f"اللاعب: {player_score} | الكمبيوتر: {computer_score} | التعادل: {draw_score}\n"
             f"Player: {player_score} | Computer: {computer_score} | Draws: {draw_score}"
    )

    # إعادة الوقت
    reset_timer()


# =========================
# إنشاء النافذة
# =========================

window = tk.Tk()

window.title("لعبة حجر ورقة مقص | Rock Paper Scissors")

window.geometry("650x700")

window.configure(bg="#1e1e1e")


# =========================
# معلومات المطور
# =========================

footer = tk.Label(
    window,
    text="Developer:\nMohamed Almehaish\nIbrahim Alawadh",
    font=("Arial", 9, "bold"),
    bg="#1e1e1e",
    fg="white",
    justify="left"
)

footer.place(x=15, y=15)


# =========================
# العنوان
# =========================

title = tk.Label(
    window,
    text="🎮 لعبة حجر ورقة مقص\nRock Paper Scissors",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="orange",
    justify="center"
)

title.pack(pady=70)


# =========================
# تصميم الأزرار
# =========================

button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#ff5722",
    "fg": "white",
    "width": 18,
    "height": 2
}


# زر حجر
rock_button = tk.Button(
    window,
    text="🪨 حجر\nRock",
    command=lambda: play("Rock"),
    **button_style
)

rock_button.pack(pady=8)


# زر ورقة
paper_button = tk.Button(
    window,
    text="📄 ورقة\nPaper",
    command=lambda: play("Paper"),
    **button_style
)

paper_button.pack(pady=8)


# زر مقص
scissors_button = tk.Button(
    window,
    text="✂️ مقص\nScissors",
    command=lambda: play("Scissors"),
    **button_style
)

scissors_button.pack(pady=8)


# =========================
# النتيجة
# =========================

result_label = tk.Label(
    window,
    text="ابدأ اللعب!\nStart Playing!",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e",
    fg="white",
    justify="center"
)

result_label.pack(pady=15)


# =========================
# السكور
# =========================

score_label = tk.Label(
    window,
    text="اللاعب: 0 | الكمبيوتر: 0 | التعادل: 0\nPlayer: 0 | Computer: 0 | Draws: 0",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e",
    fg="cyan",
    justify="center"
)

score_label.pack(pady=8)


# =========================
# الوقت
# =========================

timer_label = tk.Label(
    window,
    text="الوقت المتبقي: 10\nTime Left: 10",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="lightgreen",
    justify="center"
)

timer_label.pack(pady=15)


# =========================
# تشغيل العداد
# =========================

update_timer()


# =========================
# تشغيل اللعبة
# =========================

window.mainloop()
