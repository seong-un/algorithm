def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse()
    pickups.reverse()
    have_to_deli = 0
    have_to_pick = 0
    
    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]
        
        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2
    
    return answer