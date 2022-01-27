import heapq


def main():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    p_k_heapq = []

    def create_first_heapq(p_list, k, p_k_heapq):
        for i in range(k):
            heapq.heappush(p_k_heapq, p_list[i])
        return p_k_heapq

    def renew_heapq(p_k_heapq, i, p_list):
        min_heapq = heapq.heappop(p_k_heapq)
        heapq.heappush(p_k_heapq, max(min_heapq, p_list[i]))
        return p_k_heapq

    def print_ans(p_k_heapq):
        x = heapq.heappop(p_k_heapq)
        heapq.heappush(p_k_heapq, x)
        ans = heapq.heappop(p_k_heapq)
        print(ans)
        heapq.heappush(p_k_heapq, ans)

    p_k_heapq = create_first_heapq(p_list, k, p_k_heapq)
    print(min(p_list[:k]))
    for i in range(k, n):
        p_k_heapq = renew_heapq(p_k_heapq, i, p_list)
        print_ans(p_k_heapq)


if __name__ == '__main__':
    main()
