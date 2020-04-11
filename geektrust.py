# All kingdoms with animal emblem
kingdoms = [{"LAND": "PANDA"}, {"SPACE": "GORILLA"}, {"WATER": "OCTOPUS"}, {"ICE": "MAMMOTH"}, {"AIR": "OWL"},
            {"FIRE": "DRAGON"}]


def get_key(val):
    """ Retrives key from dictionary by value """
    for kingdom in kingdoms:
        for kingdom_name, value in kingdom.items():
            if val == value:
                return kingdom_name


if __name__ == '__main__':
    ruling_kingdom = "SPACE"

    king_dict = {}
    decrypted_array = []
    final_array = []

    try:
        with open("input.txt") as f:
            for line in f:
                # reads file line by line and stores values as key-value pair dict
                key_value = line.split('\n')[0].split(" ")
                king_dict.__setitem__(key_value[0], str(key_value[1:]))
    except FileNotFoundError:
        print("File not found")

    for input_key in king_dict.keys():
        # matches every key with all available kingdom key-values
        for kingdom_key in kingdoms:
            if input_key in kingdom_key:  # if input key present in  kingdoms
                shift = len(kingdom_key[input_key])  # calculates shift value for Ceaser encryption
                text = king_dict[input_key].replace(" ", "")  # removes blank spaces from text if any
                result = ""
                option = 2  # specifies encryption/decryption ,
                # modifies shift value according that,default 2 i .e decryption

                if option == 2:  # modifies shift value by subtracting it with total number of alphabets (reverse)
                    shift = 26 - shift

                for character in range(len(text)):  # iterates string to find ASCI value of each character
                    char = text[character]

                    # calculates decrypted ASCI values of each character , appends to result string
                    if char.isupper():  # if character is uppercase
                        result += chr((ord(char) + shift - 65) % 26 + 65)
                    else:
                        result += chr((ord(char) + shift - 97) % 26 + 97)

                decrypted_array.append(result)
                result_array = [c for c in result]  # converts string to array
                final_result = ""

                for char in kingdom_key[input_key]:

                    # if character is present in result array and kingdom keys ,
                    # removes the character from result array and appends to string
                    if char in result_array:
                        final_result += char
                        result_array.remove(char)
                final_array.append(final_result)

    output_arr = []
    for i in final_array:
        if i:
            key = get_key(i)
            if key:
                output_arr.append(key)

    if len(output_arr) > 2:
        output_str = ' '.join(map(str, output_arr))

        if output_str:
            print(ruling_kingdom + " " + output_str)  # output with ruling kingdom (SPACE)
    else:
        print(None)  # prints None if matching kingdom count < 3
