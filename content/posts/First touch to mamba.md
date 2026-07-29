---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E7MKHK6%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T081623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8RP3n7p02ITSqHejHoJlKKLYx9BnFJIdGf5QMluIGNwIhAKKrN7as9q2vJfpdxadW5kyYR8ytOOyKLQcgO6vO3XYjKv8DCHkQABoMNjM3NDIzMTgzODA1IgwGuAmCaiUOSZ2AbQgq3ANNg2Wsqjg1lvqdpH4OHTSVQGmuDgZPJvku36CIM4GHPeUH3dGDWjK5wC2Hn8YkBJzgksKnxziBTfzvXJv5SAlOcVWljXfEIPp9JRg1yLlVGX0mP7KVCk7%2FqFd2YyQhpCcqBky%2BGRBrmZGkzQ2pGf0JaXtDPDIThPv4KwVVs%2BP6Mqepx0iIiYlqAX79GI4jwOPn3tsVn9yG2lUqS4VtvmanDjKp0wL5Xyb3cD3KOzjRDpPTbxcViULsweur1PuCTvfjGvhTn8ZKxjqTOzDg%2BLSZ8jmLR%2BcBgboypo4fCbCRTXszHdeKwWwEEX6sOvIGabJZwweOrM4uaqRcPJC4N9KB3iZn2n8YKwHd0WwF3y2NB8oCyEVjgwMcLw%2BO1TLlTRj9kgnzf3%2FQ%2FN0R50ETGIgddJKaO192Z4b1sP8Pjsc%2BTmj8Cs0%2B4%2F2abxIRNbdOebLynpLn0nT5I7LNgOC6nlfU97PYurZk%2FRvqcYAbH1NaXIu7PSjmdGXa%2B55Jh1NkEMrlI4W4Q1uZrjiIugscH2e3J0plJbj0lmeR4EeMjqpTMpJoFTaOfs2YUQlyxHMAmblh5lOBoPvZntlXnO6PWtom1VeOOOrI8Z%2FePXkuvhZb0kTrjtnPOFqMLZW0aTC95abTBjqkAQendwwDjhY5RTxBNzDKDWitfjw%2FijAWtDa%2F7h0b0iPlqWh%2FqJuBc9rXJpZLyZd7DmdRm7e68UVs09ywLsNNacUx8Ps0dNh2Pfueg8leNCH2pl2ttYJu7vmnzOWPHQcDoZRTK7WASV23Ngv1T8hCmyNEfioIFfTdfFzSAuPuLzqPfq7BvfCHOizpPvhc3EkZCeFj%2FLyK6t%2FtY4OujHPl%2BikdH%2Bnm&X-Amz-Signature=51bc2808d76f6e6581d44159ec503951cf161006c841863970bd8dd05d403f97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
