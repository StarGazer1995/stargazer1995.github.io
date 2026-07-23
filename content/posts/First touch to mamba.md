---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EZ7H6MA%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T012912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIEDPGzJpAVYjaDAYqAtyUQxBCEpA7wwShT2nIU7gqQ1cAiAUMAA7P3CJy3cdwdVYQ%2B%2FcEQL%2FPBx8iF0iYwCoLm0VDCqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb7Sd5Kim4kaZjW5RKtwDntslV%2Fg7tmjtsg6xehm9xszNvaIFr%2BXSnEjeFCqCbGO7K%2FhEvKnl5aM%2B7PRVYLCXkmdDhBMbO9%2BiNe%2Fi9tdTsDyeomIFQiA4rQIBQGmR%2F7Cft6O9f2VaV0yILkxn8%2Bvj1SS%2B0EmzBcq%2Fha2YEo7UTPKy8ZObhRMBV98P2L0vNhp34nrP%2FN%2Bem5NW1sEtDyDI8vZER6HUczX21hz9ggAPtaagbPxDOVjeqxvwvTb6JMZH7SJpcy%2B0XU5HFIm2l%2FkjVHwdEqC89UyF4nGGvk475kdPzsPVo0jVjsPT9b8gl3FVwGDu8qujnit1cuaYUfPXzH%2F2hGOhoJZB4jPTTZCQJTinmMGwWEv6ScZKRqSQ41xl%2Boct6oBtGBbpziWP1o65dYjESfUq8ZbH8c5z4Zi%2BvyfocYEqTqjanprauhMhxzbU6c70SQuvptRm08AU8Ehvy9xHNskujJBMrScu58TB78K%2BzNnxlM6BPID8o0O8mMQHh%2Be90Bi2SDObICcBW09wGBnPLaeaXOVac7ht9E4H0GgRmjmWREf0Mc9%2BYlJH1a5c6j7mEKSz59EzDt4a5KoUuoYpJpCyg4rF2v1PsaSFR5e2fTBEVh4z%2FZXrL4sYQly06GheM%2FKl%2BQakPmAw6cKE0wY6pgG4iy3FNPgF4KJS1PcBy0R%2FEHz7egXt7h7MaeghYvs1Tco403mtU2bPmpSzYTHmMKBxoipv6Kz4zG3%2BdtDAtHvmtJfW5R%2BM5oAz9jp0t9f8GumQ3wLyQrTUccFGTT5zqcsY4axckdeUafa0R7WStIP%2FYsp4D%2BMYv%2FP2s0WJ7eJpdkKNaW%2Fee%2BKoxal6G%2BKCC6J%2F4j1WnX1nBb2LXICgL6Gd99%2Ffvn%2BH&X-Amz-Signature=96fc7f18fd877d28e84ec1cc12a8d8a2a64875183b13497967a4f2b49282a25a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
