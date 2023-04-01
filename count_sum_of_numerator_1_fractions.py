# 分子が1の分数をn個合計して1になる組み合わせの数を数える。
import math

def euclidean(m, n):
    if n > m:
        (m,n) = (n,m)
    while n != 0:
        (m,n) = (n, m%n)
    return m


# q/pをm個の分数で合計する組み合わせの数を数える関数
def count_fractions(q, p, m, prev_r):
    count = 0
    if m == 1:
        if q == 1:
            return 1
        else:
            return 0
    else:
        # q/pを超えない1/rを満足するrの最小値を求める
        r_min = max(math.ceil(p/q), prev_r)
        r_max = math.floor(p*m/q)

        # q/pから1/rを引いた残りが1/r*(m-1)より大きいと、rが大きすぎるのでNG
        # 1/r*(m-1) >= q/p - 1/r
        r = r_max
        while r >= r_min:
            next_q, next_p = q*r-p, p*r
            if next_q > 0:
                if m == 2:
                    if next_p % next_q == 0:
                        count = count + 1
                else:
                    e = euclidean(next_q,next_p)
                    next_q, next_p = int(next_q/e), int(next_p/e)
                    c = count_fractions(next_q, next_p, m-1, r)
                    count = count + c
            r = r - 1

        return count

if __name__=='__main__':
    n = 7
    c = count_fractions(1,1,n,1)
    print(c)

