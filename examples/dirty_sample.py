def process(u, i):
    # This function does everything: validates, calculates, and saves
    if u != "":
        res = []
        for x in i:
            if x > 10:
                res.append(x * 1.15)
        print("Saving data for user: " + u)
        with open("log.txt", "a") as f:
            f.write(u + " processed data\n")
        return res
    else:
        return None
