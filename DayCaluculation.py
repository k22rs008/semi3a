from datetime import date, timedelta

# 祝日の計算関数

# その年の指定された月の第n曜日の日付を計算する関数
def month_weekday(year, month, weekday, n):
    # 指定された月の1日の曜日を求める
    first_weekday = date(year, month, 1).isoweekday()

    # 第n曜日が何日目か計算する
    if first_weekday <= weekday:
        nth_weekday =  (n - 1) * 7 + (weekday - first_weekday)
    else:
        nth_weekday =  n * 7 + (weekday - first_weekday)

    return date(year, month, nth_weekday)

# 春分の日を計算する関数
def vernal_equinox(year):
    if year < 1900 or year > 2099:
        raise ValueError("Vernal Equinox Day calculation is valid only between 1900 and 2099.")

    # 一定の計算式に基づく春分の日の計算
    if year <= 1979:
        day = 20.8357 + 0.242194 * (year - 1980) - int((year - 1980) / 4)
    elif year <= 2099:
        day = 20.8431 + 0.242194 * (year - 1980) - int((year - 1980) / 4)
    else:
        raise ValueError("Vernal Equinox Day calculation is valid only between 1900 and 2099.")

    return date(year, 3, int(day))

# 秋分の日を計算する関数
def autumnal_equinox(year):
    vernal_equinox_day = vernal_equinox(year)
    return vernal_equinox_day + timedelta(days=186)


# メインの関数
def japanese_holidays(year):
    holidays = []

    # 元日
    holidays.append((date(year, 1, 1), "元日"))

    # 成人の日 - 1月の第2月曜日
    seijin_no_hi =month_weekday(year, 1, 1, 2)
    holidays.append((seijin_no_hi, "成人の日"))

    # 建国記念の日
    holidays.append((date(year, 2, 11), "建国記念の日"))

    # 天皇誕生日
    holidays.append((date(year, 2, 23), "天皇誕生日"))

    # 春分の日
    holidays.append((vernal_equinox(year), "春分の日"))

    # 昭和の日
    holidays.append((date(year, 4, 29), "昭和の日"))

    # 憲法記念日
    holidays.append((date(year, 5, 3), "憲法記念日"))

    # みどりの日
    holidays.append((date(year, 5, 4), "みどりの日"))

    # こどもの日
    holidays.append((date(year, 5, 5), "こどもの日"))

    # 海の日 - 7月の第3月曜日
    umi_no_hi = month_weekday(year, 7, 1, 3)
    if year == 2020:
        holidays.append((date(year, 7, 23), "海の日"))
    elif year == 2021:
        holidays.append((date(year, 7, 22), "海の日"))
    else:
        holidays.append((umi_no_hi, "海の日"))

    # 山の日
    if year == 2020:
        holidays.append((date(year, 8, 10), "山の日"))
    elif year == 2021:
        holidays.append((date(year, 8, 8), "山の日"))
    else:
        holidays.append((date(year, 8, 11), "山の日"))

    # 敬老の日 - 9月の第3月曜日
    keiro_no_hi = month_weekday(year, 9, 1, 3)
    holidays.append((keiro_no_hi, "敬老の日"))

    # 秋分の日
    holidays.append((autumnal_equinox(year), "秋分の日"))

    # 体育の日 - 10月の第2月曜日
    taiiku_no_hi = month_weekday(year, 10, 1, 2)
    if year<=2019:
        holidays.append((taiiku_no_hi, "体育の日"))

    #スポーツの日 - 10月の第2月曜日
    sports_no_hi = month_weekday(year, 10, 1, 2)
    if year == 2020:
        holidays.append((date(year, 7, 23), "スポーツの日"))
    elif year == 2021:
        holidays.append((date(year, 7, 22), "スポーツの日"))
    elif year >= 2022:
        holidays.append((sports_no_hi, "スポーツの日"))

    # 文化の日
    holidays.append((date(year, 11, 3), "文化の日"))

    # 勤労感謝の日
    holidays.append((date(year, 11, 23), "勤労感謝の日"))

    return holidays

# 日付の情報（年、月、日、曜日、祝日の名前）を出力する関数
def dayinfo(year, month, day, holidays):
    try:
        input_date = date(year, month, day)
        weekday_names = ["月", "火", "水", "木", "金", "土", "日"]
        weekday_index = input_date.weekday()
        weekday_name = weekday_names[weekday_index]

        # 日付の情報を出力
        print(f"{year}年{month}月{day}日 ({weekday_name})")

        # 祝日の名前を出力
        for holiday_date, holiday_name in holidays:
            if input_date == holiday_date:
                print(f"祝日: {holiday_name}")

    except ValueError as e:
        print(e)

# ユーザーからの入力を受け取り、日付情報を表示する部分
def main():
    year = int(input("年を入力してください: "))
    month = int(input("月を入力してください: "))
    day = int(input("日を入力してください: "))

    japanese_holiday = japanese_holidays(year)
    dayinfo(year, month, day, japanese_holiday)

if __name__ == "__main__":
    main()
