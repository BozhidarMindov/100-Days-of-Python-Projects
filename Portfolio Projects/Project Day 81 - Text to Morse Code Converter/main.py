#No imports needed

def main():
    #morse code dictionary with all possible letters and symbols
    #found the values online
    morse_letter_dict = {'A': '.-', 'B': '-...',
                        'C': '-.-.', 'D': '-..', 'E': '.',
                        'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-',
                        'L': '.-..', 'M': '--', 'N': '-.',
                        'O': '---', 'P': '.--.', 'Q': '--.-',
                        'R': '.-.', 'S': '...', 'T': '-',
                        'U': '..-', 'V': '...-', 'W': '.--',
                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
                        '1': '.----', '2': '..---', '3': '...--',
                        '4': '....-', '5': '.....', '6': '-....',
                        '7': '--...', '8': '---..', '9': '----.',
                        '0': '-----', ', ': '--..--', '.': '.-.-.-',
                        '?': '..--..', '/': '-..-.', '-': '-....-',
                        '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                         ':': '---...', '&': '.-...', '=': '-...-',
                         '@': '.--.-.'
                       }

    #getting user input
    user_input = input("Enter a string to be converted to Morse Code: ").upper()

    #converting the user input to morse code
    morse_message = str()
    for letter in user_input:
        if letter in morse_letter_dict:
            morse_message += morse_letter_dict[letter] + " "
        else:
            morse_message += " "

    #displaying the morse code message
    print(f"The message in Morse Code is: \n {morse_message}")



if __name__ == "__main__":
    main()