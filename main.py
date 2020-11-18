from PyPDF2 import PdfFileReader
import pyttsx3
import os

if __name__ == '__main__':
    pdf_file_path = os.path.join(os.path.dirname(__file__),
                                 'datas',
                                 'object_oriented_python_tutorial.pdf')
    en_voice_m_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

    try:
        book = open(pdf_file_path, 'rb')
        pdfReader = PdfFileReader(book)
    except Exception as e:
        print(f"pdf_reader_error: {e}")

    speaker = pyttsx3.init()
    speaker.setProperty('voice', en_voice_m_id)
    pageNumbers = pdfReader.numPages
    for pageNumber in range(6, pageNumbers):
        page = pdfReader.getPage(pageNumber)
        page_text = page.extractText()
        print(f"page_text: {page_text}")
        speaker.say(page_text)
        speaker.runAndWait()
        break

    book.close()
