---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKFKGZFD%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T184513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIGIEOFYlEWPQzQ4o7ECNg7yIAiNLVm0nB4qu5kRdBR57AiAWFCyIAlx9wrCVv3%2F9EDvv3oRwOGPYfA1JhE2jyyTs8SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOC5UgrBFr2rodAXZKtwDeSq6hqgxmyXPj9SCsOe8ATREXQPydbswvrjEZpnT3zFLTktF73eSh6I3svi%2FsO5YiRHE6b9gh7gZ3h4BW9sunY51sXVmmXuoG6J%2BlWDF6RBvvbRArgGx4PC%2FfhAy5yURoxn0VT65YDOG8ogzHZcXqUEZ4dUznEh1Ch2pVaq%2FehHRSWHdzKW%2Bf4MQ8yy6jiyI%2FkRpGL6lLrNe4mW3BXmEHIiUgRdkP6O6vp9ZQ0Q1aaoBu2dpqVi4PZ7i%2FYoZqPoXOcl8HVelXedmHZ0VxUWjNSqLtTrC3oMizaDz4aL4YrSoDizpBpw5SN%2FiVT6OCy0gQzehLJBJ48OHBqpOZ3l2tnH43ZixzxlmM0Xthl6gh4lSau16Rj5CkgURW57jL05tNiwrfb4SzrtG9GdXM%2FjaM%2FrkYSHzRS7a3LOzJTqsooQETU6wA%2BbbsOyXebxQryGjLQZU%2BFCv19oPt3beGGl0UY9nBSbX%2B%2BmIcy9kVQ3SfCE7f60TMLLG6yFfpeIfPrrBSbsiRQ2qmElzKLYmHWR%2FyJlu5T2dCtYjvH46%2BsTgyr3chX9lDTWVepN3Zx0e25Wri%2Bp8l80x40%2FAK990ve7vQ8EKNl6PZB0Vf3bRZ%2Ftit6KelMPFBcm3kJT7QwAwjrLy0wY6pgEdo73n5y%2F%2BAjUhw04lQ8qNOVa4iD6c8z7UduRtbUS96i1von7FDmKoJbsOFt8i1MrJHXwxuBx06vv10w6E1F1g%2FxyZX0Kr5jAzuqO2sTLVAWRiy1iAGi3KNf6PMlnjq1pkCwsp3MYYGU0LbMqOItLU9GZYfTkczmWMytywwtjntBN5spgqUt3h3u0lUsWlGuuUbB%2FSJzwhuLyaM%2BHFG2Aup4FDgq%2Bf&X-Amz-Signature=913fe7578ce30cd6bd140d9e45fef72253e3bfc9e69e3b08e7e7d888cdae12a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
