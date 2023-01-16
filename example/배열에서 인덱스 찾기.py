

a = [1, 10, 10, 3, 56, 21, 21, 3, 4, 12, 415]

# 첫번째 인덱스만 찾기
print('첫번째 인데스만', a.index(10))

# 특정위치에서 찾기
print('특정위치에서 찾기', a.index(10, 2, 5))

# 넘파이는 쓰면 안되니까!!! 여러개 찾기
tmp = list(filter(lambda e: a[e] == 10, range(len(a))))

print('인덱스 리스트 찾기', tmp)
