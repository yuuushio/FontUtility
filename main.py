import argparse
from pathlib import Path

from fontTools.misc.textTools import string
from fontTools.ttLib import TTFont
from fontTools.varLib.models import main


def get_and_fix_names(file_type):
    font_file_names = [
        f.name
        for f in Path(".").iterdir()
        if f.is_file() and f.suffix == f".{file_type}"
    ]
    new_fl = []
    for f in font_file_names:
        f = f.replace("-", " ")
        f = f.replace("_", " ")
        f = f.removesuffix(f".{file_type}")
        f = f.title()
        f = f + "\n"
        new_fl.append(f)

    print("font file names::", font_file_names)
    print("cleaned names::", new_fl)
    return new_fl


# input: file-type of the file without the `.`
def write_names(file_type):
    font_file_names = get_and_fix_names(file_type)
    with open("fonts.txt", "w") as f:
        f.writelines(font_file_names)

    f.close()


# Rule:
#  The font file should be in the form of: {font-family}-{subfamily1}-{subfamily2}.type
#   E.g., if it's something like `GTPressura-Mono-Bold-Italic`, \
#   it should be renamed to `GTPressuraMono-Bold-Italic`


def subfamily_name(font):
    pass


def set_font_names(font, f_name, sub_f_name):

    # To change the name for all platforms, because each platforms seems to have their own name table.
    platforms = [
        (3, 1, 0x409),  # Windows, Unicode BMP, English - United States
        (1, 0, 0),  # Mac, Roman, English
        (0, 3, 0x409),  # Unicode, Default, English - United States (Linux)
    ]

    name_table = font["name"]

    # a: platform_id
    # b: platform_encoding_id
    # c: language_id

    for a, b, c in platforms:
        # 1 for 'famiily name'
        name_table.setName(f_name, 1, a, b, c)

        # 2 for 'subfamily name'
        name_table.setName(sub_f_name, 2, a, b, c)

        # 4 for 'full font name'
        name_table.setName(f"{f_name} {sub_f_name}", 4, a, b, c)


def pipeline(operations):
    if operations[0]:
        get_and_fix_names("woff2")
    if operations[1]:
        write_names("woff2")


def main():
    pipeline([0, 1])


if __name__ == "__main__":
    main()
