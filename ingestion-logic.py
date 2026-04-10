data = ["row1", "row2", "row3"]
ingested = [d.upper() for d in data]
for row in ingested:
    print("Ingested:", row)
