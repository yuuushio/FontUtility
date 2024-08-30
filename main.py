import argparse
from pathlib import Path

from fontTools.misc.textTools import string
from fontTools.ttLib import TTFont
from fontTools.varLib.models import main


# Generate font files
def get_file_names(file_type):
    for f in Path(".").iterdir():
        if f.is_file() and f.suffix == f".{file_type}":
            yield f


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
    """
    Split the font name into family name and sub-family name
    """
    pf = font.partition(" ")
    fam_name = pf[0]
    sub_f_name = gen_sub_f_name(pf[2])
    return fam_name, sub_f_name


def get_and_fix_names(f_file):
    # f_file is a of <PosixPath> type; need to get the explicit name (string)
    f = f_file.name
    f = f.replace("-", " ")
    f = f.replace("_", " ")
    f = f.removesuffix(f_file.suffix)
    f = f.title()
    return f


def _test_gen_names(file_type):
    for f in get_file_names(file_type):
        cleaned_name = get_and_fix_names(f)
        print(cleaned_name, gen_names(cleaned_name))


# [Bug]: this won't work after the change since we removed iteration of fonts get_and_fix_names
# input: file-type of the file without the `.`
def write_names(file_type):
    with open("fonts.txt", "w") as f:
        pass
        # f.writelines([f"{font_name}\n" for font_name in get_and_fix_names(file_type)])
    print("Result written to file - fonts.txt")
    f.close()


def ensure_directories_exist(*dir_paths):
    for dir in dir_paths:
        if not dir.exists():
            dir.mkdir(parents=True, exist_ok=True)


def set_output_dirs(f_name, op_types):
    dir_dict = {}
    for fmt in op_types:
        dir = Path(f"./{f_name}/{fmt}")
        dir_dict[fmt] = dir

    ensure_directories_exist(*dir_dict.values())
    return dir_dict


def save_fonts(font, dir_dict, ffn):
    for fmt, pth in dir_dict.items():
        font.flavor = None if fmt == "ttf" else fmt
        font.save(f"{pth}/{ffn}.{fmt}")


def set_font_names(font, f_name, sub_f_name, custom_f_name):

    # To change the name for all platforms, because each platforms seems to have their own name table.
    platforms = [
        (3, 1, 0x409),  # Windows, Unicode BMP, English - United States
        (1, 0, 0),  # Mac, Roman, English
        (0, 3, 0x409),  # Unicode, Default, English - United States (Linux)
    ]

    name_table = font["name"]

    print(custom_f_name[0], custom_f_name[1])
    if custom_f_name[0]:
        f_name = custom_f_name[1]

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

        # 6 for postscript name
        name_table.setName(f"{f_name}_{sub_f_name}".lower(), 6, a, b, c)


def get_final_name(cn):
    return cn.replace(" ", "_").lower()


def validate_custom_name(cn):
    print("Validating custom name...")
    if isinstance(cn, str) and cn.strip():
        print("Valid name supplied.")
        return True
    else:
        print("Invalid custom name; falling back to default.")
        return False


"""
This is still better than turning it into a class and doing smt like
pl.get_and_fix_names()
pl.write_names()
[...]
This would involve a whole lot of uncommenting and recommenting; and having more
layers of classes will just make things annoying and hard to read.
This type of pipeline needn't run in order - you can call different functions
simultaneously which can be independant of each other; and switching
the operations to 1/0 for whichever function you want (/dont want) to
run is just so much easier.
"""


def batch_process_fonts(initial_type, op_types, custom_output_name):
    for f in get_file_names(initial_type):
        cleaned_name = get_and_fix_names(f)
        f_name, sub_f_name = gen_names(cleaned_name)
        dir_dict = set_output_dirs(f_name, op_types)

        font = TTFont(f)
        set_font_names(font, f_name, sub_f_name, custom_output_name)

        if validate_custom_name(custom_output_name[1]):
            final_file_name = get_final_name(
                " ".join((custom_output_name[1].strip(), sub_f_name))
            )
        else:
            final_file_name = get_final_name(cleaned_name)

        save_fonts(font, dir_dict, final_file_name)
        font.close()


def pipeline(operations, initial_type, output_types, custom_output_name):
    if operations[0]:
        get_and_fix_names(initial_type)  # ! Won't work now -- removed for loop
    if operations[1]:
        write_names(initial_type)  # ! Won't work now
    if operations[2]:
        _test_gen_names(initial_type)
    if operations[3]:
        batch_process_fonts(initial_type, output_types, custom_output_name)


def main():
    # Set to true if you would like to pass in a custom name
    custom_output_name = [True, "FabrikatMono"]
    pipeline([0, 0, 0, 1], "woff2", ["ttf", "woff2"], custom_output_name)


if __name__ == "__main__":
    main()
