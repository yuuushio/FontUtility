# FontUtility

A Python tool that converts font files between various formats, and renames them [by editing the internal table] according to custom specifications. It allows batch processing of fonts listed in a text file and includes functions to retrieve the actual font name for verification.

Essentially a pipeline to refine a garbage [cURL'd] font file. Better than loading each font separately in FontForge and changing the name in the table.

## Usage

Have the font files (`.woff2`, etc.) in the local folder.

The format should be dash separated in the form of:

`<fontname>-<type>`

e.g., `OpenSans-regular.woff2`

Run the font info file to clear some default records from the internal table:

```
python font_info.py
```

Supply the new font name inside `main.py` (this will be the Font Family, as well as the new file name), and then run the `main.py` file:

```
python main.py
```

## Attributes

There are a few attributes in the font table. Some of these will be cryptic, and it will be up to you to re-set them.

- `Filename` (id: ...): the name of the file.
- `Font Family` (id: 1): General name of the font family to which this font belongs to.
- `Font subfamily` (id: 2): The style/weight variation of the font within the family (e.g., Bold, Italic, Bold Italic, etc.)
- `Unique identifier` (id: 3): -
- `Font name` (id: 4) Full name of the font (family+subfamily)
- `Typographic family name` (id: ...): Similar to font family but specifically used in typography settings/context. Used in professional typesettings and design application.
- `Typographic subfamily name` (id: ...): Describes the subfamily in a typographic context.

## Troubleshooting

- Download using `curl`, but remove the `if-modified-since` header/line.

- If `curl` isn't working, use `wget`---the following headers/options need to be present otherwise you'll get an invalid file:
  - `--user-agent`
  - `--referer`

Issues/TODO:

- There's a separate table entry for the name displayed on Mac...
- TODO: auto-clean up after the process is complete. At the moment, I have to remove things manually.
- Script to auto generate test files given the font files, and a given preview. I.e., generate the HTML and CSS content itself (which could be done since there's a lot of repetition).
