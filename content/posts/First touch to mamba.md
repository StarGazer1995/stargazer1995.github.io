---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK4OYRXL%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T225030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCng5SavSqsWwFO0VHlaMhT%2FUVg8wjg9WlOs%2BnLW%2FteEgIgQs40LPozJTvYupPRWGlp5kp%2B4O0AZHCe78Nn8eWMiYIq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDFvbtg7pioMP9vynpCrcA9N8stKY7imza3UnQuz0Da3hGxPsuQkFmzqbaaIvi%2Fe5JGJI2WsBxMhK%2BfyrvI62hxe73qkSNMYUzQJ7yjk5gpovej%2FNY%2FkPJpvq5fXuUBk8%2BNVvL4%2FtBb7ql7f%2F0tj1zsRx%2FyGqjLcxGcxtK1G2n0DLXq0h3CU6refWsxe2BEJc0SQiRvW8YX81kWS1KjvSbEJhAElP6mXxY%2FfGnjAyBhMg5pnDQXRyoZGSnCx43q0IPw3yySKU1KbYsmW81b16KDviv7b9TIK7E5SOaCBzFDVSjf8kTq%2FGVpByQ1w8CpTtoauhN9TCoDLWb7I%2FmLsMmkeivtGlJWy%2B87sl572H9XJ42A5qDWrjYgBL0YWKMauZdIqGA4l8kwAN63LF7sKfkxe3CChgzJ7u673obm6fwYLyEktHgKZQ5ndh4jCG9wIjrciOeiN5GwC%2Bpg%2B1engo%2BHFkTnHSCYEilxzK46moIltOCczq2QvpGkfgblvPVg%2B2EF2Zh29ZVQjgU3%2BP%2FxMiP0EzZrrRjUV3ZtG2rPHC3PJwGCFwdEX1jQc%2B0652mft5uqNOh4Quc%2BoX4S9xltIpnMfqXUHqHs7dqFTPf6mI4RbJwKLlj9WMwkoFFUfJiUiu3LB8qG%2Fet79l7wOTMLXjpNMGOqUBM0NLtaD2d%2Fbw3CGMthA8%2Fm2GboRMa9NMXLzLyfR9fWknv3wxGAD76Fu%2BlHuckm3vRxUedHJ2b%2BFMnuRw0YU4Y4KthgA1oHc3lmqnuenxktz8YdUzpJoJp%2FtP%2BYM8ykQFEZ4hwUG%2BH%2Ff4C0JD%2FJ6iMDBj0oXvpIBITt0QkfyriLwNPXKpHAMAHSMmM5%2Fv3L0cPp3rEAMcGGOAbiWCEkGlrAnJzj6n&X-Amz-Signature=34e31dc70f606ca488dea4595b3241ecec4cc91301cb2d61d8d25c735b4ecdb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
