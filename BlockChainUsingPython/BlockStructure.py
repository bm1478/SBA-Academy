import hashlib

h = hashlib.sha256()
print('가나다'.encode()) #해시함수 넣게 전에는 바이트 단위로 바꿔주어야함.
h.update('가나다'.encode())
print(h.hexdigest())
h.update('가나다'.encode())
print(h.hexdigest()) #값의 일치를 따질때 사용
print(len(h.hexdigest())) #32byte = 256bit 64자의 16진수

