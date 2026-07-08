---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U22QZ6ZO%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T114141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF1hs1fKLxAYc8kb6q3ut1EWN6dU9NaihoyNJ59k06zSAiA7prGc7NarrKQbivEj71JYx3giFC1IiuWMZQwU3OVFISqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMggjbgdnrQBzlPBTyKtwDHwBQYtiSfjrQ%2BxqyC%2F66RD%2BRsgp6u4ozcfbnA6cHBgUX6hZwcbZPDMZWGl1cISW2yCdNePboyR0F1ejNaN0cZSLq9LSpjuudHvdQ5%2FJjpggMoR68tLLK0GG9tsFtozemGNPvOVOlapbapa9sCNWv%2F7d7UDIN0CWmkTvsD0qdxOrjajpY6ma0cHopPGzckZYOpy9KWrajXQ1RaWtKORrV9ytRkzDPXW%2FyWpwziBnQuVZpAuAcQZLGRf%2FagdRNNs47aTkLI9kBxH84SwgbNyxNJTBp%2FoiLobQwZNeXfirFnKDVrun0BO5P1LLzELJi2bpIzPrxFS0fsYB%2FZlcYe3aQbxp%2F5lqP%2BFs8ikC73PFjp7vFeoSOmD7cB0XK1EZIzX%2BSkYiuOxj5elXO2v2I8FipkcYlJGc8MBeuj4KVqd8uLtKc4vRAUUChRp6uHh65LxWo7Dl5TZAbQ1zr48cJ9XJ0cxbnwXV4VLuSQI4XeTQ0tC6qk4IReOfgnd%2F36rY%2FV9cAgqFZQxJZfYtxMLgZEdMBUVJkC8nFbtOQdYh294GTvm6hWMPD1NPWJduQYTuSv%2Bv4QfP8tMLq826WhMni8EDxowKlqhkNK2UdWfuVLGjr8mkD%2FHcCrRvY9CCRJ80wob240gY6pgGOfk8a7yEjNxq4R7AzNYLWSWvxojqh2TsxF9XctfHwz0kJHv9ZoGiDGSoN5Q1FR5pY9akcahlWaMcWVU2f7BHNnSKiH3rAXsd4clHrdc9hjHkVS%2BktiaNSYU54DJZyVj6KOIJDZVwT4I4aXFLKIV3lpHYmr%2B9Q6tmuKYobXK9dOAf9MIvxCGbF%2BO9d4OXZzZTfKEex3O4Y4Rqz%2F6e9VuyFcpM7kQ2d&X-Amz-Signature=26952ee1e7d6d1d33303ab4a258cf2175871b15bb8105ba5085499c0a73dac40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
