---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SENQVZZF%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T145623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1k7eoe%2B0oyprke7A3JG6m%2Bl7PvZDoHkigsCd7J%2BEipAIgeieLxSGrq3uP%2FLY01UI2%2F%2BKD0Jnn6CIWCC1OGJwpqZgq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDOf6NME%2BVRF7C2cwWCrcA9mfnuAHO8QsCA035UxFQ2ZJZ%2F71lSZFxDiKl%2BfyL3xLe5r9JCbVtsbhQhBZ2Wrz5QvlW%2BuJtYFKZ16kV3ngb%2FSyw6M%2F7NbBLz%2F1k9OJI0D6dc2X1JkisrZrElcnCcCjoC97cGIxy26Ay92XurnYVfk%2FssdnMlAHn%2BUxF5nI3RgzJmt0E8hGTenU5i1REFoDP0jQRTuO%2FBkl33mPktD7wiYuBsAZgcRlY5CRiTyvFikt82Lsm%2BDRSdia%2B1n1ICpQRODMjn12EtOBVwOuh%2FYQZ3Fdi8HkFOIr3plIkWSAtgiSKrwGO3ZmifKWHBlAuVAHc7Jtc1vYCOuHLnYoXlCHDZ5k3TMwb4kPnxhPvM2geQz%2F%2Bvrr0hRrfbV165VXLbNj3kpZRkQGB3mjfMfSKAhOXp3HOJQMBjzhIa9UBfG6PU3yCRIXTZZKVIDSOZ4tVIR1W9Sa8jMVWB%2Funcbg0No6b6rVIytFRQaeHsYF3irxc5EG6FuMAoEiB%2B%2BstMFYDtT5o8yWvhHviLZ9Pfvmjb58kw0KpjJ6torRv%2B8ZV67p%2FyOWU3hL2PZsMqdFr70T2BiPwEd54E%2FSGIjAqYlXmkBLOoN4qs329t8EmoNr4TkwvesRyRAziiv4nzqyTD00MPyNzNAGOqUBhBj6cMHwG1rlro2XvkP48GMYceJ5FQmJ90%2B58ut3cQoGx7LKA0i7YMo7G39km16jDYuuvlD2G4zVOuPz5s12qAbvut1sypt8%2BooCmZFAJFzQoSabt9%2B2E1V37YdXdB5drj6sPStxEh8DXMzGVNdTdnfDA1wv9uG9o6%2F7KUfJiZNL8S3%2BUlLlnUtJJnWkE1Ss5mV7HzpeY39lS4AP6ulwKYBreKgw&X-Amz-Signature=89d22029774fbc4f4df260f7661c265d8f751108bf66b0c2fefb00c03a193d88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
