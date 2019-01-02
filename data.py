class Word:
    def __init__(self, word: str, meaning: str, wrong_nums: int):
        """
        :param word: 단어
        :param meaning: 단어의 의미
        :param wrong_nums: 누적 틀린 횟수
        """
        self.word = word
        self.meaning = meaning
        self.wrong_nums = wrong_nums
        self.is_checked = False

    def check_answer(self):
        answer = input("word >")
        if answer == self.word:
            self.is_checked = True
            return True
        else:
            print(f"Wrong! Answer is {self.word}")
            self.wrong_nums += 1
            return False
