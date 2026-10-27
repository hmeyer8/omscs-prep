# Preparation roadmap

> Planning archive, preserved from the previous README on October 27, 2026.
> These are learning targets, not completed deliverables or a current daily schedule.
> Week numbers below refer to the original plan; dated practice folders do not necessarily follow that sequence.
> Project paths and release tags in the tables are proposed locations and names, not links to existing artifacts.

The original plan spans Python, algorithms, scientific computing, and machine learning.
The [main README](../README.md) lists the work currently available. Update this roadmap
as priorities change; mark a target complete only when its implementation and checks are committed.

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

| Project | Week | What it demonstrates | Where |
| --- | --- | --- | --- |
| **Flight logbook CLI** | 01–03 | A pure-Python package with dataclasses, validation, streaming I/O, pluggable exporters, argparse subcommands, and a pytest suite | `logbook/` (tags `logbook-v1` … `v3`) |
| **Sorting benchmark** | 05 | Insertion, merge, quick, and Timsort from n = 10² to 10⁶, with empirical growth rates on log-log axes | `week/05/` |
| **Regression tree from scratch** | 06 | CART-style splitting in NumPy, and how overfitting grows with tree depth | `week/06/regression_tree.py` |
| **Nebraska route planner** | 08 | A weighted graph of towns and airports, with shortest paths (Dijkstra) and a minimum spanning tree (Kruskal), plotted | `week/08/` |
| **kNN bias–variance study** | 10 | A vectorized kNN regressor, and in-sample vs out-of-sample error as k varies | `week/10/regressors.py` |
| **Exploratory data analysis report** | 11 | Distributions, correlations, and hypothesis tests on a real tabular dataset, written up in LaTeX | `notes/eda_report.pdf` |
| **Supervised learning study** | 12, 14 | Decision tree, kNN, and SVM compared with learning and validation curves, plus a written bias–variance analysis | `week/12/` + `notes/analysis_report.pdf` |
| **Gridworld RL** | 13 | Value iteration, policy iteration, and Q-learning converging to the same optimal policy | `week/13/rl.py` |

---

## References

*Fluent Python* (Ramalho) · *Python for Data Analysis* (McKinney) · *Algorithms* (Dasgupta, Papadimitriou, Vazirani) · MIT 6.006 (Spring 2020) · *Machine Learning* (Mitchell) · *Fairness and Machine Learning* (Barocas, Hardt, Narayanan) · *Reinforcement Learning: An Introduction* (Sutton & Barto)
