# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()  # O(N log N)
# b.sort()  # O(M log M)

# N = len(a)
# M = len(b)

# i, j = 0, 0
# cnt = 0

# while i < N and j < M:  # O(N + M)
#     if a[i] == b[j]:  # 共通要素を見つけた場合
#         cnt += 1
#         i += 1
#         j += 1
#     elif a[i] < b[j]:  # a[i] が小さい場合は i を進める
#         i += 1
#     else:              # b[j] が小さい場合は j を進める
#         j += 1

# print(cnt)

##解答例
def count_common_elements(a:list, b:list) -> int:
    """
    a, b のリストの共通する整数の個数をカウントする。
    
    Parameters:
    a (list): 相異なる整数 N 個のリスト
    b (list): 整数 M 個のリスト

    Returns:
    int: a と b に共通する整数の個数
    """
    # ハッシュテーブル (set) を作成
    n = set(a)
    
    counter = 0
    # b の各要素が H に含まれるかをチェック
    for num in b:
        if num in n:
            counter += 1
    return counter

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    result = count_common_elements(a, b)
    print(result)