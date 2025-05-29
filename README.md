Selection Sort
A minimal Python implementation of the selection sort algorithm.

About Selection Sort
Selection sort is a simple sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion and moves it to the sorted portion of the list. It’s useful for understanding basic sorting concepts and is easy to implement, though not efficient for large datasets.

Time Complexity:
Best: O(n²)
Average: O(n²)
Worst: O(n²)
Space Complexity: O(1) (in-place)
Stable: No (unless specifically implemented to be stable)
Usage
Python
from selection_sort import selection_sort

arr = [64, 25, 12, 22, 11]
print("Sorted array:", selection_sort(arr))
Features
Simple and easy to understand
Pure Python, no dependencies
Getting Started
Clone the repo:

bash
git clone https://github.com/RosmeoP/selection-sort.git
cd selection-sort
License
MIT
