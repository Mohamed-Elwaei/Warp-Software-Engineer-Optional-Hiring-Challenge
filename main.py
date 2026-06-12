
correct_tuple = None
with open("space_missions.log", "r") as f:
    best_duration = -1
    best_code = None

    for line in f:
        line = line.strip()
        if not line or line.startswith("#") or "|" not in line:
            continue

        fields = [f.strip() for f in line.split("|")]
        if len(fields) < 8:
            continue

        _, _, destination, status, _, duration, _, code = fields[:8]

        if destination == "Mars" and status == "Completed":
            try:
                d = int(duration)
                if d > best_duration:
                    best_duration = d
                    correct_tuple = fields
            except ValueError:
                continue


with open("answer.txt", "w") as answer:
    answer.write("|".join(fields))