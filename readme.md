# PDF to Text Converter

This Python script allows you to extract text from a PDF file and write it into a text file. It uses the PyPDF2 library to read the PDF and extract the text.

## Requirements

The script requires Python 3.6 or later and the PyPDF2 library. You can install PyPDF2 with pip:

```sh
pip install PyPDF2
```

## Usage

To use the script, run the following command:

```sh
python pdf_reader.py path_to_your_pdf_file.pdf
```

Replace `path_to_your_pdf_file.pdf` with the path to the PDF file from which you want to extract text. The script will create a text file named `my_file.txt` in the same directory as the script, containing the extracted text.

## Example

Here is an example of how to use the script:

```sh
python pdf_reader.py .\Downloads\Example.pdf
```

This command will extract text from `Example.pdf` in the `Downloads` directory and write the text to `my_file.txt`.

## Limitations

Please note that PyPDF2 can have problems with extracting text from PDF files that use complex layouts or non-standard fonts. If you encounter such issues, you may want to consider using a more robust library, such as PDFMiner or PyMuPDF.

## License

This project is licensed under the terms of the MIT license.