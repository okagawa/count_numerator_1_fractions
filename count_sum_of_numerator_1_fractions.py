# 分子が1の分数をn個合計して1になる組み合わせの数を数える。
import math

def euclidean(m:int, n:int):
    if n > m:
        (m,n) = (n,m)
    while n != 0:
        (m,n) = (n, m%n)
    return m


# q/pをm個の分数で合計する組み合わせの数を数える関数
def count_fractions(q:int, p:int, n:int, dic):
    def count_fractions_sub(q:int, p:int, m:int, prev_r:int, hist, dic):
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
                    # c = 0
                    # for r in range(r_min+1, r_max+1):
                    #     if (r_min * r) % (r - r_min) == 0:
                    #         c = c +1
                    c2 = (calc_num_of_divisors(r_min)+1)/2
                    # if c != c2:
                    #     print(f'{r_min=},{r_max=},{c},{c2}')
                    dic[p] = int(c2)
                    # print(f'dic[{p}]={c}')
                    count = count + c2
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

prime_list  = [2]

def gen_prime_list(n):
    sq = int(math.sqrt(n))
    for p_candidate in range(prime_list[-1], sq+1):
        flag = False
        for p in prime_list:
            if p_candidate % p == 0:
                flag = True
                break
        if flag == False:
            prime_list.append(p_candidate)
            if len(prime_list) % 1000 == 0:
                print(p_candidate)

def factorization(n):
    gen_prime_list(n)
    factor_list = {}
    for p in prime_list:
        while (n % p) == 0:
            n = int(n / p)
            factor_list[p] = factor_list[p] + 1 if p in factor_list else 1
    if n > 1:
        factor_list[n]=1
    return factor_list

def calc_num_of_divisors(n):
    '''n^2の約数の数を計算する'''
    factor_list = factorization(n)
    c = 1
    for _,v in factor_list.items():
        c = c * (v*2+1)  ## 2乗なので指数を2倍する
    return c

if __name__=='__main__':
    n_max = 7
    dic = dict()
    for n in range(2, n_max+1):
        c, dic = count_fractions(1, 1, n, dic)
        print(f'n={n}, c={c}')
        # print(dic)
        print()

