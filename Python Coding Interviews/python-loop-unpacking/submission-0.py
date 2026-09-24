from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_student = (0,"")
    for name, score in scores:
        best_student = max(best_student, (score, name))
    return best_student[1]


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
