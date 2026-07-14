---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZZT7M3Q%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T011604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCZmuEyZ9n3QMxKqEXMEYp1rn6rNVQsGqhd72Z2B%2B%2BNQAIhAJ13mbKs40i75T5jWir0%2FyiXJmuTd%2B9jKS3tdVaX9P%2BdKv8DCAkQABoMNjM3NDIzMTgzODA1Igx%2B8Cu8ywKPlUP3fZgq3AOwuJpgSA4UyM3DF2BnTqFu%2FvulzPNJSmwyNIZKmw7oaoC8ArPhURQcviu0GWnWc5A6mfU7FJ6pP2ZQHcn0BKiiqcaWU66up%2BJI9WYrTKtcwJ9l2qafZPJE2HO3eQDP1HomG4SgdwLkUblPjZn8Yc7OfzZDw5%2FthQb8KhLK7UMGQHtg9mkv0FprhnENFX3laCB8hYWTIRNS99RDfLGG4OTeyUI55w9OBZmJDLCxOr9%2Bv2mLEvIgA46wusRLU9dbPpwhyIyKQmXS2Xx6QpDVqoRAFeo0SB6wr5DX6hem3r93KXyTkS3sB%2BfYqIcKQ2XWdG1oa3Ix3UKvL%2BeJoxZjnN34J2UjLfri4Hq5VyjJ%2BB%2B92LJOBPgzkkeMgdqFPS7ZNMskSCwk8NFzAe4eNiTLYMJmPUCRo8D%2FBnNvVR2E%2FpuxtwsNJavi3919d8mz3YmaZ2DmMstE1vtt6k%2BtuzpvS8jBpVkrffNwrnZjF2Sptw8WWi%2FAR1xyMIb6dg78Z94glbx5Og79i5s1bLJ0xOzP%2B9R9SmkYcLLI%2FzQhS7xlcB%2FKHkTAAvUKGxJLCDnkHbtlCEINxgP0zfxI1Gp6bf6H%2F0ArvHkFIHGGdzccYML1%2BTRN6hkz2GC1l1cmnCIqiTCV9NXSBjqkAXyCD6sVwtSnsW0Ji16%2Bg8G7NHh9%2BvDgTjem1tECLK49Ca6cQ0vFpY17WEET620pbk2VTqCiKjAIePj2dzEIxctiQbTFyYtNWsDUGk64B8UrfShgN565kpPoJljMK2Dba8tsQDBFtcyLTY09nyLof9G%2BSK91BnyZs%2F%2BIxDlkfxnqcRT5GJ7r93H1C0hHf7b5Y%2FNXy5odMZrBA9vrZAz0MN0doOs6&X-Amz-Signature=140905ea8d12375443a8b235a5aab1a9ff1265ab6eea896342fd1b78d2de0c07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
