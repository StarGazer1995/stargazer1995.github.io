---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642ZDTKT5%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T112559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDQoGC2D4%2Bp021RRNYExbFIauKNs7AgZISQpTTS1BmLJwIgNNUyaRHKXglGQr8MyNLCQy5SToGJyc1tfCWONHaa5c4q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDCeBsHcgiF3lbcDO9SrcA2SVgLga9PfLAKktZSUUVU2tJCtJf%2FIv828GN1xkdJrREpMM%2Byl7jMvAx4Yx98xRahCxCkTV4jRXMh709UGiAYxiXOHywMdj6tmpYI5lIX%2FQDN5aoEujP2xfUVL3vja3M9FmXTORXVEF0RfHs9CNEYm%2F4b69WemiRYbEFeoacGH2nbnF%2FMJk24yGAX0PWyEoZ%2BNai751UHapQe5X8D6y4pMsT9wqcdJ%2BgJ8aL6yW4GvHzjBB19tIK0uUZUHqVWPXUrRE6NymSi2H8ntj65L44ZVNj8pKchWgf52S%2BIstTc5zA3NcAEF%2BcHxoXvAO6KMsr1OQCFzYPRH0Ev8jxZAFo7UUSpJzir6rNokRFfSy0mdKCu2tX5rkz89SbXIacgOe9CaignroNwBtexVG0X3GNwHkkz68JkY%2BOnmCULG2xugyCDVILflPDCwC06EOFRpIHJ13D20bgezM8qv0IEt64RKfNzvBQnA4pRQfk%2ByooSfnWceciYtt90svqTxm4n86j2wZdsYR6e0jya15vACMCQQV074kVTceIGWeUtR%2F8ZSW2u1XscfpeWUfPkkAFGiP%2F9FrhzSIQfJ188oWUz%2B0htYPrMMDcJCon4xkFGDxn%2FrrDhgDYPSarcRd1tD9MOHc4tIGOqUBiuN%2BjbHUlr7yq4M7kh%2B39bq8ktC0qxFMTxuqYrayZ2DnDveC0kTf28c44k4KN1jpI86370atjDZei3CKQSqWyHG7zNTRss0ynHUekTYF7H%2FS3bv7%2FLR%2F9kc9mtjaMYjTmC5xfzXZw1uF1DCU1Ed5MNR8gGaILhaGBdqgO9NeppHGdUzyHAgMI0wecQb11T0sWC2BOnE58xKRqlbYROlJ5%2BGffcrj&X-Amz-Signature=db0ab0fa846010924ba7139b07de42b8f8d9b6e8e43c27e4c5bf5a98363f6237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
