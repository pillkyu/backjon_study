def number_to_korean(number: int) -> str:
    units = ["", "만", "억", "조"]  # 한국어 단위
    digits = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]  # 숫자 -> 한글 변환

    # 1. 숫자를 네 자리씩 끊기
    chunks = []
    while number > 0:
        chunks.append(number % 10000)
        number //= 10000

    # 2. 네 자리씩 처리
    korean_number = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue
        part = []
        if chunk >= 1000:
            part.append(digits[chunk // 1000] + "천")
            chunk %= 1000
        if chunk >= 100:
            part.append(digits[chunk // 100] + "백")
            chunk %= 100
        if chunk >= 10:
            part.append(digits[chunk // 10] + "십")
            chunk %= 10
        if chunk > 0:
            part.append(digits[chunk])
        korean_number.append("".join(part) + units[i])

    # 3. 순서를 뒤집어 조 -> 억 -> 만 -> 기본단위 순서로 합치기
    return " ".join(reversed(korean_number))


# 사용자 입력 처리
def main():
    # 금액 입력 예시
    amount = input().strip()

    # 1. 입력값에서 콤마와 '원' 제거

    numeric_value = int(amount.replace(",", "").replace("원", ""))

    # 2. 변환
    result = number_to_korean(numeric_value)

    # 3. 결과 출력
    print(f"입력한 금액: {amount}")
    print(f"한글로 읽기: {result} 원")


if __name__ == "__main__":
    main()
