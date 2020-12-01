#!/usr/bin/env python3

# An interactive Nim solver

# Ideas:
# - ascii art for heaps
# - interactive
# - arbitrarily many heaps
# - option to show the best possible move

# Print the ASCII art for a list of heaps.
# Each element of `heaps` should be a single integer with the height of the heap.
def print_heaps(heaps):
    height = max(heaps)
    for i in range(height, 0, -1):
        for heap in heaps:
            if heap >= i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i, _ in enumerate(heaps):
        print(i + 1, end="")
    print()

# Return the heap to move and the number of items to remove.
def solver(heaps):
    # TODO: implement a solver, this just returns a random valid move
    return next((heap, height) for (heap, height) in enumerate(heaps) if height > 0)

def computer_turn(heaps):
    print_heaps(heaps)
    heap, height = solver(heaps)
    heaps[heap] -= height
    print()
    print_heaps(heaps)
    return True

def generate_heaps():
    from random import randint
    MAX_HEAP_SIZE = 10
    MAX_HEAPS = 5
    return [randint(1, MAX_HEAP_SIZE) for heap in range(1, randint(1, MAX_HEAPS) + 1)]

def game_over(heaps):
    return all(map(lambda x: x == 0, heaps))

def player_turn():
    print("Choose a heap to play: ", end="")
    heap = input()
    print("Choose how many items to remove: ", end="")
    height = input()
    return int(heap) - 1, int(height)

def play_game():
    def turn(heap, height):
        nonlocal heaps
        if heap >= len(heaps):
            print("error: illegal move: there are only {} heaps, but you tried to remove from heap {}".format(len(heaps), heap + 1))
            return False
        if heaps[heap] < height:
            print("error: illegal move: there are only {} items in heap {}, but you tried to remove {}".format(heaps[heap], heap + 1, height))
            return False
        heaps[heap] -= height
        print()
        print_heaps(heaps)
        return True

    heaps = [1,3,5] #generate_heaps()
    print_heaps(heaps)
    while True:
        # handle illegal moves
        if not turn(*player_turn()):
            continue
        if game_over(heaps):
            print("You win!")
            break
        assert turn(*solver(heaps)), "solver made an illegal move"
        if game_over(heaps):
            print("You lose!")
            break

play_game()
