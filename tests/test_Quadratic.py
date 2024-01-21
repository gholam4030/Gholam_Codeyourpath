from legacy_code.Quadratic import solve_quadratic


def test_solutions():
    assert solve_quadratic(1, -3, 2) == [2.0, 1.0]  # D > 0, Two solutions: [2.0, 1.0]
    assert solve_quadratic(1, -2, 1) == [1.0]  # D = 0, One solution: [1.0]
    assert solve_quadratic(1, 2, 5) is None  # D < 0, No real solution: None
