# omscs-prep

> **If I can't rebuild it from a blank file, I don't know it yet.**

This is my 14-week preparation for Georgia Tech's **OMSCS program (Machine Learning specialization)**, which I start in Spring 2027 with **CS 7641 Machine Learning** and **CS 6603 AI, Ethics & Society**.

The plan covers Python and object-oriented design, data structures and algorithms, the scientific Python stack, and a preview of core ML methods. Each week ends with a **cold rebuild gate**: rebuilding the week's core implementations from scratch until I can do it cleanly and explain every line.

---

## The rebuild standard

A weekly gate is passed only when every item on it meets all five conditions:

1. **Blank file.** No notes, docs, earlier code, or AI.
2. **Correct.** It passes that week's original test suite unchanged, edge cases included.
3. **Fluent.** It's done in one sitting, without stalling on syntax or API lookups.
4. **Explained.** I can walk through the design, the invariants, and the Big-O. A short version goes in the commit message.
5. **Durable.** It gets rebuilt cold again a week later and at the next checkpoint (Weeks 3, 9, and 13).

A failed rebuild keeps the gate open. I re-study the gap and try again within 48 hours.

---

## Roadmap

| Phase | Weeks | Focus |
| --- | --- | --- |
| Python & OOP | 01–03 | Idiomatic Python, data model, testing, inheritance vs composition, interfaces |
| Data structures & algorithms | 04–09 | Big-O, recursion, hashing, sorting, trees, heaps, graphs, dynamic programming |
| Data stack & statistics | 10–11 | NumPy, pandas, plotting, hypothesis testing, technical writing |
| Machine learning | 12–14 | Supervised learning, randomized optimization, fairness, clustering, dimensionality reduction, MDPs, RL |

---

## Weekly gates

- [ ] **01 · Python fundamentals**
  The core function set (`is_prime`, `gcd`, `fib`, `is_palindrome`, `second_largest`, …), list and dict utilities (`transpose`, `chunk`, `group_anagrams`, `word_freq`), a closure-based counter, and a `@timed` decorator

- [ ] **02 · OOP I: classes, errors, iteration**
  The logbook core model: a `Flight` dataclass, and a `Logbook` class that is iterable, sized, and sortable. Also a custom `InvalidFlightError` with a validating parser, and a streaming generator reader

- [ ] **03 · OOP II: inheritance, interfaces, class design** · *checkpoint*
  An `Aircraft` class hierarchy using `super()`, an `Exporter` ABC with two implementations, alternative constructors (`from_csv_row`, `from_csv`), a `Timer` context manager, and a `BaseLearner` interface with `fit` / `predict` and an `evaluate()` harness

- [ ] **04 · Big-O, recursion, hashing**
  `power(x, n)` in O(log n), backtracking `subsets` and `permutations`, a `DynamicArray` with doubling resize, and a `HashMap` with chaining and load-factor resize, checked against `dict` with randomized ops

- [ ] **05 · Linear structures & sorting**
  A stack, a queue, a circular buffer, and a `LinkedList` with iterative and recursive `reverse` plus Floyd cycle detection. Also `merge_sort`, randomized in-place quicksort, and `quickselect`

- [ ] **06 · Divide & conquer, binary search, trees**
  Karatsuba multiplication and binary-search variants (`first_ge`, `last_le`, search in a rotated array). All four tree traversals, including iterative in-order, and BST insert, search, and delete covering all three delete cases

