from fontTools.ttLib import TTFont
from fontTools.varLib.models import main


# Get the list of fonts. This uses their file name, not their actual font name.
def get_fonts():
    with open("fonts.txt", "r") as f:
        lines = f.readlines()

    lines = [n.strip("\n") for n in lines]
    return lines


class FontName:
    """
    Class containing functions used to fetch the [actual] name of the
    font as defined in their font table--the name that's displayed
    when you load it into a word processing application.
    """

    def __init__(self) -> None:
        pass

    # There are times when the downloaded font has a garbage name (to prevent commercial use),
    #  so this function whether to see if it does.
    def get_font_name(self, font_file_path):
        font = TTFont(font_file_path)
        font_name = self._get_name_utility(font)

        print(f"The font's actual name is: {font_name}")

    # This will be used to confirm whether our font renaming was successful or not.
    def confirm_font_renames(self, font_type):
        for f in get_fonts():
            font = TTFont(f"generated_fonts/{f}.{font_type}")
            font_name = self._get_name_utility(font)

            print(f"The font's actual name is: {font_name}")

    def _get_name_utility(self, ttfont_name):
        # Load the font
        # The 'name' table contains various strings, including the font name
        name_table = ttfont_name["name"]

        # Iterate over the name records
        # nameID 4 is usually the full font name; 1 is the font family name
        # Platform ID 3 and Encoding ID 1 specify Windows Unicode
        # Language ID 1033 is US English
        font_name = ""
        for record in name_table.names:
            if record.nameID == 4 and record.platformID == 3 and record.langID == 1033:
                # Decode byte string to Python string and remove any binary zeros
                font_name = record.string.decode("utf-16-be").rstrip("\0")
                break

        return font_name


def main():
    print("hi")


if __name__ == "__main__":
    main()
