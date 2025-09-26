#  weather_sample.py


weather_information = [
    {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
    {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
    {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

    {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
    {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
    {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

    {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
    {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
]

def main():
    temps = [d['temperature'] for d in weather_information]
    avg_temp = sum(temps) / len(temps)
    print("Q1 全国平均気温:", avg_temp)

    osaka_stations = [d['station'] for d in weather_information if d['prefecture'] == '大阪府']
    print("Q2 大阪府の駅名:", ",".join(osaka_stations))

    fukuoka_temps = [d['temperature'] for d in weather_information if d['prefecture'] == '福岡県']
    avg_fukuoka = sum(fukuoka_temps) / len(fukuoka_temps)
    print("Q3 福岡県平均気温:", avg_fukuoka)


if __name__ == '__main__':
    main()
