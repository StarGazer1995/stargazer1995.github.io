---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZUWI7TW%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T132046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIA0ShE5mtdIEJgjI1ovxFJ6FZ6Q4F7lzH68mRzUAvPLvAiBqdlidJIew9K5aDVBJFuaqwriwvtYm0DojQF9Uq5kYaSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWpC9LU1sEOruSbsjKtwD8fOBEZ7zbHAkhCxV1yM0Ld8QLbIcX1iaC0PcILb%2FP7hmBJe7h3FsUF5VgJCWEQSctej1juVVLdjx%2B07GYo1IsahjxlHWNdfpcCIXDXWYDvJUZDnMBTxdI93JLMepMpRy2%2BssfnEbn3j4IFZ74WvSZ9OTI5aDV2oWhC4SEUG%2Fal2YS%2BbIn%2FfptropRqt%2B%2BrMZsj%2FeO0BxlnR91NxRv37vSOlGhiqYp8ihylWDBweT6go2Bu8LoInDsYIVUedjZD18xQ9oseMCncDrxfHkVrsp23Qw98%2B8bg61bnYBMbA4H1QZJ%2BGILGlYyr5N6KQfnbxtKJWjinTAzr2Nrbui1SIWxB%2B4qjlK5n3UvFBs1N31ukVfhJWSz2yunKmspQwKfs%2BF3UX1LA7LTYhgTi9VRk2S%2B8LQkJqisFT1RrJdAtSVN0CcjxmboRfsZkj6ya7BpYM%2F7EGRQ4xHLocOboEq97kWiOJu1QrQd%2FBjRzOVgZ1DQ4iEUVqyIqdT3Lf9v7bZmISXD9Wr4nxU3QTGMkxpKSZue9K%2B1QC6EDTxGO6XLA6zMFsYHqBpXPsYWEWWq6wBAIL9Tl4L8ZIFUo8cTfW%2BRsePzRR%2FC1cM9D66EJEkUtTlpBmo7Tgz33O1zu5KJyIwwPiH0wY6pgFnl2rQWXtlEF89T7%2Fu%2BMs6AzPmMBnXggRbXc%2B%2BzT3zN2%2FU5IFf5LnrUinAtrGoaX5AC0x%2BSxhp7pu4XmEYYJwBhVkr3p%2BAFyK5JClNUuxn7gbZqDvGl6dSDs6HBEsbJxrZlSRNELV11wX3DeB65kyBmVggWy4y0W1oxO8Vbpj5FfusYLzDk25lhizyKhLXNAlg8EaYzIpqeuUZnn0yJ%2BF%2Bo8O5GowI&X-Amz-Signature=026883f38ae92e5f65965183cf6bb7a0f0e447f0c6f5e73d93b3bf01b4879e32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
