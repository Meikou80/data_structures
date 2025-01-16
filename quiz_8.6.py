# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# N = len(a)
# M = len(b)

# common = []
# for i in range(N):
#     for j in range(M):
#         if a[i] == b[j]:
#             common.append(a[i])
            
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# common = list(a & b)  # set の共通部分を求める: O(N + M)

from collections import Counter

def count_occurence(a:list, b:list) -> int:
    """
    a の要素の出現回数を連想配列 (辞書) で記録し、b の要素ごとに合計を計算する。

    Parameters:
    a (list): 整数 N 個のリスト
    b (list): 整数 M 個のリスト

    Returns:
    int: b 内の各要素が a に含まれる回数の合計
    """
    # # 連想配列 (辞書) D を作成
    # d = {}
    # # a の各要素の出現回数を記録 (O(N))
    # for num in a:
    #     d[num] = d.get(num, 0) + 1
    # result = 0
    # # b の各要素について d[b[j]] を result に加算 (O(M))
    # for num in b:
    #     result += d.get(num, 0)
    
    d = Counter(a)
    print(d)
    result = 0
    for num in b:
        result += d[num]
    return result

if __name__ == "__main__":
    a = [1, 3, 3, 5, 7, 9, 3, 5]
    b = [3, 5, 8, 9]
    result = count_occurence(a, b)
    print(result)