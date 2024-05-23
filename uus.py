import random
import string

def generate_content(character_type, chars_per_line, lines_count):
    content = []
    if character_type == "letters":
        characters = string.ascii_letters
    elif character_type == "digits":
        characters = string.digits
    elif character_type == "dots":
        characters = '.'
    else:
        raise ValueError("Invalid character type. Choose from 'letters', 'digits', or 'dots'.")

    for _ in range(lines_count):
        line = ''.join(random.choice(characters) for _ in range(chars_per_line))
        content.append(line)
    
    return '\n'.join(content)

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# إعدادات البرنامج
character_type = "letters"  # يمكنك تغيير هذا إلى "digits" أو "dots"
chars_per_line = 10
lines_count = 5
filename = "output.txt"

# توليد المحتوى وحفظه في ملف
content = generate_content(character_type, chars_per_line, lines_count)
save_to_file(filename, content)

print(f"تم حفظ المحتوى في الملف {filename}")