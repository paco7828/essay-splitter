import re

print("Press enter every time you have finished a sentence!")
print("--------------------------------------------------------------------------------")
ask_for_input = True
try:
    with open("essay.txt", "r", encoding="utf-8") as file:
        text = file.read()
        if not text.strip():
            raise ValueError("The essay.txt is empty.")
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        if not sentences:
            raise ValueError("No sentences found.")
        for sentence in sentences:
            if ask_for_input:
                try:
                    input()
                except KeyboardInterrupt:
                    print("\nInterrupted by user, exiting...")
                    break
            else:
                print(sentence)
            if sentence == sentences[-1]:
                ask_for_input = False
            print(sentence)

except FileNotFoundError:
    print("Error: File not found!")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")