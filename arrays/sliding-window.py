start = 0
for end in range(N):
  if end - start + 1 > window_size:
    # do something
    start += 1

  if end - start + 1 == window_size:
    # Found a window
