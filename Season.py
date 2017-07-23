print('season(month)')
def season(m):
    if m in (12, 1, 2):
        return 'Winter'
    elif m in (3, 4, 5):
         return 'Spring'
    elif m in (6, 7, 8):
         return 'Summer'
    elif m in (9, 10, 11):
         return 'Fall'

m= int(input('Month: '))
print(season(m))
m= int(input('Month: '))
print(season(m))

m= int(input('Month: '))
print(season(m))

m= int(input('Month: '))
print(season(m))

m= int(input('Month: '))
print(season(m))
