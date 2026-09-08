def solution(sequence, k):
    answer = [0, float("inf")]

    start = 0
    partial_sum = 0
    for end, end_val in enumerate(sequence):
        if end_val > k:
            break
        partial_sum += end_val
        while partial_sum > k:
            partial_sum -= sequence[start]
            start += 1
        if partial_sum == k and answer[1] - answer[0] > end - start:
            answer = [start, end]
            if end - start == 0:
                break

    return answer


if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 5]
    k = 7
    print(solution(sequence, k))

    sequence = [2, 2, 2, 2, 2]
    k = 6
    print(solution(sequence, k))

    sequence = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    print(solution(sequence, k))
