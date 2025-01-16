def main(n, k, a, b):    
    INF = 20000000
    min_value = INF
    
    # 線形探索
    for i in range(n):
        for j in range(n):
            # 和が K 未満の場合はスキップ
            if a[i] + b[j] < k:
                continue
            # 最小値を更新
            if a[i] + b[j] < min_value:
                min_value = a[i] + b[j]
    
    print(min_value)

if __name__ == "__main__":
    n, k = 3, 10
    a = (8, 5, 4)
    b = (4, 1, 9)
    main(n, k, a, b)