from fontTools.ttLib import TTFont
from pathlib import Path

"""
Name ID 0: Copyright notice.
Name ID 1: Font Family name.
Name ID 3: Unique font identifier.
Name ID 8: Manufacturer name.
Name ID 9: Designer name.
Name ID 11: URL of the vendor.
Name ID 13: License description.
Name ID 14: License information URL.
"""


def get_font_list():

    # Get the list of .woff2 files in the current directory
    return [f.name for f in Path('.').iterdir() if f.is_file() and f.suffix == '.woff2']

def rm_id_of_font(font_name):
    font = TTFont(font_name)
    # Access the 'name' table
    name_table = font['name']

    # List to keep track of records to remove
    records_to_remove = []


    # Collect the records to remove
    for record in name_table.names:

        print(record.nameID, record.toStr())
        if record.nameID in [0, 8, 9, 11, 13, 10, 12, 14]:
            records_to_remove.append(record)

    # Remove the collected records
    for record in records_to_remove:
        name_table.names.remove(record)

    font.save(font_name)


def run_removal(font_list):
    for font in font_list:
        rm_id_of_font(font)

def run_pipeline(options_list):
    fl = get_font_list()
    if options_list[0]:
        print(fl)
    if options_list[1]:
        run_removal(fl)


def main():
    run_pipeline([1,1])

if __name__ == "__main__":
    main()
