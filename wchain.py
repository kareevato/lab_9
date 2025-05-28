# Файл: wchain.py

def read_input(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        words = [f.readline().strip() for _ in range(n)]
    return words

def write_output(filename, result):
    with open(filename, "w") as f:
        f.write(str(result) + "\n")

def longest_chain(words):
    word_set = set(words)
    words.sort(key=len)
    dp = {}
    max_chain = 1

    for word in words:
        dp[word] = 1  # мінімум: сам по собі
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]  # видаляємо одну букву
            if prev in dp:
                dp[word] = max(dp[word], dp[prev] + 1)
        max_chain = max(max_chain, dp[word])

    return max_chain

if __name__ == "__main__":
    words = read_input("wchain.in")
    result = longest_chain(words)
    write_output("wchain.out", result)
