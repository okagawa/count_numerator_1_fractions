// See https://aka.ms/new-console-template for more information
using System;

class CountNumerator1Fractions {
    public static int Euclidean (int m, int n) {
        if ( n > m ) {
            (m, n) = (n, m);
        }
        if ( n == 0 ) {
            return m;
        } else {
            return Euclidean(n, m % n);
        }
    }

    public static int CountFractions(int q, int p, int m, int prev_r) {
        var count = 0;
        if ( m == 1 ) {
            if ( q == 1) {
                return 1;
            } else {
                return 0;
            }
        } else {
            var r_min = (int)Math.Max( Math.Ceiling(p*1.0/q), prev_r);
            var r_max = (int)Math.Floor( p*m*1.0/q );
            var r = r_max;
            while ( r >= r_min ) {
                var next_q = q * r - p;
                var next_p = p * r;
                if ( next_q > 0 ) {
                    var e = Euclidean( next_q, next_p );
                    next_q = next_q / e;
                    next_p = next_p / e;
                    count = count + CountFractions(next_q, next_p, m-1, r);
                }
                r = r - 1;
            }
            return count;
        }
    }

    static void Main(string[] args) {
        var n = 6;
        var c = CountFractions(1, 1, n, 1);
        Console.WriteLine(c);
    }
}
