import os
import PyPDF2

def main():
    '''Merge multiple pdfs into one'''

    '''
       Some PDF documents have an encryption feature that will keep them from being read until whoever is opening the document provides a password.
       To read an encrypted PDF, call the decrypt() function and pass the password as a string.
       If given the wrong password, the decrypt() function will return 0 and getPage() will continue to fail.
       Note that the decrypt() method decrypts only the PdfFileReader object, not the actual PDF file.
       After your program terminates, the file on your hard drive remains encrypted. Your program will have to call decrypt() again the next time it is run.
        
    '''

    print("Enter the location of PDF's on your device.\n Enter '.' if pdfs are in the current directory:")
    os.chdir(input())

    print("Enter the number of pdf's to merge :)")
    num_docs = int(input())

    #create an array of filenames
    pdf_names = []
    for i in range(num_docs):
        print("PDF Name {}?".format(i+1))
        pdf_names.append(input())

    writer = PyPDF2.PdfFileWriter()

    # append files together
    i = 0
    file_names = []
    while i < num_docs:
        open_pdf = open(pdf_names[i], "rb")
        pdf = PyPDF2.PdfFileReader(open_pdf)

        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            writer.addPage(page)

        file_names.append(open_pdf)
        i += 1

    # create new pdf
    print("Enter new file name:")
    new_pdf = input()
    new_pdf += ".pdf"

    output_file = open(new_pdf, "wb")
    writer.write(output_file)

    # close files
    output_file.close()
    close_files(file_names)


def close_files(file_names):
    '''close all opened files'''
    for f in file_names:
        f.close()

if __name__ == "__main__":
    main()
