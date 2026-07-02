---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNHDKKLK%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T155937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCICgaEQ8aFlVAk69QNH204wEHhrUi%2FZslnV9nuwJxPCG5AiAI0wSUIUyyMzcT3s6jkF8tmkeZEucY%2BJjaHjf32l84hCqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv3xVRc%2FVEymZGnaEKtwDIrCMaj0%2B1SlSUjyk%2FwByroH9AOnCcPF7Z3yEkrg19vpFAy5j04pVo0k4sikA0FEUuCuNx11xD6IZ9NJSSjtjqdeIbcMcCGO6GplzigjD7xuk%2FKhqvsWZPNchh%2FrLo4u5QNK3JmTXxZoTPyfzJnVznht2hia3B9hWuT2lEcbmFoW6msyJmzD6Hx41ZJfBV1kcp%2B%2BcNQ%2B14h2y1cTKQcTjyYFuD7fvRy4Sd6GiVKzVnqoh9CYavI%2BBhi%2Fw%2FjrbO64c1Q2GP9xX16NF3JQh86C2kJxWoCbVYosWa%2BmWmiXy1zCsjfwaEj%2F48aKzVXPQ1nuB1e56SDpKTTgjzNX8ZQM%2BGKNT4mkCvL0Cyy%2FCCHgrFKnmIdStiSli71c%2FkAnB5%2BE9JNqTwb7eUZxg4O0%2Fy80WqMeXLupxD9F%2FPLI%2BdZhfpfw5UoksxNlUcXQEh8p8rol9ApqtY9qZdAWpyq4pWpYbg3%2FQhXr6E87FOLM7yb4AMLVxTWVdlVr3HVLGSwNS4krvVVVY2YAKaL3UFZkDRT6mBgIxjBnf7im2Gx1o30V7FO5ADHVzydcneDUdPe8RH%2Bmi18mFpDTlWb93MIA0wK2OePfQeWcn%2BUQxg%2FrCcqzjtHIfTD90o4Gk8yEwXLYwt%2BmZ0gY6pgFL1wm3pcqr3tob3Bh2r%2B2NWHVrxJ%2FYTw%2FoFUWP88widk%2BNpovVu75g3Ft7yW%2BpEeTBkPb7q0f5B85PbU4pm00tPmpewlBjU%2F6A5QWPv5cfZXjdUZNOZHE8xEloGpkRVJFGAwUQE5fo34wHBSE1LIIM1gTEq76GJ9H6irFdEhl7l%2FCiJAnYEcbccBUu0oCgoX8LcbTQZJBqWPouNLFdXdYqeu67Nwch&X-Amz-Signature=a93c0a38259af5058a4d38b91953210f09b230b4a128a0a23014c3a218ff09c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
