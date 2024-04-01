from collections import Counter

def print_stats(numbers):
    if not numbers:
        return

    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    mode = Counter(numbers).most_common(1)[0][0]

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Mode: {mode}\n")
def process_stream(stream):
    numbers = []
    for num in stream:
        numbers.append(num)
        print_stats(numbers)

#Example
stream_input = "5 2 4 3 2 -3"
stream = map(int, stream_input.split()[1:])
process_stream(stream)

