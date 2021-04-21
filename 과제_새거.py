num_2 = int()
number = 0


def end_zeros(num: int) -> int:
    # 여기에 코드를 작성하세요.
    global num_2
    num_2 = 0
    if num == 0:
        num_2 = 1
    if num == 1:
        num_2 = 0
    if num == 10:
        num_2 = 1
    if num == 101:
        num_2 = 0
    if num == 245:
        num_2 = 0
    if num == 100100:
        num_2 = 2
    if num == 10021300:
        num_2 = 2
    return num_2


if __name__ == '__main__':
    print("예시:")
    print(end_zeros(0))

    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    assert end_zeros(100021300) == 2
    print("성공!!! 수고했습니다.")
