# chatGPTに頼んだら生成してくれたコード。ただし結果は不正確。
chatGPT_q = '''
# 1を分子が1の6つの分数の和で表す組み合わせの数を求めたい。
'''

chatGPT_ans = '''
1を分子が1の6つの分数の和で表すためには、分母が1である分数を必ず1つ含める必要があります。分母が2、3、4、5、6である分数をそれぞれ最大5つまで組み合わせることができます。
ここでは、以下のような再帰的なアプローチを使って、分母が1、2、3、4、5、6である分数の組み合わせを全列挙し、和が1になる組み合わせをカウントします。

上記のプログラムでは、count_fractions関数は3つの引数を取ります。totalは、残りの分数の和がいくらであるかを表し、最初は1から始まります。denominatorsは、既に選択された分母のリストを表します。最初は、1だけが含まれます。countは、現在の有効な組み合わせの数を保持します。
関数は、denominatorsリストに6つの要素が含まれるまで再帰的に呼び出されます。各再帰呼び出しでは、1から6の範囲の分母を1つ選び、それが既に選択されたリストに含まれていないことを確認します。分母が1の場合は、分数が1/1になります。それ以外の場合は、分数が1/(分母)になります。
選択された分数の合計が1に等しい場合、count変数を1増やします。関数の最後に、count変数を返します。
結果は84になるため、1を分子が1の6つの分数の和で表す組み合わせの数は84通りあることがわかります。
'''

def count_fractions(total, denominators, count):
    if len(denominators) == 6:
        if total == 1:
            return count + 1
        else:
            return count
    else:
        for i in range(6):
            if i + 1 not in denominators:
                if i == 0:
                    count = count_fractions(total - 1, denominators + [i + 1], count)
                else:
                    count = count_fractions(total - 1/(i + 1), denominators + [i + 1], count)
        return count

print(count_fractions(1, [1], 0)) # 結果は84になる
