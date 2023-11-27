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

    # There are times when the downloaded font has a garbage name (to prevent commercial use),
    #  so this function whether to see if it does.
    def get_font_name(self, font_file_path):
        font = TTFont(font_file_path)
        font_name = self._get_name_utility(font)

        print(f"The font's actual name is: {font_name}")

    # This will be used to confirm whether our font renaming was successful or not.
    def confirm_font_renames(self):
        # Hard code bc they should already been in ttf as that's our desired _to_ conversion
        font_type = "ttf"
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


class FontConverter:
    def otf_to_ttf(self):
        fonts = get_fonts()
        for f in fonts:
            font = TTFont(f"{f}.otf")
            font.save(f"generated_fonts/{f}.ttf")

    def woff_to_ttf(self):
        fonts = get_fonts()
        for f in fonts:
            font = TTFont(f"{f}.woff2")
            font.save(f"generated_fonts/{f}.ttf")

    def gen_ttf(self, current_type):
        if current_type == "otf":
            self.otf_to_ttf()
        elif current_type == "woff":
            self.woff_to_ttf()
        else:
            print("Invalid font extension.")


def set_font_name(family_name, font_list, font_type):
    for f in font_list:
        # Load the already generated (converted) fonts; i.e., they are of desired font format
        font = TTFont(f"generated_fonts/{f}.{font_type}")

        name_table = font["name"]

        # Modify the names
        # The entries in the naming table are referenced by their 'nameID'
        # For example, nameID 1 is the Font Family name, and nameID 2 is the Font Subfamily name
        # You'll need to replace 'New Font Family Name' and 'New Font Subfamily Name' with your desired names
        name_table.setName(family_name, 1, 3, 1, 0x409)
        name_table.setName(f, 2, 3, 1, 0x409)
        name_table.setName(f, 4, 3, 1, 0x409)

        # Save the modified font
        font.save(f"generated_fonts/{f}.{font_type}")

        # Close the font object
        font.close()


def main():
    font_list = get_fonts()
    print(font_list)
    conv = FontConverter()
    conv.gen_ttf(current_type="woff")

    # TODO: get family_name as command line argument
    set_font_name("Adonis", font_list, "ttf")
    FontName().confirm_font_renames()


if __name__ == "__main__":
    main()
