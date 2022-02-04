import sys

N,M=map(int,sys.stdin.readline().rstrip().split())

site_pass = dict()

for _ in range(N):
    site,password=sys.stdin.readline().rstrip().split()
    site_pass[site]=password

for _ in range(M):
    target_site=sys.stdin.readline().rstrip()
    print(site_pass[target_site])
