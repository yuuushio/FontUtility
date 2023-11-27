from fontTools.ttLib import TTFont
from fontTools.varLib.models import main


# Get the list of fonts. This uses their file name, not their actual font name.
def get_fonts():
    with open("fonts.txt", "r") as f:
        lines = f.readlines()

    lines = [n.strip("\n") for n in lines]
    return lines


def main():
    print("hi")


if __name__ == "__main__":
    main()
