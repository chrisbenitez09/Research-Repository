'''The purpose of this game is just to practice the basics of Python, this is going to be a quiz game about Computer components.'''

def main():
    print("Welcome to The Computer Quiz Game, let's learn something!!! ")
    user = input("Are you ready to play? ")
    score = 0

    '''the .lower() method returns the lowercase string from the given string, it converts all uppercase character to lowercase.'''
    '''In this case if the player say yes it will play, otherwise the game will never start. '''
    '''!= not equal to '''
    if user.lower() != "yes":
        quit()

    print("Alright let's play!!! ")

    user = input("What is BIOS? ")
    if user == "Basic Input Output Services".lower():
        print("That's Correct ! The BIOS is your PC's most important startup program, BIOS, or Basic Input/Output System, is the built-in core processor software responsible for booting up your system. Typically embedded into your computer as a motherboard chip, the BIOS functions as a catalyst for PC functionality action.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is CD? ")
    if user == "Compact Disc".lower():
        print("That's Correct! CD is a type of optical media, so-called because it uses light to read the data stored on the disk.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is CPU? ")
    if user == "Central Processing Unit".lower():
        print("That's Correct!  The CPU is the electronic circuitry that executes instructions comprising a computer program. The CPU performs basic arithmetic, logic, controlling, and input/output (I/O) operations specified by the instructions in the program.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is HDD? ")
    if user == " Hard Disk Drive".lower():
        print("That's Correct! HDD is an array of magnetic disks that store data until it is intentionally deleted by the user, the system, or a program.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is HDMI? ")
    if user == "High Definition Multimedia Interface".lower():
        print("That's Correct! HDMI is a digital standard for transmitting high-definition video and audio using a single cable. HDMI is rapidly becoming the standard interface for computers and home entertainment devices.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is PSU? ")
    if user == "Power supply unit".lower():
        print("That's Correct! The purpose of the PSU is to supply power to all of your PC components.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is RAM? ")
    if user == "Random Access Memory".lower():
        print("That's Correct! RAM is memory that's writable by the system and by programs, that stores information while it is needed for running the system and for the execution of programs.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is SSD? ")
    if user == "Solid State Drive".lower():
        print("That's Correct! SSD is a mass-storage device with no moving parts, which stores data in arrays of flash memory.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    user = input("What is PSU? ")
    if user == "Power supply unit".lower():
        print("That's Correct! The purpose of the PSU is to supply power to all of your PC components.")
        score += 1
        score = score + 1
    else:
        print("Incorrect! ")

    print("Your score is " + str(score))

    '''main() will take me again to the beginning of the quiz'''
    user = input("Do you want to try again? Y/N : ")
    if user == "Y".lower():
        main()
    else:
        quit()
main()