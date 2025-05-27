import sys
from time import sleep
import time

def print_lirik():
    lines = [
        ("Tak nak pusing, tak nak tanya", 0.08),
        ("aku kuat tanpa drama", 0.09),
        ("aku dah lupa, tak ingat lagi", 0.09),
        ("Nama kau pun hilang dari hati", 0.08),
        ("aku move on, hidup sendiri", 0.08),
        ("Tak perlu kau, aku happy", 0.07),
        ("Aku dah lupa, tak ingat lagi", 0.08),
        ("Nama kau pun hilang dari hati", 0.09),
        ("Aku move on, hidup sendiri", 0.08),
        ("Tak perlu kau aku happy", 0.08),
        ("................", 0.20),
    ]

    # Delay antar baris (kalau mau diatur sendiri)
    delays = [0.1, 0.1, 0.1, 0.1, 0.2, 0.3, 0.1, 0.1, 0.1,] * len(lines)  # Panjangnya disesuaikan otomatis

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lirik()
