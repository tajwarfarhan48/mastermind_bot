# MODIFY THE CODE LENGTH, SOLUTION AND INITIAL GUESS TO TEST THE BOT WITH DIFFERENT COMBINATIONS. 
# EACH COMBINATION MUST HAVE {LEN_CODE} NUMBERS, AND EACH NUMBER MUST BE A NUMBER FROM 1 TO 8

LEN_CODE = 4
NUM_TRIES = 10
solution = '5678'

possible_colors = '87654321'
possible_scores = []

for i in range( LEN_CODE + 1 ):
    for j in range( LEN_CODE + 1 - i ):
        possible_scores.append( f'{i}{j}' )

untried_guesses = [ '1', '2', '3', '4', '5', '6', '7', '8' ]

while len( untried_guesses[-1] ) < LEN_CODE:
    ug = untried_guesses.pop()

    for c in possible_colors:
        untried_guesses.insert( 0, c + ug )

untried_guesses.sort()
possible_solutions = untried_guesses.copy()

print( f"Solution: {solution}" )

def get_score( guess : str, actual : str ) -> str:
    if len( guess ) != LEN_CODE or len( actual ) != LEN_CODE:
        raise RuntimeError( f"Length of guess and actual sequences must be {LEN_CODE} pegs, got guess: {guess} with {len( guess )} pegs and actual: {actual} with {len( actual )} pegs." )

    black, white = 0, 0

    guess_pegs = [ c for c in guess ]
    actual_pegs = [ c for c in actual ]
    indices = { i for i in range( LEN_CODE ) }
    
    unused_actual_indices = indices.copy()
    unused_guess_indices = indices.copy()

    for i in range( LEN_CODE ):
        if actual_pegs[i] == guess_pegs[i]:
            black += 1
            unused_actual_indices.remove( i )
            unused_guess_indices.remove( i )

    for i in unused_guess_indices:
        for j in range( LEN_CODE ):
            if j in unused_actual_indices and guess_pegs[i] == actual_pegs[j]:
                white += 1
                unused_actual_indices.remove( j )
                break 

    return f'{black}{white}'

guess = ''.join( [ str( i // ( LEN_CODE // 2 ) + 1 ) for i in range( LEN_CODE ) ] )

for i in range( NUM_TRIES + 2 ):
    print( f"{i+1}-th guess: {guess}" )
    
    score = get_score( guess, solution )
    print( f"Score: {score[0]}B {score[1]}W" )

    if i == NUM_TRIES + 1 and score[0] != LEN_CODE:
        print( "The bot has taken too many turns. You have won!" )
        break 

    if score[0] == LEN_CODE:
        print( "The bot won!" )
        break

    untried_guesses.remove( guess )
    possible_solutions = [ s for s in possible_solutions if get_score( guess, s ) == score ]

    if len( possible_solutions ) == 1 and possible_solutions[0] == solution:
        print( f"{i+2}-th guess: {solution}" )
        score = get_score( solution, solution )
        print( f"Score: {score[0]}B {score[1]}W" )
        print( "The bot has won!" )
        break

    guess_kill_counts = []

    for guess in untried_guesses:
        guess_kill_count = len( possible_solutions ) - 1

        for score in possible_scores:
            score_kill_count = 0

            for s in possible_solutions:
                if get_score( guess, s ) != score:
                    score_kill_count += 1
            
            guess_kill_count = min( score_kill_count, guess_kill_count )
        
        guess_kill_counts.append( guess_kill_count )

    max_kill_count = guess_kill_counts[0]
    max_guess = untried_guesses[0]

    for i in range( len( untried_guesses ) ):
        if guess_kill_counts[i] > max_kill_count:
            max_kill_count = guess_kill_counts[i]
            max_guess = untried_guesses[i]
    
    guess = max_guess