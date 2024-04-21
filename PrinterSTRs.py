import requests
from io import StringIO

# تحديد رابط الملف على GitHub
url = 'https://raw.githubusercontent.com/Xfya0/Qwe/main/Soka.py'

# استدعاء الملف وتحويله إلى ملف نصي
response = requests.get(url)
file_content = response.text

# تحويل المحتوى إلى ملف
file_object = StringIO(file_content)

# استدعاء الدالة من الملف
exec(file_object.read())

# النص الذي تريد تحويله
input_string = input("Enter a string: ")

# استخدام الدالة المستدعاة من الملف
converted_string = convert_to_custom_format(input_string, write_side_by_side=True)

print(converted_string)
