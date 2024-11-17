import json


def task() -> float:
    with open("input.json") as f:
        d = json.load(f)

    total_sum=sum([m["score"]* m["weight"] for m in d])
    return round(total_sum, 3)


# Пример использования
if __name__ == '__main__':
    print(task())