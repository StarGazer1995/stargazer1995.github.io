---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ONK4RZ%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T064623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzEy50TGIw8BcDPmk6pqlnvrrxTIZKyNjcaeK%2FGFdDlwIhAO6aj5Gk2EUP%2Beb3GzipiA3RTheHvxbSx%2FHR9QcGNj6NKv8DCH4QABoMNjM3NDIzMTgzODA1IgyK1d26VeJHgtOlmSEq3AO3B1SymX%2Fj9QEV6UFeq6Ek77BV%2FfQQM8IFShobXpEPbZhbn6qGx9M9Xq9fIinge12TqylRIQyyasQT7bA%2Bk7hNu900mqUtMlwrg1%2B50MwNtbBN%2BfIFqUq8kohsBic6fKSUfIsHw2VAqqpkthgrja3Joyah3sVf7kEkCEskaVcEC0MmzLNzwIDHJ0vwQuY9lcaMvxjWNqtVftshChHYoeSUUgCGYm%2BCXCZtBBMKsGuuIvaBLQpxq4U%2BjCUwgk2HSiZ4dE8Ak%2FH8ibUdfH8WONoO29juGWqY9QCe6AVTPbjf1dchhj7nM1c6YoUJ32jMEmbjy3jDZKXF%2B5bxrwyA9s98et6HNsigq59V2rxlszqeoLsAAPTMZe3t8wSmAaNnpI%2B%2FgaqWSCTM%2BIyxex%2FVtOKB%2BRRx65UFY4FnY1Vlo95eQSjCVR9FG4NtlknyT%2BF68GbBi106y7wdMCHsnE3b%2F%2FwmIPJTkfpKCNI7KyPSAUGcGKd8xKB7OI2DLvlSje3OtanoWHrZ8Z7PXnQDQfKJe8k5FzHVZgqwgRgPUSdCU4feJA1ihgilUH%2FQx5kNyAKjwBJ9Iwb5YSUrXhX4FMX2iy0FJsqTzWzs37rR4dJCSQ6I5w%2Bh8NHD6tSU51AprzCW8IjVBjqkAWIwuglyMQHxGKjztkbkWlUu0eCNBA8dCiJ%2FA7pQynMRC3Zu3HW8jc%2FuFsiQymjNX9I6pWNJfP%2Ba9jD2Udh4o9l7WiIiVCZ6t9JpxcKHGtJUVux%2BL78BizMWmnaB9C4JSlgpJDmRvA6Nx7KPr0A8eZsvfnxuDNLvYP23xj6nFRq%2BOervQlPRhzfq82tXpRjnYU5jEIt%2BYZy78lngBdhbF2EOQGQW&X-Amz-Signature=80f483a9ac623311996cb4daf5f46cf35516d615045d84f2813958012c9da667&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
