

with open("fishtotals.txt", "r+") as myfile:
    count = 0
    flounders = []

    for line in myfile:
        individual = line.split(",") #"Fisherman C: flounder 12 inches", " "
        fisherman_name = individual[0]


        for piece in individual:
            if "flounder" in piece:
                sole = piece.strip() 
                structured = (f"{fisherman_name}: {sole}")
                flounders.append(structured)
                count += 1
                pass

with open("flounder.txt", "w") as new_file:
        for line in flounders:
            new_file.write(line + "\n")
        new_file.write(f"Total: {count} flounders caught")
