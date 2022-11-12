"""def函数示例"""


def count_list(source_list: list):
    """
    count
    :param source_list:
    :return:
    """
    result = len(source_list)
    return result


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """ask_ok"""
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