- [ ] **07 · Heaps & graphs I**
  A `MinHeap` with sift up/down and O(n) heapify, and DFS with pre/post clocks. Topological sort two ways (DFS order and Kahn's algorithm), BFS with path reconstruction, and strongly connected components

- [ ] **08 · Weighted graphs**
  Dijkstra with a binary heap and path reconstruction, Bellman-Ford with negative-cycle detection, union-find with path compression and union by rank, and Kruskal's and Prim's MST algorithms

- [ ] **09 · Dynamic programming** · *checkpoint*
  Longest increasing subsequence with reconstruction, 0/1 knapsack, edit distance with alignment, chain matrix multiplication, and Floyd–Warshall. Each one starts from a written solution (subproblem, recurrence, base cases, runtime) before any code

- [ ] **10 · NumPy**
  A 15-drill NumPy rep set, pairwise distances via broadcasting with no loops, linear regression three ways (normal equation, least squares, gradient descent), and a vectorized kNN regressor

- [ ] **11 · pandas & statistics**
  A 12-drill pandas rep set and a time-series pipeline: aligning multiple tickers, forward then backward fill, daily and cumulative returns, rolling mean and standard-deviation bands. Also a group-rate analysis with `groupby` / `pivot_table`, and a bootstrap confidence interval

- [ ] **12 · Machine learning I**
  Randomized hill climbing, simulated annealing, and a genetic algorithm. Fairness metrics (statistical parity difference, disparate impact, true-positive-rate gap), and a learning-curve / validation-curve experiment pipeline

- [ ] **13 · Machine learning II** · *checkpoint*
  k-means from scratch, PCA via SVD, and value iteration, policy iteration, and tabular Q-learning on a gridworld

- [ ] **14 · Cumulative rebuild**
  One artifact from every phase, chosen at random, rebuilt cold to the full standard

---

## Projects

| Project | Week | What it demonstrates |
| --- | --- | --- |
| **Flight logbook CLI** | 01–03 | A pure-Python package with dataclasses, validation, streaming I/O, pluggable exporters, argparse subcommands, and a pytest suite |
| **Sorting benchmark** | 05 | Insertion, merge, quick, and Timsort from n = 10² to 10⁶, with empirical growth rates on log-log axes |
| **Regression tree from scratch** | 06 | CART-style splitting in NumPy, and how overfitting grows with tree depth |
| **Nebraska route planner** | 08 | A weighted graph of towns and airports, with shortest paths (Dijkstra) and a minimum spanning tree (Kruskal), plotted |
| **kNN bias–variance study** | 10 | A vectorized kNN regressor, and in-sample vs out-of-sample error as k varies |
| **Exploratory data analysis report** | 11 | Distributions, correlations, and hypothesis tests on a real tabular dataset, written up in LaTeX |
| **Supervised learning study** | 12–13 | Five learners compared with learning and validation curves, plus a written bias–variance analysis |
| **Gridworld RL** | 13 | Value iteration, policy iteration, and Q-learning converging to the same optimal policy |

---

## Method

Every study day follows the same loop:

1. **Recall.** Rewrite yesterday's key function from a blank file.
2. **Learn.** Do the day's reading or lecture.
3. **Build.** Implement it, with a passing test or a plot as feedback.
4. **Log.** Commit, and note what broke and what fixed it.

**Ground rules**
- **Type it, don't paste it.**
- **Predict before running:** the output, the shape, the complexity.
- **Help ladder:** memory → docs → hint → pseudocode → solution. AI is used as a hint-giver only.
- **Make it visible:** a test for every function and a plot for every experiment.
- **Separate rebuild commits:** each cold rebuild is its own commit (`rebuild: <artifact>`), so the history shows every attempt.

---

## Repository layout

```
omscs-prep/
├── week/
│   └── 01/ … 14/    # builds, tests, and cold rebuilds for each week
├── reps/            # drill files rewritten from blank on a rolling basis
└── notes/           # write-ups and reports
```

---

## Academic integrity

Everything here is independent practice, completed before coursework begins. No course assignments, solutions, or course materials are stored in this repository. Graded work is written fresh from each course's specification and follows that course's collaboration and AI-use policies.

---

## References

*Fluent Python* (Ramalho) · *Python for Data Analysis* (McKinney) · *Algorithms* (Dasgupta, Papadimitriou, Vazirani) · MIT 6.006 (Spring 2020) · *Machine Learning* (Mitchell) · *Fairness and Machine Learning* (Barocas, Hardt, Narayanan) · *Reinforcement Learning: An Introduction* (Sutton & Barto)