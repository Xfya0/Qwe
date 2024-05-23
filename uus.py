import random
import string

def generate_non_repeating_content(character_type, chars_per_line, lines_count):
    all_characters = string.ascii_letters + string.digits + '.'
    content = []
    
    for _ in range(lines_count):
        line = []
        for _ in range(chars_per_line):
            while True:
                char = random.choice(all_characters)
                if not line or char != line[-1]:
                    line.append(char)
                    break
        content.append(''.join(line))
    
    return '\n'.join(content)

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# طلب الإعدادات من المستخدم
chars_per_line = int(input("أدخل عدد الأحرف في كل سطر: "))
lines_count = int(input("أدخل عدد الأسطر: "))
filename = input("أدخل اسم الملف لحفظ المحتوى: ").strip()

# توليد المحتوى وحفظه في ملف
content = generate_non_repeating_content("mixed", chars_per_line, lines_count)
save_to_file(filename, content)

print(f"تم حفظ المحتوى في الملف {filename}")