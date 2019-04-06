def generate_brackets(thresholds, rates):
    if len(thresholds) != len(rates):
        return None
    if len(thresholds) == 0:
        return []
    brackets = []
    for i in range(len(thresholds)):
        brackets.append({"threshold": thresholds[i], "rate": rates[i]})
    return brackets
