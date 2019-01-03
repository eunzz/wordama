from utils import read_words_from_db, write_db, count_remaining_words

EXCEL_FILE_PATH = "absolutely_essential_words_504.xls"


def run_test(day_index: int, file_path: str):
    words = read_words_from_db(file_path, day_index)
    remaining_words_num = count_remaining_words(words)
    while remaining_words_num != 0:
        for word in words:
            if not word.is_checked:
                word.check_answer()
        remaining_words_num = count_remaining_words(words)
        print(f"remaining: {remaining_words_num}")
    print("Completed!")
    write_db(file_path, day_index, words)


if __name__ == "__main__":
    day_idx = int(input("which day do you want to test? (start by 0)"))
    run_test(day_idx, EXCEL_FILE_PATH)

