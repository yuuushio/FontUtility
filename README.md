# FontUtility

A Python tool that converts font files between various formats, and renames them [by editing the internal table] according to custom specifications. It allows batch processing of fonts listed in a text file and includes functions to retrieve the actual font name for verification.

Essentially a pipeline to refine a garbage [cURL'd] font file. Better than loading each font separately in FontForge and changing the name in the table.

Issues/TODO:

- There's a separate table entry for the name displayed on Mac...
- TODO: auto-clean up after the process is complete. At the moment, I have to remove things manually.
- Script to auto generate test files given the font files, and a given preview. I.e., generate the HTML and CSS content itself (which could be done since there's a lot of repetition).
