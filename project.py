import speech_recognition as sr
from word2number import w2n
import csv
import os

# File to store roll numbers
CSV_FILE = 'roll_numbers.csv'

# Create file with header if not already present
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Roll Number'])

def capture_roll():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say your roll number...")
        audio = recognizer.listen(source)

        try:
            spoken_text = recognizer.recognize_google(audio)
            print(f"You said: {spoken_text}")
            roll_number = w2n.word_to_num(spoken_text)

            # Store roll number in CSV
            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([roll_number])

            print(f"Roll number {roll_number} saved!")

        except Exception as e:
            print(f"Error recognizing speech: {e}")

# Run the loop
if __name__ == "__main__":
    while True:
        capture_roll()
        cont = input("Add another roll number? (y/n): ").strip().lower()
        if cont != 'y':
            break
