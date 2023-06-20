import argparse
import re
import pyttsx3
from pypdf import PdfReader

# Example call: python main.py --male -s 5 -e 5 -sp -pf "example.pdf" -sf "example.mp3"


def parse_arguments():
    parser = argparse.ArgumentParser()
    voice_group = parser.add_mutually_exclusive_group(required=True)
    voice_group.add_argument('--male', action='store_true', help='Select male voice')
    voice_group.add_argument('--female', action='store_true', help='Select female voice')

    parser.add_argument(
        "-s", "--start", type=int, default=1, required=False,
        help="""Text start (specify the page number you want the audiobook to start (1 - indexed).
             This is useful if you want to skip a book header. If not specified, the parses starts at page 1"""
    )
    parser.add_argument(
        "-e", "--end", type=int, required=False,
        help="""Text end (specify the page number you want the audiobook to end (1 - indexed).
             This is useful if you want to skip a book footer."""
    )
    parser.add_argument(
        "-pf", "--pdf_file_path", type=str, required=True,
        help="File path/name of pdf file you want converted to mp3."
    )
    parser.add_argument(
        "-sf", "--save_file_path", type=str, required=False,
        help="File path of the file you want the mp3 to be saved at."
    )
    parser.add_argument(
        '-sp', "--speak", action='store_true',
        help='Speak the audio book in addition to saving it as a file'
    )
    args = parser.parse_args()

    return args


def check_for_book_start_end_errors(book_start, book_end, page_count):
    if book_end < book_start:
        raise Exception("Error: The book end page should be greater than the book start page.")

    if book_end <= 0 or book_start <= 0:
        raise Exception("Error: Page numbers should be positive")

    if book_end > page_count or book_start > page_count:
        raise Exception("Error: Invalid page number")


def replace_newlines_in_the_middle_of_sentences(text):
    pattern = r'([^\n])\n([^\n])'
    replacement = r'\1 \2'
    result = re.sub(pattern, replacement, text)
    return result


def get_text_from_pdf(pdf_file_path, book_start, book_end):
    reader = PdfReader(pdf_file_path)
    text = ""

    if book_end is None:
        book_end = len(reader.pages)

    print(len(reader.pages))
    check_for_book_start_end_errors(book_start=book_start,
                                    book_end=book_end,
                                    page_count=len(reader.pages))

    for i, page in enumerate(reader.pages):
        page_number = i + 1
        if book_start <= page_number <= book_end:
            text += page.extract_text()

    return replace_newlines_in_the_middle_of_sentences(text)


def convert_text_to_speach(text, voice, speak, save_file_path, pdf_file_path):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  # setting up new voice rate

    voices = engine.getProperty('voices')
    if voice == "male":
        engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    else:
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    if speak:
        engine.say(text)
        engine.runAndWait()

    if save_file_path:
        path = save_file_path
    else:
        path = pdf_file_path.replace(".pdf", ".mp3")

    engine.save_to_file(text, path)
    engine.runAndWait()
    print(f"MP3 file saved as: {path}")


def main():
    args = parse_arguments()
    print(args)

    if args.male:
        voice = "male"
    else:
        voice = 'female'

    text = get_text_from_pdf(pdf_file_path=args.pdf_file_path,
                             book_start=args.start,
                             book_end=args.end)
    convert_text_to_speach(text=text,
                           voice=voice,
                           speak=args.speak,
                           save_file_path=args.save_file_path,
                           pdf_file_path=args.pdf_file_path)


if __name__ == "__main__":
    main()
