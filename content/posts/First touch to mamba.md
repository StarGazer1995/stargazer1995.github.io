---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BFMQ62E%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T095426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIHQK1gy8hvVYQNS5N8EBfMZa3zwmoX50sLulaDNjhMNhAiEA4IfxqiOxjuwa6KU5h0vEBy3%2FQQRLcGiUs6mTu%2FFF7rcq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLqtGBFL0ycBfEeH1yrcAyFwfUD8ZsIce84%2BQWrBvvhB35tWdc4Is3roiIfqi2TRXQTjcqvF53Xb2nM193yn7UJIvYDO7ZnluG%2Ff4p7GDdXRJcMeVoanw85M5XE6Kk%2FUJYYNm6gmQEg1swxvjGPGZ2EBZT6ORPu9dcG5OFFaeUnR0hwVcVzV%2BHgltY25WJNvwE3PQGqkmk6nYG%2BNcN9IGBk0Cqw8UPkUAwIY6w5lJjDtpXQpTW1WzGqYEPHPzIjiWOnFrEpTxBr7GrmF7Z3ejVwCLKXlNuoEp%2Fx%2BYZ7umGzx4AKTaejZjjrFE6otVBOdRxBpWX0Pds1H%2BKGCfRQTJo2WBiZjDQlj99uoDyzhKQBE6tVhyXSNeabnBBE7e4JqZRLfiREGFMDkNCrx7NvKdCJVtlL75QAcCK96fy3PtzPy%2FBPziAAjS5H7LqEzNx4dxYull0TBX97QIktDOzWPGX7RqA3tkX%2BDY7mrH4AEn9TXaIDrtNomoSHboTTmqMzS7hCDNxV12JF9Qt5itaje2%2FDhjebYEIH%2Bh%2BBWLpdkegLIYaZW6Ukm4YmrZOezRQ5NJu9fBjBEd06pKoL1QOHeBbDZ2uLNTlhhAPI3MFHgt2tTb%2BGNXrz%2Bfb7ccwoVb6ZWrz6ri%2BQuLTGF3Z%2BUMOyn4tIGOqUBo9WDWJJy%2FGn5RYsDoBWr2FJI2taemPPX67teqsiK6mTpX3K6glhxU2LLxLlsC24Qx5gbSz0ET%2BcbAWNr4JNf7kqRYBByIG12oWU%2FH35Xfw3yJEPLNKLp62ZTx4SYIz2qGOFOuN4cdHySQm6l33MftLmXrUJoUuuA%2By9B2BkRcUFkbBhyCX%2Bd%2BCubj7966xXPsEbXwSLMxahHaYr8jf6bUb6PpmTy&X-Amz-Signature=beb2d32abfbe63d51b10417271807a9d6a46a1706cd1e1b5b3d50c7dfad388d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
