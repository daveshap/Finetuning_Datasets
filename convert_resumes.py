import pypandoc
import os
import PyPDF2 
import tika
import pdfplumber


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def convert_docx2txt(src_dir, dest_dir):
    files = os.listdir(src_dir)
    files = [i for i in files if '.docx' in i]
    for file in files:
        try:
            pypandoc.convert_file(src_dir+file, 'plain', outputfile=dest_dir+file.replace('.docx','.txt'))
        except Exception as oops:
            print(oops, file)
            


def convert_pdf2txt(src_dir, dest_dir):
    files = os.listdir(src_dir)
    files = [i for i in files if '.pdf' in i]
    for file in files:
        try:
            with pdfplumber.open(src_dir+file) as pdf:
                output = ''
                for page in pdf.pages:
                    output += page.extract_text()
                    output += '\n'
                save_file(dest_dir+file.replace('.pdf','.txt'), output.strip())
        except Exception as oops:
            print(oops, file)




if __name__ == '__main__':
    #convert_docx2txt('resumes/', 'converted/')
    convert_pdf2txt('resumes/', 'converted/')