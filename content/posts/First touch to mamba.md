---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UGTQQLQ%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T234735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQDwoJV8vvERpWng0sgOhp7bxzmZLKc1hAuXUTHMA8HYEAIgPHk24yqRh9FjekNvsZEthXgShfqIdPxy9q2f2S4U8PQq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDFaz%2Bi%2Bq0gNIWE6jRircAyFbcFSyop%2FxuNMxCPLp0orytRkg3MUpx%2FQMeRZb4lMaRwGgCZtpNDE3sSNt5FGJOnSd95gw72lpUrnVcMP9zegxnJgb3ord5gWXw7QyYyDM87DDZ0EliSL10MsUq3bCWFZK04SA4TOUS%2FwuR4u%2F2%2FTCZEHAiGKY3o6rJF9K2ZQ0GMzG2RflFljMiWwu2T9sS0CX4p%2FYNPG7ZujMJZFjHVB%2FcBsAKAiBNWH%2BN1KKIoCpWzgY93PDcsLTAQsRY8mOAnvKoATxerXet7cOOIj2pWFqFM2paSqdNpdgS8SoZyD0n%2Bp6rZUSU9jcbD%2BmmYZqb3qbt%2F26lIjKZQocF7QNatqPzFrMOc%2FKklXTLHc%2BjZigbltiY%2Bkz7J1f9YV70He2u2OmIZxlLuO25YvOFmF2HC9P0xKrbcan6qX9kDtcWpo%2BWF2mPSp9VRSBEHy7FQvfWSJlw4FfK5cP60JpJ1XOvxZHq%2BT7v3vcN9CW8IvgGAIPnNhm%2FeGtdBplCdhp2bOIRL4uHdJG6RhQ9cW1nyE3PLo%2Fs49xrmZERVS1Bsc2TAd9ZF2rflriWJdBfiuIi8HxrDDJX2ZltAfcfm4s7x2sLWJ4dgu2LoHGeEyStv4jRWLuUQJcSOwgn8CKEzFmMKOp1NMGOqUBSP7mmXv7hrwe1QWES7MPgcWJF7Pxybrd2BDobojHKiTOQqG5paAneZmqHjN1daJp1qtDeYPhfQYTtrSQ85ZZIlE0yZR4LI%2BC4fvX3MgT3HDZ8Rl%2FAhiJtVqfy6tgbmhEvzjdq2%2BAYmxFpk%2BkNEOnt9l4gfgATFMFYY71vbCBwHB6qYggss1MX%2FuIt5t28Gg3J8txxiv7rMKiFEUkmQJ5LrVPyZSK&X-Amz-Signature=1fbd4c9d8a563acbea954ef78036acddc7e835365d6691305a4c94859c7050c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
