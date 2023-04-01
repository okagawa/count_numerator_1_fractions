// See https://aka.ms/new-console-template for more information
using System;
using System.Numerics;

class CountNumerator1Fractions {
    const int m_max = 7;
    public static long Euclidean (long m, long n) {
        if ( n > m ) {
            (m, n) = (n, m);
        }
        while (n != 0) {
            (m, n) = (n, m % n);
        }
        return m;
    }

    public static int CountFractions(long q, long p, int m, long prev_r) {
        var count = 0;
        if ( m == m_max-1 ) {
            Console.WriteLine(prev_r);
        }

        if ( m == 1 ) {
            if ( q == 1) {
                return 1;
            } else {
                return 0;
            }
        }

        // q/pを超えない1/rを満足するrの最小値を求める。ただし直前のr以上の値である必要がある
        long r_min = (int)Math.Max( Math.Ceiling(p*1.0/q), prev_r);
        // q/p = m/rを満足するrがrの最大値(1/r*mがq/p未満だと1/rの和の形で表せない)
        long r_max = (int)Math.Floor( p*m*1.0/q );

        // m=2(残り2個)かつ、q/p=1/r_minの場合は特別ケース。
        // 1/r_min - 1/r の分母が分子で割り切れるかどうかで判別すればよい。
        if ( m == 2 && q*r_min-p == 0 ) {
            for(var r=r_min+1; r<=r_max; r++ ){
                if ( (r_min*r) % (r - r_min) == 0 ) {
                    count = count +1;
                }
            }
        } else {
            for (var r = r_min; r <= r_max; r++ ) {
                long next_q = q * r - p;
                if ( next_q > 0 ) {
                    long next_p = p * r;
                    // m=2(残り2個)の場合は、q/p-1/r=(q*r-p)/(p*r)の分母が分子で割り切れるかどうか
                    // 判定すればよい。
                    if (m == 2) {
                        if ( next_p % next_q == 0 ){
                            count = count + 1;
                        }
                    } else {
                        var e = Euclidean( next_q, next_p );
                        next_q = next_q / e;
                        next_p = next_p / e;
                        count = count + CountFractions(next_q, next_p, m-1, r);
                    }
                }
            }
        }
        return count;
    }

    static void Main(string[] args) {
        var c = CountFractions(1, 1, m_max, 1);
        Console.WriteLine(c);
    }
}
