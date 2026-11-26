"""cloud-computing-lab 的第一个程序 —— 简单的学生信息小程序。"""


def greet(name: str) -> str:
    """返回问候语。"""
    return f"你好，{name}！欢迎来到云计算课程实验室。"


def show_menu() -> None:
    """打印一个简单的菜单。"""
    menu = [
        "1. 打招呼",
        "2. 计算两数之和",
        "3. 计算一组数的平均值",
        "0. 退出",
    ]
    print("=" * 30)
    print("cloud-computing-lab 小程序")
    print("=" * 30)
    for line in menu:
        print(line)


def add(a: float, b: float) -> float:
    """计算两数之和。"""
    return a + b


def average(numbers: list[float]) -> float:
    """计算一组数的平均值；空列表抛出 ValueError。"""
    if not numbers:
        raise ValueError("列表不能为空，无法计算平均值。")
    return sum(numbers) / len(numbers)


def main() -> None:
    show_menu()
    while True:
        choice = input("请选择功能: ").strip()
        if choice == "1":
            name = input("请输入你的名字: ").strip() or "同学"
            print(greet(name))
        elif choice == "2":
            try:
                a = float(input("请输入第一个数: "))
                b = float(input("请输入第二个数: "))
                print(f"{a} + {b} = {add(a, b)}")
            except ValueError:
                print("输入的不是有效数字，请重试。")
        elif choice == "3":
            raw = input("请输入一组数字，用空格分隔: ")
            try:
                nums = [float(x) for x in raw.split()]
                print(f"平均值 = {average(nums):.2f}（共 {len(nums)} 个数）")
            except ValueError as err:
                print(f"输入有误：{err}")
        elif choice == "0":
            print("再见！")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()
