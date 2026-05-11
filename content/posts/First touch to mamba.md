---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4DFB6BF%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T210947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIBszZOfCOZWZDWabe15slEn7z4bGGfO4JOY7YssIOP7iAiAY06udWtgKO1JgY0olMofKYLo%2FR61dyGJM977r43oyxyr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM96CLL2pCmVINwJEFKtwDPPQw7MpK%2FevE713Y1rAT7JIT7Takf242iOUIfQyj93juZUCB%2FY9sRu3Ygv0a1OLTwype8wpEThmB5%2B3EV6Fv66x3gbgrITcvkSC%2Bof%2FI12TgLP46oBmYCqAvrVRSpn2HSXvMDtcFmzzIuptDhR%2Fkswf69r11GeKeUlDuH5ANZ2fW9IVxHvD5oze2tO1gg%2BMw8PJfkuSzUxiOe2z425lN9HYNyWTYKdZQ8kEzo1DaK%2Fry93K6Otfoe0iH5kk4Gs3%2FSMQix%2FJFCdDAidbEDBCLBWQ4YrXMye%2F6zX4hi%2B%2Fso1KVufYiX4rx%2BmssUJd6h7q2SbMoq%2BnPV52oM2AwEOu3a20imC31QaN05H%2BCkWFvI7T3oTDXkszxm7uS2fqdLQvn3RDf7t3f72VXDzVk9VmYKfWPYuj3lG70%2FTeUJwCAiVY0RsvAlzSgVwl%2F%2FrDjbWeT96PHJkTQR4EBdgIYuAtsOS6%2BMkntZlDbvimg8zf8EdZchxC9Cg0Y4tKnE%2F%2BoVLoKmy2Yx9%2FmTiZ30rXxhKxgHCHffQAf9EpulCV37itnqBa2mQU6aUaaj%2B7sU7gzS2EwGrSR%2FaZ%2F7%2FyANtYqWpKHm7cTPHbz7d5PBMlwuWNthjHJWyTdRZfOh0Wh1zkwnvSI0AY6pgHGJB4qeFyTQagBDgoeL7i8fuiupBmpB4%2B5UBGIJDIsSRXLF6Gazw2%2FqFRmUEsmCheyJajTVZb98iEkABJokj3zsv7ZRXMJL4FWZ4XQvkW4k1Gqi4A8BFa9sBu07K74L%2FzWyB6Ij3xZZRSWCd7HGlo%2BeWzo7nutrCJfI0AeXad2wVQVTHnlUNMF1uW2dv7OimuxFfGKYwWd%2FEc2NqM4mJ5MRjYiinqS&X-Amz-Signature=cfbf050d4254ea6e089e5e6006e98f769dfa83021fcbf29765995cc1aa3a53e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
