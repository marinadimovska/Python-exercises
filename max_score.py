n = int(input())
arr = map(int, input().split())
max_score = float('-inf')  # Initialize max_score as negative infinity
second_score = float('-inf')  # Initialize second_score as negative infinity

for score in arr:
    if score > max_score:
        second_score = max_score  # Update second_score with the previous max_score
        max_score = score
    elif score > second_score and score != max_score:
        second_score = score  # Update second_score if score is greater than the current second_score

print(second_score)
