#Team name : Py-Pioneers

def convert_seconds(total_seconds: int) -> str:
    seconds= int(total_seconds)
    if not(0<= seconds<= 86400):
        raise ValueError("total_seconds must be between 0 and 86400")
    minutes = seconds//60
    remaining_seconds= seconds % 60
    return f"{minutes}m {remaining_seconds}s"
