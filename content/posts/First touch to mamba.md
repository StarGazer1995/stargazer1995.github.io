---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMCF3HPY%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T032507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIFoUj%2F3e3Siym8wXxbrcz3vZQIelGyXn9SuarA2vKkyDAiB4nUrt8IS%2FDdfFqYbJ71yRNNKq3fbByXTKMACZPlyXXCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFZR6mh9kzv8NMQFBKtwDXggdij6fdxlDwh9ZHMIzh%2BcIfMcfH3lwp5PVwBiRDGTO2qJqU%2Bmkx5%2FSI1GrwpxBSh6ZpGq980HTe1KF23OD%2F8X5tKExQyPH1WUaK8m0RNeZQ3VE5TZkZU2BeR5eesT9mm0KpJUYfBB4AZySyTdGQ744EQpPo8iK2sdwtjKCWstjRNCSR0a1z7TQqeC8tpa0VvlVBbScypfoJTGUbQ5w%2BMDDUs93A1eajQMQ4aFUo1bFoFQ7icgBdyzPaEXxcK9x6wdBhrs4M5DvWw8RKfIZsjarry8ivd3pt%2B%2Fib%2B12woU5REhjwDYdjngLkiACIWIT3GFZTKWrMsMtf8lzGCwLUQ7g%2BpaBNXuAQ1m0tHNvMQ6FKELBx4LKZb1e74I%2FxobdGRxt3Kbb51wcRtao3aCdJaDxPcbsjL%2FFy6mQ124InnonjuH0sM%2FNx28ZaINEf5qsaMgEevQqFsI8zZ%2Fg7VHt4xTe8D6hoH%2BHaWWRJgd3z%2Fzg7X0vid2StAYtksi66HQ6K%2F5Hb2ucqVwoaDcqItTEsPjYI64Ux2Vf5RfEpEEYN45BQidLV9VG3IScRjj9%2BV%2FwEE2qotfylaP0lJ75Ea7oWo0U%2BroN9KUS5DvU1VXirQ7dYSJIq6fXDy%2B7sfswps3L1gY6pgGGZk42ZeNikS6%2FdAb%2FyOgP6jXkKf7uhOsiJC%2BGgTmp8vKyGlmUExulAVtiO%2BF%2BIcoIajx9QU2pz2AjwEn50NdwDMzHIK3PFy9I7mZ8Z1aLe0F1HKqrf4cqPuwmdYGV2a%2B%2B3z6Umru41gdTFPFdjb%2FZnTp3aKJtlGKIYhdvTRAO%2BJlFi04yQTxfB%2Bd1y17slbjC%2B4nfAWB4ncfQiu7qBHTMmzsdzwj0&X-Amz-Signature=aedb3660b1cee7479792624b3888559c50e3d3abb5a9068d696874185799db7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
