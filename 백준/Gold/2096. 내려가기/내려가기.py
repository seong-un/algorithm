N=int(input())
max_game=list(map(int, input().split()))
min_game=max_game[:]
for i in range(1, N):
  max_stage=list(map(int, input().split()))
  min_stage=max_stage[:]
  max_stage=[max(max_game[0]+max_stage[0], max_game[1]+max_stage[0]), max(max_game[0]+max_stage[1], max_game[1]+max_stage[1], max_game[2]+max_stage[1]), max(max_game[1]+max_stage[2], max_game[2]+max_stage[2])]
  min_stage=[min(min_game[0]+min_stage[0], min_game[1]+min_stage[0]), min(min_game[0]+min_stage[1], min_game[1]+min_stage[1], min_game[2]+min_stage[1]), min(min_game[1]+min_stage[2], min_game[2]+min_stage[2])]
  max_game=max_stage
  min_game=min_stage
print(max(max_game), min(min_game))