import sys
input=sys.stdin.readline
import heapq

V,E=map(int, input().split())
K=int(input())

route=[[] for _ in range(V+1)]
for _ in range(E):
    u, v, w=map(int, input().split())
    route[u].append((v,w)) # 도착지, 가중치

# 다익스트라 최적경로 탐색
least=[int(1e9)]*(V+1) # 처음 초기값은 무한대
least[K]=0 # 시작 노드까지의 거리는 0
queue=[]
heapq.heappush(queue, [least[K], K]) # 시작 노드부터 탐색 시작

while queue: # queue에 남아있는 노드가 없을 때까지 탐색
    dist, node=heapq.heappop(queue) # 거리, 탐색할 노드

    # 기존 최단거리보다 멀다면 무시
    if least[node]<dist:
        continue

    # 노드와 연결된 인접노드 탐색
    for next_node, next_dist in route[node]:
        distance=dist+next_dist # 인접노드까지의 거리
        if distance<least[next_node]: # 기존 거리보다 짧으면 갱신
            least[next_node]=distance
            heapq.heappush(queue, [distance, next_node]) # 다음 인접 거리를 계산 하기 위해 큐에 삽입

for i in least[1:]:
    if i==int(1e9):
        print('INF')
    else:
        print(i)