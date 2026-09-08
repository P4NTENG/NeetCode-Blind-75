def solution(citations):
    h = 0
    citations = sorted(citations)
    for index, citation in enumerate(reversed(citations)):
        if citation >= index + 1:
            h += 1
    return h


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))
    citations = [10, 20, 30]
    print(solution(citations))
    citations = [0, 0, 4, 4]
    print(solution(citations))
