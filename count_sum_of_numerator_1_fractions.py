# 分子が1の分数をn個合計して1になる組み合わせの数を数える。
import math

def euclidean(m, n):
    if n > m:
        (m,n) = (n,m)
    if n == 0:
        return m
    else:
        return euclidean(n, m % n)


# q/pをm個の分数で合計する組み合わせの数を数える関数
def count_fractions(q, p, m, prev_r, memo):
    count = 0
    if m == 1:
        if q == 1:
            return 1, memo
        else:
            return 0, memo
    
    # q/pを超えない1/rを満足するrの最小値を求める
    r_min = max(math.ceil(p/q), prev_r)
    r_max = math.floor(2*p*(m-1)/q)

    # q/pから1/rを引いた残りが1/r*(m-1)より大きいと、rが大きすぎるのでNG
    # 1/r*(m-1) >= q/p - 1/r
    r = r_max
    while r >= r_min:
        next_q, next_p = q*r-p, p*r
        if next_q > 0:
            e = euclidean(next_q,next_p)
            next_q, next_p = int(next_q/e), int(next_p/e)
            if (next_q,next_p,m-1,r) in memo:
                c = memo[(next_q,next_p,m-1,r)]
                # print(f'hit!:({next_q},{next_p},{m},{r})={c}')
            else:
                c, memo = count_fractions(next_q, next_p, m-1, r, memo)
            count = count + c
        r = r - 1

    memo[(q,p,m,prev_r)] = count
    return count, memo

if __name__=='__main__':
    n = 6
    memo = dict()
    c, _ = count_fractions(1,1,n,1,memo)
    print(c)

