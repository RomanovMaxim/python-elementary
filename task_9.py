# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды

time = 86400 + 3600 + 60 + 5

days = time // 60 // 60 // 24
hours = time // 60 // 60 % 24
minuts = time // 60 % 60
seconds = time % 60


print(f'{days}:{hours}:{minuts}:{seconds}')
