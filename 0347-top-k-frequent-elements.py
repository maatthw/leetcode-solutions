def topKFrequent(nums, k):
    n = len(nums)
    freq = {}
    buckets = [[] for _ in range(n + 1)] # Each bucket will correspond to a frequency (buckets[0] = frequency of 0, buckets[1] = frequency of 1, etc..)

    # Create the frequency dictionary. Could just use Counter, but I'd prefer to avoid imports if possible.
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Insert numbers into a bucket based on their frequency
    for num, f in freq.items():
        buckets[f].append(num)

    top_k = []

    # The most frequent numbers will be the numbers in the farthest buckets
    for bucket in reversed(buckets):
        for num in bucket:
            if len(top_k) == k:
                return top_k
            top_k.append(num)

    return top_k