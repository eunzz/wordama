from typing import List

import xlrd

from data import Word


def read_words_from_db(excel_file_path: str) -> List[Word]:
    words = []
    wb = xlrd.open_workbook(excel_file_path)
    # TODO: should be able to select sheet_num
    sheet = wb.sheet_by_index(0)
    for row_num in range(0, sheet.nrows):
        if row_num == 0:
            continue
        word = Word(
            word=sheet.cell_value(row_num, 0),
            meaning=sheet.cell_value(row_num, 1),
            wrong_nums=sheet.cell_value(row_num, 2),
        )
        words.append(word)
    return words


def sync_db(excel_file_path: str, words: List[Word]):
    # TODO: Not implemented
    pass


def count_remaining_words(words: List[Word]) -> int:
    count = 0
    for word in words:
        if not word.is_checked:
            count += 1
    return count
