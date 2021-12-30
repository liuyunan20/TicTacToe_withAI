def get_percentage(num, round_digits=None):
    if round_digits is None:
        return f"{round(num * 100)}%"
    else:
        return f"{round(num * 100, round_digits)}%"
