// 分子が1の分数をn個合計して1になる組み合わせの数を数える。
var n_max=7;

for (var n = 2; n <= n_max; n++) {
    var objDate0 = new Date();
    var tick0 = objDate0.getTime();
    
    document.write("<p> n = " + n + "</p>");
    c = count_fractions(1,1,n,1);
    document.write("<h2>"+ c + "</h2>");

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
function count_fractions(q, p, m, prev_r) {
    var count = 0;
//    if (m == 1) {
//        if(q == 1){
//            return 1;
//        }else{
//            return 0;
//        }
//    }

    // q/pを超えない1/rを満足するrの最小値を求める。ただし直前のr以上の値である必要がある
    var r_min = Math.max(Math.ceil(p/q), prev_r);
    // q/p = m/rを満足するrがrの最大値(1/r*mがq/p未満だと1/rの和の形で表せない)
    var r_max = Math.floor(p*m/q)
    
    var r = r_min
    while ( r <= r_max ){
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
                var e = euclidean(next_q, next_p);
                next_q = parseInt(next_q/e);
                next_p = parseInt(next_p/e);
                count = count + count_fractions(next_q, next_p, m-1, r);
            }
        }
        r = r + 1;
    }

    return count;
}


function _debug( message ) {
	document.write("<p>Debug: " + message + ".<\/p>");
}
