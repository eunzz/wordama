from utils import read_words_from_db, write_db, count_remaining_words

EXCEL_FILE_PATH = "absolutely_essential_words_504.xls"

if __name__ == "__main__":
    words = read_words_from_db(EXCEL_FILE_PATH)
    remaining_words_num = count_remaining_words(words)
    while remaining_words_num != 0:
        for word in words:
            if not word.is_checked:
                word.check_answer()
        remaining_words_num = count_remaining_words(words)
        print(f"remaining: {remaining_words_num}")
    print("Completed!")
    write_db(EXCEL_FILE_PATH, words)
