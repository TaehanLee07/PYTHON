def solution(people, limit):
    people.sort() 
    left, right = 0, len(people) - 1 
    count = 0 
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1 # 
        count += 1 # 
        
    return count

N = int(input()) # 사람 수
people = list(map(int, input().split())) # 사람들의 몸무게 리스트
limit = int(input()) # 구명보트의 무게 제한

print(solution(people, limit))
