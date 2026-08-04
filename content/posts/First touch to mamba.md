---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMMYQY3C%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T045400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQDZC22VzgDLjfvsqkeGRmeKCmy117u4cDFt4lzRv3iO6gIhAMbLEQQbIiKBSpRQ5HNmYUHE8rvnpD703gX4lLbdBDTXKv8DCAIQABoMNjM3NDIzMTgzODA1IgwUw1WmnDTx5k1poXcq3ANYjdWUi3JD6f1ahvQ2A4WmN8UxNz4eSAd%2BraWYnjt0%2BPglXD5RNzkAInBx0cC5k4fITsXgpzEQtcFUhRijqRnaFLrPbecY3Hek%2Fva0eKLAyk1tVYKEl929hIhcmlYN%2F7%2BCTWOq4omMHdqpI1CS32coJ0jYT5tzuPJzFFglD12KDWQCeW2nrWJPPy4pEEGMxkEC05huxXOlV47rBCTxZJ8QTnw%2F1J7q2XlMhtpWHlSrVojaHiyQ2oNW6%2BNCs3QAI6nVPBxdjOga0%2F2vpcNQgsFd%2F1J7i6mOGXLUslU5Hwnw0PuOIjkU%2FiJjZi6KA8e%2F1bsEbjur2FHu3Qt%2B48UBmOavbZM2XL9LL0MI%2FYrDPbq%2FEjVpVpMvbi%2BsyOYQgF0I3Vc%2FA4mETPzMPBcGD95%2BN%2F6LK317my97MciEWM9phKkU4iEZkXy6cfuxcwukW0bBwZmIMR5TAzx57RyFir5%2FkHlwLMGbh9h5%2BdGndtWzy%2FG7z2I8XYbE3zexlm6qDT1aty9zlqyvDnjO6t%2F%2B5NBvKsF%2BF5xPp%2Fl0cwzWip7t6zQAM3gRGkT%2BY59WvKM9Gz6hjq5%2FFuaUVXFJ9ZskvI%2BkI9Wzbx8y5Aqikj3me5pUpXHs5qgyZuZ5PqUV%2BCEqQTDV5cTTBjqkARPKoGxCp%2FAvc7%2Fe%2BOrlKyXJtDI2h%2BDhREUr8m9uUZsfP0FP4DUaaQ%2Ffx8vgdF3kxkpfwIyhfFa2peIUkoGFam5KVAm%2BFhMTf45dXKN33fdUMoBz8Z8e3yN5FCI3g70ccuDlq5cf25NFRPGQJkXVy4kDoBGGPuiOqvF5FqopExNjXOJMTLjkTRv2oKTcFNiBhshDVYwnV%2FJnqaB7GA0576nFeKMS&X-Amz-Signature=97230ca1babc2d7b818b41ae70dd0005da89bd50de6ad08e0490c79c392d8f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
