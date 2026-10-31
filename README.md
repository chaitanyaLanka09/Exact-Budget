# Problem 06 – Exact Budget: Count Plans and Find the Smallest Team

## 📌 Problem Overview
In this problem, we are given a pool of $N$ candidates, where each candidate has an associated hiring cost (or salary). We are assigned an exact target budget $B$.

Our goal is to analyze all possible hiring combinations (plans) that hit this exact budget and determine:
1. **`COUNT`**: The total number of unique plans (candidate subsets) whose total cost equals $B$.
2. **`MIN_SIZE`**: The minimum team size (fewest number of candidates) among all valid plans.
3. **`OPTIMAL_COUNT`**: The number of valid plans that achieve this `MIN_SIZE`.
4. **`CHOSEN`**: The lexicographically smallest 0-indexed list of candidate indices that form an optimal team of size `MIN_SIZE`.

---

## 🧠 Algorithmic Concept: Include / Exclude Backtracking

### What is Backtracking?
Backtracking is a systematic, brute-force search technique that explores all possible combinations step-by-step. Whenever a candidate path is found to be invalid or unable to produce a solution, the algorithm **prunes** (aborts) that branch and **backtracks** to the previous decision point.

### The Include / Exclude Paradigm
At every step $i$ (from candidate $0$ to $N-1$), we face a binary decision:
1. **Option A (Include Candidate $i$):**
   - Add candidate $i$'s cost to our running total (`current_sum + costs[i]`).
   - Add candidate index $i$ to our team (`current_team.append(i)`).
   - Recurse to candidate $i + 1$.
   - **Backtrack (Undo):** Remove candidate $i$ from our team (`current_team.pop()`) to restore state.
2. **Option B (Exclude Candidate $i$):**
   - Do not add candidate $i$'s cost (`current_sum` remains unchanged).
   - Candidate $i$ is not added to `current_team`.
   - Recurse to candidate $i + 1$.

```text
                     Candidate 0
                     /         \
             [Include 0]      [Exclude 0]
                /                   \
           Candidate 1           Candidate 1
           /         \           /         \
       [Inc 1]     [Exc 1]    [Inc 1]    [Exc 1]
         ...         ...        ...        ...
```

### Key Considerations
- **Pruning**: If all candidate costs are positive and `current_sum > budget`, any further inclusions will only increase the sum. We can safely `return` immediately.
- **Base Case (Target Reached)**:
  - If `current_sum == budget`, we have discovered a valid plan!
  - Increment `COUNT`.
  - Compare the team size `len(current_team)` against `MIN_SIZE`:
    - If strictly smaller: update `MIN_SIZE = len(current_team)`, reset `OPTIMAL_COUNT = 1`, and update `CHOSEN = list(current_team)`.
    - If equal: increment `OPTIMAL_COUNT += 1`, and if `current_team < CHOSEN` (lexicographical comparison), update `CHOSEN`.
- **Lexicographical Comparison**:
  In Python, lists are compared element-by-element from left to right:
  `[0, 3] < [1, 2]` evaluates to `True` because `0 < 1`.

---

## ⏱️ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(2^N)$ in the worst case, as each candidate has 2 choices (include or exclude). Pruning helps reduce the explored branches in practice.
- **Space Complexity**: $\mathcal{O}(N)$ recursion stack depth and current team storage.

---

## 🚀 How to Run the Program

Run the script from your terminal using Python 3:

```bash
python problem06.py
```

---

## 🧪 Sample Test Cases

### Sample Test Case 1 (From Assessment)
**Input:**
```text
6 10
5 5 10 3 7 10
```
**Candidate Mapping (1-based):**
- Candidate 1: 5
- Candidate 2: 5
- Candidate 3: 10
- Candidate 4: 3
- Candidate 5: 7
- Candidate 6: 10

**Valid Plans Summing to 10:**
- `[3]` (cost 10, size 1)
- `[6]` (cost 10, size 1)
- `[1, 2]` (cost 5 + 5 = 10, size 2)
- `[4, 5]` (cost 3 + 7 = 10, size 2)

**Expected Output:**
```text
COUNT         : 4
MIN_SIZE      : 1
OPTIMAL_COUNT : 2
CHOSEN        : [3]
```

### Sample Test Case 2 (From Assessment - Impossible Target)
**Input:**
```text
3 1
2 4 6
```
**Expected Output:**
```text
COUNT         : 0
MIN_SIZE      : -1
OPTIMAL_COUNT : 0
CHOSEN        : []
```

### Additional Test Scenarios
1. **Target T = 0**:
   - `3 0` with costs `2 3 5`
   - `COUNT: 1`, `MIN_SIZE: 0`, `OPTIMAL_COUNT: 1`, `CHOSEN: []`
2. **Duplicate Costs & Tie-Breaking**:
   - Covered in Sample 1 with duplicate costs `5, 5` and `10, 10`, testing separate candidate identification and lexicographical tie-breaking (`[3]` vs `[6]`).

---

## 📦 Git & GitHub Workflow

When your implementation is complete and verified:
1. Initialize git repository: `git init`
2. Add files: `git add .`
3. Commit changes: `git commit -m "feat: implement include/exclude backtracking for exact budget"`
4. Add remote & push (after confirming with instructor/user):
   ```bash
   git remote add origin https://github.com/<your-username>/Problem-06-Exact-Budget.git
   git branch -M main
   git push -u origin main
   ```
