"use strict";
// 分子が1の分数をn個合計して1になる組み合わせの数を数える。
// コンソール(Node.js)用
var n_max=8;
var prime_list = [2];

for (var n = 2; n <= n_max; n++) {
    var objDate0 = new Date();
    var tick0 = objDate0.getTime();
    
    console.log("<p> n = " + n + "</p>");
    var cache = new Map();
    var c;
    [c, cache] = count_fractions(1, 1, n, 1, cache);
    console.log("<h2>"+ c + "</h2>");

    var objDate1 = new Date();
    var tick1 = objDate1.getTime();
    var cost1 = tick1 - tick0;
    _debug(cost1/1000 + " sec");

}

// Euclidの互除法
function euclidean(m,n) {
    if ( n > m ) {
        [m,n] = [n,m];
    }
    if ( n == 0 ) {
        return m;
    } else {
        return euclidean(n, m % n);
    }
}

// q/pをm個の分数で合計する組み合わせの数を数える関数
function count_fractions(q, p, m, prev_r, cache) {
    var count = 0;
//    if (m == 1) {
//        if(q == 1){
//            return 1;
//        }else{
//            return 0;
//        }
//    }
    if ( m == 2 ) {
        console.log('q='+q+',p='+p);
    }

    // q/pを超えない1/rを満足するrの最小値を求める。ただし直前のr以上の値である必要がある
    var r_min = Math.max(Math.ceil(p/q), prev_r);
    // q/p = m/rを満足するrがrの最大値(1/r*mがq/p未満だと1/rの和の形で表せない)
    var r_max = Math.floor(p*m/q);

    // m=2(残り2個)かつ、q/p=1/r_minの場合は特別ケース。
    // 1/r_min - 1/r の分母が分子で割り切れるかどうかで判別すればよい。
    if ( m == 2 && q == 1 && r_min == p ) {
        if ( cache.has(p) == true ) {
            count = count + cache.get(p);
        } else {
//            var c = 0;
//            for(var dr=1; dr<=(r_max-r_min); dr++ ) {
//                var r_min2 = r_min % dr;
//                if ( r_min2 == 0 || ((r_min2*r_min2) % dr) == 0 ) {
//                    c = c+1;
//                }
//            }
            var c2 = Math.trunc((calc_num_of_divisors(r_min)+1)/2);
//            if ( c != c2 ){
//                console.log('r_min='+r_min+',c='+c+',c2='+c2);
//            }
//            for(var r=r_min+1; r<=r_max; r++ ){
//                if ( (r_min*r) % (r - r_min) == 0 ) {
//                    c = c +1;
//                }
//            }
            cache.set(p, c2);
            count = count + c2;
        }
    } else {
        for( var r=r_min; r<=r_max; r++ ) {
            var next_q = q*r-p;
            if (next_q > 0) {
                var next_p = p*r;
                // m=2(残り2個)の場合は、q/p-1/r=(q*r-p)/(p*r)の分母が分子で割り切れるかどうか
                // 判定すればよい。
                if (m == 2) {
                    if ( next_p % next_q == 0 ){
                        count = count + 1;
                    }
                } else {
                    var c;
                    var e = euclidean(next_q, next_p);
                    next_q = Math.trunc(next_q/e);
                    next_p = Math.trunc(next_p/e);
                    [c, cache] = count_fractions(next_q, next_p, m-1, r, cache);
                    count = count + c;
                }
            }
        }
    }

    return [count, cache];
}

function gen_prime_list(n) {
    var sq = Math.trunc(Math.sqrt(n));
    for( var pc = prime_list.at(-1); pc <= sq+1; pc++) {
        var flag = false;
        for(const p of prime_list) {
            if( pc % p == 0 ) {
                flag = true;
                break;
            }
        }
        if( flag == false ) {
            prime_list.push(pc);
            if( prime_list.length % 10000 == 0) {
                console.log(pc);
            }
        }
    }
}

function factorization(n) {
    gen_prime_list(n);

    var factor_list = new Map();
    for (const p of prime_list) {
        while( n % p == 0 ) {
            n = Math.trunc(n / p);
            if( factor_list.has(p) == true) {
                factor_list.set(p, factor_list.get(p)+1);
            } else {
                factor_list.set(p, 1);
            }
        }
    }
    if( n > 1 ) {
        factor_list.set(n, 1);
    }
    return factor_list;
}

function calc_num_of_divisors(n) {
    // n^2の約数の数を計算する
    var factor_list = factorization(n);
    var c = 1;
    for(const v of factor_list.values() ) {
        // console.log('k='+k+',v='+v)
        c = c * (v*2+1);
    }
    return c;
}


function _debug( message ) {
	console.log("<p>Debug: " + message + ".<\/p>");
}
