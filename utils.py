from typing import List

import xlrd
from xlutils.copy import copy

from data import Word


def read_words_from_db(excel_file_path: str, day_index: int) -> List[Word]:
    words = []
    wb = xlrd.open_workbook(excel_file_path)
    try:
        sheet = wb.sheet_by_index(day_index)
    except IndexError:
        raise Exception("The sheet does not exist.")
    for row_num in range(0, sheet.nrows):
        if row_num == 0:
            continue
        word = Word(
            id=int(sheet.cell_value(row_num, 0)),
            word=sheet.cell_value(row_num, 1),
            meaning=sheet.cell_value(row_num, 2),
            wrong_nums=sheet.cell_value(row_num, 3),
        )
        words.append(word)
    return words


def update_db(excel_file_path: str, day_index: int, words: List[Word]):
    # ref: https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
    sorted_words = sorted(words, key=lambda w: w.id)
    # ref: https://www.blog.pythonlibrary.org/2014/03/24/creating-microsoft-excel-spreadsheets-with-python-and-xlwt/
    existing_workbook = xlrd.open_workbook(excel_file_path)
    new_wb = copy(existing_workbook)
    try:
        # 이미 존재하는 sheet를 가져와서 덮어쓴다.
        new_sheet = new_wb.get_sheet(day_index)
        new_sheet.write(0, 0, "id")
        new_sheet.write(0, 1, "word")
        new_sheet.write(0, 2, "meaning")
        new_sheet.write(0, 3, "wrong_nums")
    except IndexError:
        raise Exception("The sheet does not exist.")

    for idx, word in enumerate(sorted_words):
        new_sheet.write(idx + 1, 0, word.id)
        new_sheet.write(idx + 1, 1, word.word)
        new_sheet.write(idx + 1, 2, word.meaning)
        new_sheet.write(idx + 1, 3, word.wrong_nums)
    new_wb.save(excel_file_path)


def count_remaining_words(words: List[Word]) -> int:
    count = 0
    for word in words:
        if not word.is_checked:
            count += 1
    return count
