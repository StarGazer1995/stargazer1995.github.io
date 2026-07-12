---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSA3KAMH%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T144719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCZL9KW%2FlrLJvy80exL%2FqDzROq45XXXD1LGrFOP97DxRwIhAMUP1pcmqdn1u72dtBTxlfDB0pCD8VnNeVz1h6%2FfsXDtKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxCbYlRxiHLSSUk9dsq3AOMT5vyu7QmoFOYelqxq2zINcW9IySN%2BHvWFyu5Md2zCtCVf4IJPyLepHBptG9wFyrTuW4N%2FwBtfnn%2F5W%2BZ4IpCTttIVQkKpU%2BNAa6tbBlo9kacwSstA1xNKLm8ynDfKvxVIIe6BBNdXHfdXDKJ%2BNOEjmpl0k3bXGftQ67wva7o0sjlgaXKu3Dz3IhRD1038SYveYZhFK%2FwNb4EfTIulqRGfLsDQBbjtbbhXwEpJ0NVxJMwqiLh149N39wI2LVremMP2h8uW7GHjxOoWiy3RLle1HSSteVeO5kcZu5g5GAQU6TrdBq5QPkusiFG6gu%2BO3fOCP1WbtCS5%2BTVRvTdqBP%2FxizHU2Bw9adgt5a232PTidgKLPQKnrOyr3Pji%2FdrnYJ%2F3Bc73edrus6EMsBF110wlqimeqL3gulrNyoJh6giX%2FBtWS0mNAnrJXw6K3B%2B6r7FbokC%2BPoTefEHOo%2Fqiw6mtr5cvSV56W62fA6BhwvJFHcGHzdcX7IHhcoJzKYfOhBca2y0W35QB7SoE%2B0o%2BN0LtJmhTicTzrtREu%2FsIX8zKE3kixOFVVsBSYQKvcZmA%2BZDlIzZQU7cpKFoLp2n%2FypvEg%2FnlRTPN8A7xZ8y3TV8F%2FW%2BM7Bo%2FgmBkQhKwjDw%2F83SBjqkAb3XLgEMtzWEcCw%2FouOzMZxQA7%2FjYlqHE%2BQNRoWfm2dft00lvcqsaCSuk1oL8D3IB1Lr0P%2FbXsH7oHghH9ewANknm3fTxIOTA03f3MUJ9vrnkt4lysnHweHwWQI5LfFXzYVND0%2F2M5lXbFe%2BB60i2KVsONRhZnDZbQAzUjCDuN3htzUTT0EsUaVynfDbZUeM9WhXprBPr4VjbAwRtCJaTb1eUKsA&X-Amz-Signature=70ba88e42a42406aed71f4314c2dbd335017ca365b0170ebdfc222088c73c90f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
