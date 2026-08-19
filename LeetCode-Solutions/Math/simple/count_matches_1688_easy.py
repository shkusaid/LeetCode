def count_matches(n):
    return n - 1

print(count_matches(7))

# for every even number of teams n / 2 matches and n / 2 teams eliminate i.e. suppose n is 4 in round 1
# 2 matches are played and 2 teams remaining and in the second round 1 match is played so in total
# 2 + 1 = 3  
# for odd number of teams 1 directly qualified for next round and then even scenerio applies and then
# calculated for 7 3 matches and 1 qualfied so in total 4 for next round and then in round 2 , 2 matches
#  were played and then in round 3 , 1 match, so in total 3 + 2 + 1 = 6