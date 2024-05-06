from question_a import sum_list, average_of_list

def main():
    nums = []

    for i in range(5):
        userNumber = int(input(f"Input a number ({5 - i} left)"))
        nums.append(userNumber)

    nums.sort()

    print(f"""
    List: {nums}

    Lowest number: {nums[0]}
    Highest number: {nums[len(nums) - 1]}
    Total: {sum_list(nums)}
    Average: {average_of_list(nums)}
    """)

main()