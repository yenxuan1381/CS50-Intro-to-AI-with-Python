from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    # A is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A says "I am both a knight and a knave."
    # If A is a knight, he is telling the truth so he is a knight and a knave
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave, then he is telling a lie so he is not both a knight and knave
    Implication(AKnave, Not(And(AKnight, AKnave)))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    # A is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or a knave, not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A says "We are both knaves."
    # If A is a knight, then A and B are both knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, then A and B are not both knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    # A is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or a knave, not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A says "We are the same kind."
    # If A is a knight, then A and B are the same kind
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # B says "We are of different kinds."
    Implication(BKnight, Or(And(AKnight,BKnave), And(BKnight, AKnave))),
    Implication(BKnave, Not(Or(And(AKnight,BKnave), And(BKnight, AKnave))))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

    # A is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or a knave, not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # C is either a knight or a knave, not both
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # B says "A said 'I am a knave'."
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnave)),

    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnight, Not(CKnave)),

    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
