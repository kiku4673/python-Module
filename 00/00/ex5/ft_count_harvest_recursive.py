def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def helper(current: int) -> None:
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        helper(current + 1)

    helper(1)

# inputで収穫時期の日数を受け取って、
# intで文字列を数字に変換して、
# daysにそれを代入。

# helper関数で、
# currentという変数をintで受け取って、
# もしcurrentがdaysより大きかったら、
# "Harvest time!"を出力。からのreturn。
# そうでなかったら、Day{current}を出力。
# helper関数にcurrent + 1 を代入。

# helper関数に1を代入して、再帰を始める。
