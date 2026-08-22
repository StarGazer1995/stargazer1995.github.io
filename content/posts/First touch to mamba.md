---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKI5JO77%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T121514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDErPc9ectJJ1OXsIhJ%2BHZLPiz7s7TMdeDVRm0zl5wazAiADGqCZ3EJCi02ruOt0vZqK4sMHlE%2FgQXcQpqnDA2mf5yqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZwE7pcYk1mf2R9ynKtwDdmlmGiXUKoFIv9AYM6%2FgNiONKO68uk2qjBKXx7bX8L2Qcc%2FkOMzGBA8FY12ADm2vt%2FlFMHFfXsmo0dbiO49dO3yEMyvWRB0IskC2uWP7mk9GrLOqqGMGwHpepYSa3co5MpQtGivzZwZ1JdN1sPD0L%2FCjGujAxePHtak8kNlUnkK5TnlQo%2BZTmBgWxNDvyF4yjOlN51L7evoaAUy5IqfVR2WBG2GQlHDIZhyhhJARtG6hUbire%2Bfxu2t%2BY5Y%2BnTpEJ8ePU%2BUHb7xrpdCM2FTmUqT74LPxqstW9jlqslosKINXVVcp2BuhjjH79QiS1iBoCuTSGJ8sFHGxA3wuwz3xZsshcmT8wuDtE%2B0Z2OmAZRm0PdXxXSfIemfr9pR9BzN1wKTX3Oetdr4KM%2B8e%2FIGz1W9PlxGjVpVYMgfWuVAZWh30tamyL3bdk2wJarfAh9P0qjnZhjZJ8ZHXnfHhiu1CtMa%2Fp0tEeHj8lsqXcvwSsuHcJXFTptw8k3VsyyBiTf%2BJAMZ4y%2F%2FZ%2F2R82aocw6HqA3GaQEojpdCi%2F%2BeBKTHKw2JcQtkurrREbAouBs4OXt1NO8Fub7MrBXOOcY9bAJvU%2Bplwuc4KV6bZJAi92X8wyVXK6g5tdFs8NL7nBSgwgeKl1AY6pgHYUmq85tB0rkcWbx03ZJpNnt4DpHlBx%2B7kJ%2BSEvR0hDdA5A%2BEnj3wofApgBGSYDT42%2Bwwwnbq6GDim3eTTSw7nGgUv%2Brvq8dcno0NF1CqiFifu%2FVWMhRqIYZkJFQ5z9ehQZYmDQuR9uuh3WQFecMPta2PhlkFtUu6kdpEkDdJk8nRMKm2U9JWed5F%2FUB6erQBBwZcfRnkkRPikT41rIfqlSqRf3nFk&X-Amz-Signature=9c1b8b0ecb17a94a33b4b61ee6cdf4b7fcd8483d464e981a083499b97f6648f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
