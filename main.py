import argparse
from pathlib import Path

from fontTools.misc.textTools import string
from fontTools.ttLib import TTFont
from fontTools.varLib.models import main


# Generate font files
def get_file_names(file_type):
    for f in Path(".").iterdir():
        if f.is_file() and f.suffix == f".{file_type}":
            yield f.name


def gen_sub_f_name(secnd_partition):
    lc = secnd_partition.lower()
    # It just makes sense to have the logic like this (from reading perspective)
    if "regular" in lc:
        if "italic" in lc:
            return "italic".title()
        else:
            return "regular".title()
    else:
        return secnd_partition


# Rule:
#  The font file should be in the form of: {font-family}-{subfamily1}-{subfamily2}.type
#   E.g., if it's something like `GTPressura-Mono-Bold-Italic`, \
#   it should be renamed to `GTPressuraMono-Bold-Italic`


def gen_names(font):
    pf = font.partition(" ")
    fam_name = pf[0]
    sub_f_name = gen_sub_f_name(pf[2])
    return fam_name, sub_f_name


def get_and_fix_names(file_type):
    # new_fl = []
    for f in get_file_names(file_type):
        f = f.replace("-", " ")
        f = f.replace("_", " ")
        f = f.removesuffix(f".{file_type}")
        f = f.title()
        # f = f + "\n"
        yield f

    # print("font file names::", font_file_names)
    # print("cleaned names::", new_fl)
    # return new_fl


def _test_gen_names():
    for f in get_and_fix_names("woff2"):
        print(gen_names(f))


# input: file-type of the file without the `.`
def write_names(file_type):
    font_file_names = get_and_fix_names(file_type)
    with open("fonts.txt", "w") as f:
        f.writelines([f"{font_name}\n" for font_name in get_and_fix_names(file_type)])
    print("Result written to file - fonts.txt")
    f.close()


def set_font_names(font):
    f_name, sub_f_name = gen_names(font)

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
    if operations[2]:
        _test_gen_names()


def main():
    pipeline([0, 1, 1])


if __name__ == "__main__":
    main()
