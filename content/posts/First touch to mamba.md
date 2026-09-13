---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HOTSQFR%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T215830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIB3yuc%2FN0h8NqBt41L4Mr6Ywskp6wcyR6Zhyyde9Ra0zAiEAhlSQe2SuK33Vld0M7P%2BuIj94K%2FAU9ZH9dFZUq5lIQhUqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE00K6rw2q7d61UqRircA5bdtwuenCpAP721BqlzQBl3DbeDyt%2FSBNJP73%2BECDtgtR6Ya9Tl5Ycn7BxmqAgbpK6AiN4GkxEJrKnbBOn%2F0sQ0W%2FjyBgFMrS1tRa3ygkzpdqDsqo%2Bgg%2FEtfxPpzRUXHTm0jEKukVb%2FxVRD%2F8JEF8PD72ewMmsu0DT0iyO3SNRJ4TGBd3IBs89JBx6MngwSTxxtCpTY6hFjoL0K26fDgwxMc3ZbGEAFOZgqOtB6xkbEUlth1Q1ozNNOCf%2BJgB3vbzr9Q9XQFoM0rtrcks0AgveAb172fAZnTSkSWOt7JUi5swTX%2Bu27rL73%2FcaGHN8xjeSK1ryVOYOZiO3oOrTjuYfmFhhd8XYq%2BoDhyZsyDrTBLLYCx%2FQlao1aqbQfySYLJKfvKCyeV48oUMNU6AIZNwMIOCDrUJxgDk0Oi3yP4TEVIFcVtdumb0O1m90qs6%2Fiu95tTvR4lgjBqVvghE18IFn2m24F%2FesqP9nbV%2B0p%2BLVQG974yqnTpYdSiozuB5PCcMMAInCHHUM65n7Hc5G1datagWs%2FJnb%2BvFwubukp26jts1zKL4sKkzlXRGmCD3%2BCK2dVSBSwB9DZuImBjaNVgkOp6M7bsAo3xVBiY7PgxCUyjEK7ufzaY%2FApmSUAMI%2BBnNUGOqUBRvcCKHwlZXDKoxFBZGO2vyagOQglEZBxHNqWkTZf8nq4CQGE6qKDcSFrClChjFGW2Uxsau%2FqBQX9g2ZjlpaIWNcSBIGJxSIx2nTaieou%2FtQFrR%2Fh3ev%2Fsl2NYnC4LbYO%2BQTD0vJOweqLNQCwYtJYn6d%2Fldrnn3Bq4HLbWCbIRXNriQQHiJKHr5siXXERD9OxsKpdmQQWdd%2ByDWCoUzmHLM1dmMux&X-Amz-Signature=d196291f9514119ec3facead7c3dfa669ea8ba0a1cb9701a3487c240968d94d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
