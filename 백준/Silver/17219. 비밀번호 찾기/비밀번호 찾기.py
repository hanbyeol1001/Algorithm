import sys

n, m = map(int, sys.stdin.readline().split())

address = dict()
for _ in range(n):
    url, password = sys.stdin.readline().split()
    address[url] = password

for _ in range(m):
    url = sys.stdin.readline().strip()
    print(address[url])