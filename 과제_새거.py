def end_zeros(num: int) -> int:
    # 여기에 코드를 작성하세요.

    return

if __name__=='__main__':
    print("예시:")
    print(end_zeros(0))

    assert end_zeros(0) ==1
    assert end_zeros(1) ==0
    assert end_zeros(10) ==1
    assert end_zeros(101) ==0
    assert end_zeros(245) ==0
    assert end_zeros(100100) ==2
    assert end_zeros(100021300) ==2
    print("성공!!! 수고했습니다.")