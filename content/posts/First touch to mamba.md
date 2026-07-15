---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ET3PZCI%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T130616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIBHeIVYHXET1MgBL3kjkppPkTXEDzwaq4ANlM7Y2PQEZAiEAptlECO2QbIji%2Fz7hVeVFp6ua8O3h4m96TJRuZKHfcOIq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDO%2BgaeV122YwmHefLCrcA1WvJyl0pk8MgZwg6TR70KTwTJ0806lpgL%2BTcDArltqCallSqV775Scr%2FM6waxRFCX9G5fRRJYgHMmZ1bKNGRCbpXxo%2BfUpWjmzEEudePG5stYjk89A9VbhCKnCQMe0RJ8EJmUmAqDl%2BYUyMk1i4nuSQpmEqPk5U6l7%2B8vTaK0d3ifoF%2BXm48Yb%2BtiH7NZS4u3K%2BbUA8zYFN1hIr0zbN2dOy8rB0FOh%2BbiRAFoXXHAYuFo52OaecmNsiHlbxjD%2Fde4esSlUhCpOneUwmpxTtDct%2FDgW3vMAghBNJs0yhywhGLmJkr15oPxDlkvHOam58%2FbjanKGcbjJVTLdYJwy9FOcqciI%2Fhh%2ByhKl%2BUESJOuGyR45xMrHGMtfTA3G31gG9aSnvZXZKxtaJf872JDH70OC%2FxxTlUutKGBBzKp8jSRuo63zNChZpR%2FvgtC%2FzI8zeiiqqjXSVSvd1hioDZ2DdRjh%2B3eXKZbxYnS0C2XRkpydzvW0p8gFqHcJjgIHxaj6vxBotdC1lhl2A%2BZYL7QCnxkgmrTaE%2BlPp%2Fyf%2FJhAazs%2BmeWm2%2BDBMfvnIdG8wBNDvlgoQvdhHGMMVzjRZJ5K8ooPKybwFys80c3%2FYEb6q%2F46nrhtLx%2FcDrY3LlyjEMNr03dIGOqUBSmXnYiMtNpUcBVs2xHOr0oR3mhhjNchSZhWrCby33h8J0LBoRPJvUBOscB%2FUuqU8qgkTtc3erEzA%2BKd7QuM0qcPftDhE8W33HD2X4EmoL6mRZIkxtSUjwtFpl%2F6mVod7PYMBaSw3hL4n5iougHXwx5LUusBOGKQuGbUBy7YWcanaNR8csIASYsa2tCyB%2BT9aX%2Fz6pzRHi4AZuA8mLybUK8B%2Fvj9L&X-Amz-Signature=919ab791a95e5db989455f480ec0f4d9da926026b33220b31f8a0c75f98d4cd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
