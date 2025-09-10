from gtts import gTTS
import PyPDF2

pdf_file = open("C:/Users/Nagashree Bhat/Downloads/notes .pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
count = len(pdf_reader.pages)
textList = []

for i in range(count):
    try:
        page = pdf_reader.pages[i]
        text = page.extract_text()
        if text:
            textList.append(text)
    except Exception as e:
        print(f"Error on page {i}: {e}")


textString = " ".join(textList)

print(textString)
language = 'en'

myAudio = gTTS(text=textString, lang=language, slow=False)

myAudio.save("Audio.mp3")
print("Audio file saved as Audio.mp3")
