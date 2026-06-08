---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSIQCB5Y%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T172012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2BYRFhVW9E2MAgDoOFdro%2FsAEZfQF6PCoVxzZGiRvnAiAHnfbmdYUq%2Ba4PEZ6GIH3y44KeO%2BDVLsUKJiyG4kxRbyqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKE1LMRweQg%2BLJfrGKtwDNqUFKyn%2B6w3kTcUDkoCoHXTrsufWGuOcNvELlF4NtxgDym12fpHp4JvRVj8lq9ob7%2B8vUAO7%2BXYPwDSzfstydSXxWutiKCegFIXpS9Tpo8AZ6tpQRfXhHxGxwa6nNTPJaopAy1h6kfX8YCnrIaCurbxhks3tDO8MWrpf85g04H1mrdBshzqcvDX6EVCf8K%2FDdUKia74KdF76%2BLvzOg80TxKEIit0F0W9ZEkZdXi5U2lL1UZZYj4QpbN7WA1b%2F3pKc1zzhAI7eotEdURy%2F0zcp85umDjRWdZtZocbAYwgSLnuecvAUNzjes3dQlEi7V97P8Bjx6rIPAf7pf47kDE0jkuZh5fOxGo%2FdCeY0AswQOGQ77O7%2FkhlGpLbHeZMpg5vzXYyTJfR4yHCykX26WpOIOprC63yWFcCpKcRB6QKZ3fd1Oe25yc5frcwJcT10a%2B29tDmUBKaRhgLXimwvdE5eEfBzS6uD6DQXg%2FlXcfaFfs49FP8kWfts3QBC0vCq%2B2WB54U5N%2FzRa%2FWa%2BYJnOIWX7ttmLcCGXYmFWSsKnHe7x1KrvhIRx%2BJdgdvV%2FfngOpVsOf6iID3Lc1F32XohyGtEM0fEhS%2BB3zURq1B%2BEaEaNdhMZV1x6m1nmOsFTUwjqGb0QY6pgGykyvaLpaopWUIkpvx1JOsB4YQz9cAQ20tSdC4TKEDxZB9LPXLjGcvPXZTQ%2F5enjgCYsbsEAx5p6WbBzXA03eNcGd1vQ252QGrMVpMgQYulD6H4AXRB1%2BJ8RCtMoCfAomjhwvGoXqr0jRwQNcMpwsApJ7R1XL6lTMw3dSowYNUpT7BWZWhEytONHyHqGG9JZWhQZbweXZD8EqBnKmKVXJLoYGtZKDH&X-Amz-Signature=b8f19c53c648ae78260df3d13cde004cb6b40ecd58d805acf3597f51aaad1dcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
