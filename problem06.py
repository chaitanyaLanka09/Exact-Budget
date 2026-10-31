
def solve_exact_budget(n, budget, costs):
    total_plans = 0
    min_size = float('inf')
    optimal_plans = 0
    best_chosen = []

    def backtrack(index, current_sum, current_team):
        nonlocal total_plans, min_size, optimal_plans, best_chosen

        # Step 1: Pruning
        if current_sum > budget:
            return

        # Step 2: Exact budget reached
        if current_sum == budget:
            total_plans += 1
            current_size = len(current_team)

            if current_size < min_size:
                min_size = current_size
                optimal_plans = 1
                best_chosen = list(current_team)

            elif current_size == min_size:
                optimal_plans += 1
                if current_team < best_chosen:
                    best_chosen = list(current_team)

            return

        # Stop when all candidates are examined
        if index == n:
            return

        # Step 3: Include candidate
        current_team.append(index + 1)
        backtrack(index + 1, current_sum + costs[index], current_team)
        current_team.pop()

        # Step 4: Exclude candidate
        backtrack(index + 1, current_sum, current_team)

    backtrack(0, 0, [])

    if min_size == float('inf'):
        min_size = -1
        optimal_plans = 0
        best_chosen = []

    return total_plans, min_size, optimal_plans, best_chosen


def main():
    first_line = list(map(int, input().split()))

    if len(first_line) == 2:
        n, budget = first_line
    else:
        n = first_line[0]
        budget = int(input())

    costs = list(map(int, input().split()))

    count, min_size, opt_count, chosen = solve_exact_budget(
        n, budget, costs
    )

    print(f"COUNT {count}")
    print(f"MIN_SIZE {min_size}")
    print(f"OPTIMAL_COUNT {opt_count}")

    if min_size == -1:
        print("CHOSEN NONE")
    elif not chosen:
        print("CHOSEN EMPTY")
    else:
        print("CHOSEN", *chosen)


if __name__ == "__main__":
    main()
