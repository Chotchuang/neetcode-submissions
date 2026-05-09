from typing import List


def sort_words(words: List[str]) -> List[str]:
    """
    เรียงลำดับคำตามความยาวของคำ (ความยาวมากไปน้อย)
    เหมือน SQL: ORDER BY LENGTH(word) DESC
    """
    words.sort(key=len, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    """
    เรียงลำดับตัวเลขตามค่าสัมบูรณ์ (Absolute Value) จากน้อยไปมาก
    เช่น [-5, 1, -2] จะกลายเป็น [1, -2, -5] เพราะ |1| < |-2| < |-5|
    เหมือน SQL: ORDER BY ABS(number) ASC
    """
    numbers.sort(key=abs)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
