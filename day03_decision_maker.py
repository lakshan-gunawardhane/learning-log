import random

def main():
    # 1. Define your options
    tasks = [
        "Study CS50P",
        "Do 20 Pushups",
        "Meditate",
        "Drink Water",
        "Review Goals"
    ]

    # 2. Let the computer pick one
    selected_task = random.choice(tasks)

    # 3. Show the result
    print(f"🤖 The System has decided. You must: {selected_task}")

if __name__ == "__main__":
    main()