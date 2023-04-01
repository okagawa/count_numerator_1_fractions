# 分子が1の分数をn個合計して1になる組み合わせの数を数える。
import math

def euclidean(m, n):
    if n > m:
        (m,n) = (n,m)
    while n != 0:
        (m,n) = (n, m%n)
    return m


# q/pをm個の分数で合計する組み合わせの数を数える関数
def count_fractions(q, p, n, dic):
    def count_fractions_sub(q, p, m, prev_r, hist, dic):
        count = 0
        if m == 1:
#            if q == 1:
#                hist.append(r)
#                # print(hist.append(r))
#                hist=hist[:-1]
#                return 1, hist, dic
#            else:
#                return 0, hist, dic
            pass
        else:
            # q/pを超えない1/rを満足するrの最小値を求める
            r_min = max(math.ceil(p/q), prev_r)
            r_max = math.floor(p*m/q)

            # m=2(残り2個)かつ、q/p=1/r_minの場合は特別ケース。
            # 1/r_min - 1/r の分母が分子で割り切れるかどうかで判別すればよい。
            if  m == 2 and q == 1 and p == r_min:
                if p==r_min and p in dic:
                    count = count + dic[p]
                    # print(f'q/p={q}/{p}, dic[{p}]={dic[p]}')
                else:
                    c = 0
                    for r in range(r_min+1, r_max+1):
                        if (r_min * r) % (r - r_min) == 0:
                            c = c +1
                    dic[p] = c
                    # print(f'dic[{p}]={c}')
                    count = count + c
            else:
                # q/pから1/rを引いた残りが1/r*(m-1)より大きいと、rが大きすぎるのでNG
                # 1/r*(m-1) >= q/p - 1/r
                for r in range(r_min, r_max+1):
                    next_q, next_p = q*r-p, p*r
                    if next_q > 0:
                        if m == 2: # q != 1
                            c = 0
                            if next_p % next_q == 0:
                                hist.append(r)
                                hist.append(int(next_p/next_q))
                                # print(hist)
                                hist = hist[:-2]
                                c = c + 1
                            count = count + c
                        else:
                            e = euclidean(next_q,next_p)
                            next_q, next_p = int(next_q/e), int(next_p/e)
                            hist.append(r)
                            c,hist,dic = count_fractions_sub(next_q, next_p, m-1, r, hist, dic)
                            hist = hist[:-1]
                            count = count + c

            return count,hist, dic
    count, _, dic = count_fractions_sub(q, p, n, 1, [], dic)
    return count, dic

if __name__=='__main__':
    n_max = 7
    dic = dict()
    for n in range(2, n_max+1):
        c, dic = count_fractions(1, 1, n, dic)
        print(f'n={n}, c={c}')
        # print(dic)
        print()

