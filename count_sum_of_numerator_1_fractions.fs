open System

let rec euclidean m n =
    let (m,n) = if n > m then (n,m) else (m,n)
    if n = 0 then m else euclidean n (m % n)

let rec count_fractions (q:int) (p:int) (m:int) (prev_r:int) =
    let count = 0
    match m with
    | 1 -> if q = 1 then 1 else 0
    | _ ->
        let r_min = Math.Max(int(Math.Ceiling(float(p)/float(q))), prev_r)
        let r_max = int(Math.Floor(2.*float(p)*(float(m)-1.)/float(q)))

        let (r:int) = r_max
        let rec cf_loop r count =
            if r < r_min then count else
                let next_q, next_p = q*r-p, p*r
                if next_q > 0 then
                    let e = float(euclidean next_q next_p)
                    let next_q = int(float(next_q)/e)
                    let next_p = int(float(next_p)/e)
                    let count = count + count_fractions next_q next_p (m-1) r
                    cf_loop (r-1) count
                else
                    cf_loop (r-1) count
        cf_loop r count



[<EntryPoint>]
let main args =
    // for arg in args do
    for n in 2..7 do
        let c = count_fractions 1 1 n 1
        printfn "n=%d, c=%d" n c

    0