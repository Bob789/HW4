slice: int = int(input("Give me a slice piza number : "))
friend: int = int (input("Give me number friends : "))

remainder: int = int (slice % friend)
slice_per_freind: int = int (slice/friend)


print(f"remainder {remainder}")
print(f"each friend get  {slice_per_freind}")