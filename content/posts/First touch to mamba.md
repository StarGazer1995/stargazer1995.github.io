---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ONYMIK7%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T073615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIDgUyxja78FUNBZurw2D2dPUIIjd6zh9rBN8aGUZHbGfAiAGOq6CnVm81%2FfBwS%2BjjM3GGMp6DM2gD%2BXVsXKMHZ4Euir%2FAwgYEAAaDDYzNzQyMzE4MzgwNSIMgxONXBtsp0yhawowKtwDmvfbGnpgBUnjEfQjWNY0tHfD%2F5UBO9SfUOshJbPaKrCc8h39XrcF6GMlUZrlvqBqn2DCo00AfH3AD9Y6KQ5C%2FXpNCQy4iDrDz5JykTax92FB3VRb9%2FYI0m6aDk7Y64R4RaKnSJPwQOMqnNHRUOXx%2FZNbs4ELLRSQQtyVx7amxsn86uA416dWrwoCYZinRPBUZPUl6gtZXHLnILQfM5EDiqv2FW5uQr7pE5xYNIdOprjUeNmPsRALVSxrav1miiqt5VbZQkWHXMPkrrZ3TKfRe5V6y2bUKVMukye0Tl0dqhtXqHJJEsLdJ94lz%2BDfwwwxPVoUS8Ni4rmRGwkqmUSS%2FolYqW0CBvzeM5ICV5zA3NdbXTKqmh%2FMnCjGtgB2hrtgvVf6KN8f64Zpz2bZvcuj5jLU%2BTxjRKtJqFJGqgvggUhQ6r%2BHQOv6lOrKkVBrXJjZJVfBafh8ZUnrmTKrsc8LYoToC4xVsXVjkmfQzc%2B%2Bat2pko%2FLPhc3NY%2Ftq1XtIKkZ4rGyku6mDkw49e9o%2FttZ7kcsRtgm0uHQJYa%2BVkZ%2FoXPI0QbartHzgTPbW1HfgmPTcrrxSVBGyFeJ8u1hm66yeZm3%2F%2B1JwdhhC%2BFV7isYq6NVVO7Lz4V%2BeY%2BGPnQwwfa%2F0AY6pgGFVnCCy5CMgDUnWnbj34u3xmI%2Fms%2FJ23NNDrnItRMJShgsNmKhCTyuCa68Z2KFJUN6CR%2BrgvT3rULuC%2BnFiJLnZFPuws7%2BnkCnMDlS2AlnzxxXBA4THpCRsCCWxPJVtj7V0nju0%2BX6cBRAfXTYWDIjVQ20V9VToskqQbmYqiq2W6MjxmckZGTHv6GoIaqTD0Jw0JcC30Tq%2FIi7npdPWDU8lEv7UB5F&X-Amz-Signature=c8293e34630759ef8c866083791953159edce2e10a62abaa56f00d65df9e3ea9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
