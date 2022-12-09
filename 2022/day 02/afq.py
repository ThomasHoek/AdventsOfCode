import sys

def main(filename: str):

    enum_points = {'X': 1, 'Y': 2, 'Z': 3}
    enum_strat  = {"A": "Y", "B": "Z", "C": "X"}

    with open(filename, mode="r") as f:
        score = 0
        for line in f:
            # Win
            if line[2] == enum_strat.get(line[0]):
                score += 6
            
            # Draw
            elif line[2] == line[0]:
                score += 3
            
            # Lose
            else:
                score += 0
            
            # Add base
            score += enum_points.get(line[2])
        
    print(score)


if __name__ == "__main__":
    main(sys.argv[1])