def convert_to_custom_format(character, write_side_by_side=False):
    # كود تحويل الحروف إلى الصيغة المخصصة
    alphabet = {
        'a': ["  ___  ",
              " / _ \\ ",
              "| | | |",
              "| |_| |",
              " \\__,_|"],
        'b': [" ____  ",
              "|  _ \\ ",
              "| |_) |",
              "|  _ < ",
              "|_| \\_\\"],
        'c': ["  ____ ",
              " / ___|",
              "| |    ",
              "| |___ ",
              " \\____|"],
        'd': [" ____  ",
              "|  _ \\ ",
              "| | | |",
              "| |_| |",
              "|____/ "],
        'e': [" _____ ",
              "| ____|",
              "|  _|  ",
              "| |___ ",
              "|_____|"],
        'f': [" _____ ",
              "|  ___|",
              "| |_   ",
              "|  _|  ",
              "|_|    "],
        'g': ["  ____ ",
              " / ___|",
              "| |  _ ",
              "| |_| |",
              " \\____|"],
        'h': [" _   _ ",
              "| | | |",
              "| |_| |",
              "|  _  |",
              "|_| |_|"],
        'i': [" ___ ",
              "|_ _|",
              " | | ",
              " | | ",
              "|___|"],
        'j': ["     _ ",
              "    | |",
              " _  | |",
              "| |_| |",
              " \\___/ "],
        'k': [" _  __",
              "| |/ /",
              "| ' / ",
              "| . \\ ",
              "|_|\\_\\"],
        'l': [" _     ",
              "| |    ",
              "| |    ",
              "| |___ ",
              "|_____|"],
        'm': [" _   _ ",
              "| | | |",
              "| |_| |",
              "|  _  |",
              "|_| |_|"],
        'n': [" _   _ ",
              "| \\ | |",
              "|  \\| |",
              "| |\\  |",
              "|_| \\_|"],
        'o': ["  ___  ",
              " / _ \\ ",
              "| | | |",
              "| |_| |",
              " \\___/ "],
        'p': [" ____  ",
              "|  _ \\ ",
              "| |_) |",
              "|  __/ ",
              "|_|    "],
        'q': ["  ___  ",
              " / _ \\ ",
              "| | | |",
              "| |_| |",
              " \\__\\_\\"],
        'r': [" ____  ",
              "|  _ \\ ",
              "| |_) |",
              "|  _ < ",
              "|_| \\_\\"],
        's': [" ____  ",
              "/ ___| ",
              "\\___ \\ ",
              " ___) |",
              "|____/ "],
        't': [" _____ ",
              "|_   _|",
              "  | |  ",
              "  | |  ",
              "  |_|  "],
        'u': [" _   _ ",
              "| | | |",
              "| | | |",
              "| |_| |",
              " \\___/ "],
        'v': ["__     __",
              "\\ \\   / /",
              " \\ \\ / / ",
              "  \\ V /  ",
              "   \\_/   "],
        'w': ["__        __",
              "\\ \\      / /",
              " \\ \\ /\\ / / ",
              "  \\ V  V /  ",
              "   \\_/\\_/   "],
        'x': ["__  __",
              "\\ \\/ /",
              " \\  / ",
              " /  \\ ",
              "/_/\\_\\"],
        'y': ["__   __",
              "\\ \\ / /",
              " \\ V / ",
              "  | |  ",
              "  |_|  "],
        'z': [" _____",
              "|__  /",
              "  / / ",
              " / /_ ",
              "/____|"]
    }

    # تحويل الحرف/الحروف إلى حالة صغيرة
    characters = [char.lower() for char in character]

    # تحويل كل حرف إلى صيغته المخصصة
    converted_characters = []
    for char in characters:
        if char == "\n":
            converted_characters.append("\n")
        elif char in alphabet:
            converted_characters.append(alphabet[char])
        else:
            converted_characters.append([""])

    # دمج الصفوف
    zipped_characters = list(zip(*converted_characters))

    
    # تحويل الصفوف المدمجة إلى سلاسل نص
    lines = [" ".join(row) for row in zipped_characters]

# دمج جميع السلاسل مع إضافة فواصل بين الأسطر لإنشاء النص النهائي
    return "\n".join(lines)
