---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IC4K4RT%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T193715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDu1B4%2FQyWea8mpDuSAO6o9EdTS42g6vgrsCwankHoXVAIgWWGO%2BTQ9mGud00FjC6b4wHR8vo8dXnYfF0e1G1AskkMq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDr9t3a4UmpGKHHC0ircA%2FFEl9wDICsh9j5d2SZ8qVoyDhY4Q2cMDsuRoTOLIuEsEjtxkc16%2BBnGi%2BwSA1rNr5UnYR%2BGtOYMs9mX%2FrwInwURWeMslIJ9Ed4dWUChMFcjl5xOXahSu7qiniSZ9r8ZSPDYz3oHF%2BgI5JZIQURUn%2FHGFAPTl7jr3C5%2F7ifv7Rf74aUAEAQduSFH2Q2UN4NH6THTT68T3uec8gC5nSVk3uJI1Xv9eLkT2ylcmmJgom%2BpCB4h3LKaKLvcukhcxFBzTb9gCmzK%2FERqNrORCeR%2BmYprP85%2FGXjgJIbE5wk%2Bpjjz%2B2rtnxPCMm70GjpcSp4C16MjBu0pFV%2Bt%2B7xzTgywLMn2BWWBYVBazUUdB1Oj9KCUWdspc%2BlJqvAEYdXzb3Bg9pTwtc6LFODV3WbwHa%2BPCrTy3v3B97j%2B0BwtyxcodfisVFQh6wPmnTK1n9YS9yx%2FXQVKCBzEZAp75v8uAZF%2Bqgg8F6hxdr9vDH1QRGDAVWnDNjP2%2BJLak%2FEQK771iw7lnGj05jybDegFHOQ9vu9BqpyGQJ6IE38wvX%2FBhq1doeCE3qJXJwvAiyLNSq6h7vAVfo2qTVIJI%2BAXXS5etgnF55rRrRDH5YBH5aqV0V5miQaHizhuI51iyIfyZ75SMPegqtYGOqUBHGdAERagEVX8vs6sQe1m1IUjeLO%2BslfbqiIcvy6DXDJcQezEtD8iXQ3r13Gfhx3OD36%2Bv0W8VV0nwpa%2Bw%2BgMK7bt8oWAo8H%2BH1Jn3G%2Fm7gcx9lcP%2FrceeHKqHRekW60rRidN02WZ2ffZ2PcObBdNHQLTlpdJjS%2FSs8hzTmWxVDbNlCzzP4SLeSo1xDJS0c1Tnef1PnJ2Ddlmram8S5sA2bJPKkHz&X-Amz-Signature=794a6b335689149b71b10db9cb6521c0af31bb765c32d94db7741f285ea79f9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
