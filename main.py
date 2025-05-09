from map_utils import Map

def read_point(prompt):
    while True:
        try:
            parts = input(prompt).split()
            if len(parts) != 2:
                raise ValueError
            return tuple(map(int, parts))
        except ValueError:
            print("Введите координаты в формате: row col (например, 2 3)")

def main():
    try:
        map_obj = Map("map.txt")
    except FileNotFoundError:
        print("Файл map.txt не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении карты: {e}")
        return

    print(f"Карта загружена: {map_obj.rows}x{map_obj.cols}")
    start = read_point("Введите координаты начальной точки (суша): ")
    goal = read_point("Введите координаты конечной точки (суша): ")

    try:
        path = map_obj.find_path(start, goal)
    except ValueError as ve:
        print("Ошибка:", ve)
        return

    if path:
        print("\nНайден путь:")
        for r, c in path:
            print(f"({r}, {c})", end=" ")
        print()
    else:
        print("Путь не найден.")

if __name__ == "__main__":
    main()
