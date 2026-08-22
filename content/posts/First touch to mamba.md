---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYJESR6N%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG77UieT1%2B9kiVg6TMNt%2F1lMP%2BNhqtRYqfartoMK%2FQJeAiEA%2BSIuNEgci3f6hDqabv5zledX98r9E1weZ%2F9uIgcnqIwqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIDVE5jQ1pIFHj%2B3oSrcAxXkVpm%2FidWJTHRvZqJ8huJ76RDVDn7F7Aw6KtlTxywtU8yiQrJ15IuylopuAQcPeGGX%2BE7oSY8Yi1TWm9WfTvbhaFKF6SOpVktIAvlnvaueOUSwExQONELW1uY1whZikh%2Fm8C0Iilv7c3hfEmH%2FlHZpzbRPXuiMmbkzzA2sBofpGsoKETe2npxauPnYYFNNnkjHqFcH%2FxHi0hV0YCfZ3OneYxCwvi3BdgiSnHnyggSJMOqdtxyisdnH7Upfroul8L4HcJZUaMws%2F%2FHd8G6tG5nAR5FMlERlOu%2BDdKBknGLUxLl%2FyKq2nUQzDJjorvYM0TC12XTRhb25VsFPSTJDtVBaIjNSfPjIuLXm%2BtjSpLuAcwIL7FqCPhjmEClTuYXmXveoqxXDVjxiIpKQITBX39Yxmh4l0we7Qu62lJ3LU303JJlR%2FysZu6JsmBJD8yShDNy0mUgadnRQvoFtPi%2BotGxQr43U7AyjBfN8Txwgs4jDPd23Jw4qRdwETYyJhfAedgIvGs0QrOk5A0QQ62EB%2B9TynlbAV%2BsqnI0anb%2BeqxoUnuK8NSugkumrjrGtqmrAzVl0qlHtEKzSfRRgFsAhMz0fgipsrAFYBcxKKqJMObvycwkjl9OECfCzRHnMMP6ApNQGOqUBQorkK7sz%2FDcoRYt2WwXF6x1QSZkjj0l3bDPWVkvmAJzk8qF%2BGsgdWpwV25Ir4y%2FcUnqp2W63hkkFRjMtVQISurYqSTVZ0aVhXQv7Lj%2BopsEjak9dJsCKjYBl9%2FmVGKWlOL6HM2XIJDeW5q9csusAZnX32SRlkFyTXW7ydE20POLjYscOwJ92bX0Lm2kE9nAnLBQaMkfEPWIQjRj7516JBF%2Bnh%2FIy&X-Amz-Signature=3d86c293aebca87b0a2affb414df161f8f69f6cfe3f8e30d6ec7c20a5758abcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
