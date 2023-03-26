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


function euclidean(m,n) {
    if ( n > m ) {
        t = m;
        m = n;
        n = t;
    }
    if ( n == 0 ) {
        return m;
    } else {
        return euclidean(n, m % n);
    }
}

function count_fractions(q, p, m, prev_r) {
    var count = 0;
    if (m == 1) {
        if(q == 1){
            return 1;
        }else{
            return 0;
        }
    }
    var r = Math.max(Math.ceil(p/q,), prev_r);
    while (2*p*(m-1)>=q*r){
        var next_q = q*r-p;
        var next_p = p*r;
        if (next_q > 0) {
            var e = euclidean(next_q, next_p);
            next_q = parseInt(next_q/e);
            next_p = parseInt(next_p/e);
            count = count + count_fractions(next_q, next_p, m-1, r);
        }
        r = r + 1;
    }

    return count;
}


function _debug( message ) {
	document.write("<p>Debug: " + message + ".<\/p>");
}
