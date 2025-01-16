# from bisect import bisect_left

# def main(n, k, a, b):
#     # b をソート
#     b.sort()
    
#     ans = False
#     for i in range(n):
#         # K - a[i] に対応する b の要素を探す
#         target = k - a[i]
#         idx = bisect_left(b, target)
#         # idxが範囲内、かつ b[idx] が target と等しいか判定
#         if idx < len(b) and b[idx] == target:
#             ans = True
#             break
    
#     print(ans)

# if __name__ == "__main__":
#     n, k = 3, 14
#     a = [8, 5, 4]
#     b = [4, 1, 9]
#     main(n, k, a, b)    

def has_pair_with_sum(a:list, b:list, k:int) -> bool:
    """
    a の要素を連想配列 (辞書) で管理し、b の各要素について K - b[i] が存在するか判定する。

    Parameters:
    a (list): 整数 N 個のリスト
    b (list): 整数 N 個のリスト
    K (int): 目標となる合計値

    Returns:
    bool: K - b[i] を満たす a の要素が存在すれば True, そうでなければ False
    """
    # 連想配列 (辞書) D を作成し、a の要素をキー、値を True にする (O(N))
    d = {num: True for num in a}
    # b の各要素について K - b[i] が D に存在するかチェック (O(N))
    for num in b:
        if (k - num) in d:
            return True
    return False

if __name__ == "__main__":
    a = [1, 3, 5, 7, 9]  # N 個の整数
    b = [2, 4, 6, 8, 10] # N 個の整数
    K = 3  # 目標の合計値

    result = has_pair_with_sum(a, b, K)
    print(result) 