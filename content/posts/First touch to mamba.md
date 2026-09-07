---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHYM25ZZ%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T182833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQD4a1kzz4SzgFhT16nV57S3ti1IUYqysvFK9IW4JX6R2gIhANTLYkvtH05sehtNPu%2BDEfmhnn74NuI%2B41nWkPctjrjtKv8DCEEQABoMNjM3NDIzMTgzODA1IgwF7xOkKeM3xRULG3oq3AP8IbuQaJ3RhBEc%2Fwmu%2FVLqyH%2BWPy0OJbnez6L2JwHY4w9CYQsmjGa%2FyMGFVyKwzmXc1t7SKFcki4U7zo5Y42yua4J3Yt%2BYYa8oZ1jp5h0QEXVv5GFHpsupGvtJeV9eCwgXfyDTG9dHdPyvNyZ7vFhsdvHLzcnc2cUdQ%2FyWb3q6dXuPd%2FsdXDXPDzHC9Pwix1QqlIY85Inl1K%2FRJg8l%2BUJ6p9CftdL2ofd9PDWAxszm1UzDskuU6zV8VYMnqshYELqUcab3ATOOxQNDAtKgqiLAmfPKDP3JaOtL2U8%2Be8HHbUGuiYr89LBh%2BdiH8mW7F7%2Fj%2F4rKq4cydVG%2Bpk8negAU4riAy%2BhS1h%2BkUS3HsX8JdHm8Ff1EaAxbSzY0xNbKjA5T9G4eT8kXzxxLnGbLUl65WMznBJjAPqRkhf4WA5ELTXPaRb%2F09bKbbRwEozSIedzShnnL%2BjiWxwjXpHdlN6VdA8peOc694Qlr72gWZrOJQQ0%2B7F7NksI9XwDe1lUYwRWMf140wdLTswFcfBPyYU7quAmL4d%2B3WXEoRR%2B3x%2FuwZGdazTFANQ598ENnZ2u0MFK3ecZKu8h7q%2Fu%2BGObUn7Ah3Ms8aa6%2B3t%2FF7vt%2BFJrhd%2FzsKVwBig4BWBfz8TC0yfvUBjqkAZE4GuTMHyqZj1xRGJreXFeQzVbDY7Yeq%2FrfjO3V5c%2BshRfb0rAVYMjIFuJv1iRwGgqChyMtW9LY0XT5R0dPMHD108Q8qU7oe6%2F4p9vbG901QuMjhPBZ0iqgzwcn37dNVtTfskkPjhSYYpMefxfcuJ%2FH%2FRt82kYTq9I5USaRpcSi91CXX4cfeiFkp5WXxtEw6Gq6RcReOJHVkunxrv%2BOv%2FJ6hQWJ&X-Amz-Signature=9e7ae3add3e475d4fbc7745f679f0cdb773ab79fb53ba5313d7c0560babe3210&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
