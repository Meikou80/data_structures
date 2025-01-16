from bisect import bisect_left

def main(n, k, a, b):
    INF = 20000000
    min_value = INF
    
    # a, b をリストに変換してソート
    a = list(a)
    b = list(b)
    
    # b をソート
    b.sort()
    # b に無限大を表す値 (INF) を追加
    b.append(INF)
    
    # a を固定して解く
    for i in range(n):
        # b の中で K - a[i] 以上の範囲での最小値を探す
        idx = bisect_left(b, k - a[i])
        val = b[idx]
        # min_value と比較する
        if a[i] + val < min_value:
            min_value = a[i] + val
    
    print(min_value)

if __name__ == "__main__":
    n, k = 3, 10
    a = (8, 5, 4)
    b = (4, 1, 9)
    main(n, k, a, b)