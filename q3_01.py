import numpy


def get_even_squares(num_list: list[int]) -> list[int]:
    """
    返回 num_list 中所有偶數的平方值列表
    """
    return [numpy.power(num, 2) for num in num_list if num % 2 == 0]


def get_odd_cubes(num_list: list[int]) -> list[int]:
    """
    返回 num_list 中所有奇數的 3 次方值列表
    """
    return [numpy.power(num, 3) for num in num_list if num % 2 == 1]


def get_sliced_list(num_list: list[int]) -> list[int]:
    """
    返回 num_list 從第 5 個元素開始到最後一個元素(包含最後一個)的子列表
    """
    return num_list[4:]


def format_numbers(numbers: list[int]) -> list[int]:
    """
    返回一個新列表,其中每個數字都被格式化為 8 個字元的寬度,並靠右對齊
    """
    formatted_numbers = []
    for number in numbers:
        formatted_numbers.append(str(number).rjust(8))
    return formatted_numbers


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = get_even_squares(num_list)
odd_cubes = get_odd_cubes(num_list)
sliced_list = get_sliced_list(num_list)
formatted_even_squares = format_numbers(even_squares)
formatted_odd_cubes = format_numbers(odd_cubes)
formatted_sliced_list = format_numbers(sliced_list)

print(','.join(formatted_even_squares))
print(','.join(formatted_odd_cubes))
print(','.join(formatted_sliced_list))
