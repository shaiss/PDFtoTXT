import PyPDF2
import sys

def main(pdf_file_name):

    # Open the PDF file
    with open(pdf_file_name, "rb") as pdf_file:

        # Create a PDF reader object
        reader = PyPDF2.PdfReader(pdf_file)

        # Get the number of pages in the PDF file
        num_pages = len(reader.pages)

        # Create an empty list to store the text from each page
        text_list = []

        # Iterate over the pages in the PDF file
        for i in range(num_pages):

            # Get the text from the current page
            page_text = reader.pages[i].extract_text()

            # Add the text to the list
            text_list.append(page_text)

        # Write the text to a TXT file
        with open("my_file.txt", "w") as f:
            for text in text_list:
                f.write(text + "\n")

if __name__ == "__main__":

    # Get the file name from the command line
    pdf_file_name = sys.argv[1]

    # Call the main function
    main(pdf_file_name)
