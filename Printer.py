def convert_to_custom_format(character):
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

  # Convert the character(s) to lowercase
  characters = [char.lower() for char in character]

  # Convert each character to its custom format
  converted_characters = []
  for char in characters:
      # Check if the character is a newline character
      if char == "\\n":
          # Add a newline to the converted characters list
          converted_characters.append("\n")
      elif char in alphabet:
          # Add the character's representation to the converted characters list
          converted_characters.append(alphabet[char])
      else:
          # Add an empty space for unsupported characters
          converted_characters.append([""])

  # Zip the converted characters lists to transpose them
  zipped_characters = list(zip(*converted_characters))

  # Join each row of characters and add a newline at the end of each row
  lines = [" ".join(row) for row in zipped_characters]

  # Join all lines with newline characters in between to create the final representation
  return "\n".join(lines)

# Ask the user to enter a string
input_string = input("Enter a string (use '\\n' for new line): ")

# Call the function with the entered string
converted_string = convert_to_custom_format(input_string)
print(converted_string)
