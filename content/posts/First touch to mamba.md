---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGBBL2AM%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T115419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBCxQy6nXOoggXuvt7AIROsRuIRPKQRkQi%2B4VaeJ%2FijfAiEArPXK0IpjyPKeX%2FhW%2FDgQ5mTX9wCenzzj19VzGnEmRnsq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDPZjiii%2BOyD%2FgFA8KCrcA648vcc3AvaS1HH%2FmenH02oaiZPUQFDrotZIkD131ihDp8uM4A0CfG7qR6x%2FBxj5NgqzF%2Bzp9%2BKdDyD1dYp6GLRRkQHWb2r1Sr1HxEFR7lCSy1JXHr%2BrOkrTwk8OHpiooYETZZAKnnAJrWZGgfC%2B0V%2Fsj7Okhb7ghvQyb72Bffda2JGcTibHBQ71tjIbVA7If8dpV5HLyfxVTlrZu23xDSt5SAESxRzrDUjMFDN35Y7hwEccThfCNfkJU8lgxwn5KREuxUyXp%2FlFLORUaPXwsoQu1PJ20yo%2BRCdvWaHVE3Wr7unDZlV91ex%2FBUTuU93zHrhmeGOCnm7xB58yb2FUJc6y7ElsPWxRtQOSjoPFcoyOHgGQx9%2BOHobxtWWkpBsPlrY0paFRoacWQWG7dJ%2FI%2Fa7l55ViBvvwZolzm4BHSxfK9a7SvzMXItU3YyHGLZlPIX4fIjaV7j2rsLT6gHTlVxtY2w3H9Kf3ovq14BXK4xA0rxS58TE4gTr4UJ1vQDKluv%2FQo16Xqjvztlo4XPL%2B8Xnf8OxYXzBD4vhzW125MUMKRTYRixgnXc32gO93RlmV0wmNGFnckCBoUrrSK0rCMXWVgdF5mObaqCQSTqxh6Zl3eCV4gJ7zPBXG3533MMqBrtIGOqUBRJLWJh3qoM%2BTP3uPDw2RNc6is9SO1%2BhxFhXLBVJMGK4KO6zKEWzAKM3u0EqRJvHOqa%2B3OAmQbaArGaNZdyRoWH8k5OJC9sHORHUX92SHYFduA8Qy5Y2KUvUSPn4T3eUpcEEyoRFTnLfF8%2FLMTnL4YMNx5PWiG0u6Pdq0liG%2Fy0OUPZIGuFZaSmrGKQpf%2Fz7nDy6Hxd%2Fhs66mM1VfVheaf2oXP2F2&X-Amz-Signature=a3387bc613460617370c1d0130757d94aa3488631663a8c19afe954369820316&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
