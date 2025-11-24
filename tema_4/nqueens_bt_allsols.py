import copy

def print_board(sol):
    N = len(sol)

    header = "  " + " ".join(str(i) for i in range(N))
    print(header)
    print(" +" + "--" * N + "-")

    for i in range(N):
        row_str = str(i) + "| "
        for j in range(N):
            row_str += "Q " if j == sol[i] else ". "
        print(row_str)


def is_solution(sol, row):
    return row == len(sol)


def is_feasible(sol, row, col):
    feasible = True
    i = 1
    while feasible and i <= row:
        feasible_col = sol[row-i] != col
        feasible_diag_45 = sol[row-i] != col-i
        feasible_diag_135 = sol[row-i] != col+i
        feasible = feasible_col and feasible_diag_45 and feasible_diag_135
        i += 1
    return feasible


def n_queens_bt_allsols(sol, n, row, sols):
    if is_solution(sol, row):
        sols.append(copy.deepcopy(sol))
    else:
        for col in range(n):
            if is_feasible(sol, row, col):
                sol[row] = col
                sols = n_queens_bt_allsols(sol, n, row+1, sols)
                sol[row] = -1
    return sols


n = 4
sol = [-1] * n
sols = []
n_queens_bt_allsols(sol, n, 0, sols)
for s in sols:
    print_board(s)