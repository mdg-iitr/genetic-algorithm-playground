def payoffMatrix(a, b):
    return {
        (0, 0): (3, 3),
        (0, 1): (0, 5),
        (1, 0): (5, 0),
        (1, 1): (1, 1)
    }.get((a, b))

def playIteratedGame(A, B):
    netScoreA = netScoreB = 0
    A.reset(), B.reset()

    for _ in range(100):
        moveA = A.move()
        moveB = B.move()
        scoreA, scoreB = payoffMatrix(moveA, moveB)
        netScoreA += scoreA
        netScoreB += scoreB
        A.update(moveA, moveB), B.update(moveB, moveA)

    return netScoreA / 100, netScoreB / 100
