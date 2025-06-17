

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi_array = []
    try:
        for it_height, it_weight in zip(height, weight):
            value_bmi = it_weight / (it_height * it_height)
            bmi_array.append(value_bmi)
        return bmi_array
    except Exception as e:
        print(e)

def apply_bmi(bmi: list[int | float], limit: int) -> list[bool]:
    return [True if bmi_value > limit else False for bmi_value in bmi]