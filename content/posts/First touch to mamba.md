---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZSKITZC%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T135832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhzN3pGClzN8AWbae2gZWk6t2ccJULKgB%2BrsSNlkKQXAiEA0%2F4qAskkySAZbYLNOpApNXbALo%2BOU5%2Bm7572OjG%2Bd10qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoxYa%2FspO8O%2FvasuCrcA8Y02WW9N6DOH68VzvqwX1XZoahVKXHswbaHvqNMANII5JNdS7ZpzORQqmc20FucD%2FShW17vpA9c7cqpenE09h9X9efYtkTOPt4yCdPzq%2BEgUQnnN49jOk4y13qSBpxgFqfPcFanniyT%2BCYq9z%2B5peIc7DBuDcq%2FNdptsmI%2BpjXfBkwkOFttyUpFOg0IZSdc3mFSyJhBU5S9XP%2BRk0hGFwBsHF8lfNamNkFKCfPuTyFhenwQp04PVIG%2BkY%2FWQ0QNUvbbCfBYuhqt11KDaMb9LT0C8riSPVLe%2FmTzbvwF0Z3mlB06YGrRxSLsb4hQjtmG%2FsE5cAcy48KVH7eDtW7e5JNgNioP3qQ6pa7LOZ%2F5bYjgvw2TT%2FE%2FkIXucVurfz9%2FRXzGD42zsFcBzJwNNZ%2BFLEtNlSZ21gL%2F18%2BVn85Zn4gf3VRNn9MelJK%2BSeWKgWfdgIK1o0CSHN%2FEcYEOqvWvT8Dbl4%2F3JsRV%2BxVSqA87oFRzn0BBCLKCCrG0r%2FO%2FA0sKt9fYYpIUYOSa6IZj5U0lyF9oRrhtNq5c7%2BzBJcHcS9N3XFELaCKsOmVZX3po8jQkSGKMvUWPwlGuWcJVeZrQWN3fZYQQpiJxt3CC3kOCdeZiPEbNg%2Ff1OkdKjisHMKnbidIGOqUBd3nB%2Bki3yhDw1fpWKAP26%2B1G9GOOxD%2FUkB2I3BxWarSBb4lwCKfoR0SWKO2MOXrpeqYmN7gvV8kE4nqz64I5vvwtwlN7Odr6UajfGh0I0EU9%2BH%2B7FLgNE5lNT%2FB4mfsJtgwT9INeV%2FdS2gGEzSCXrYj8I1R34t2jsPghJY7ffNpfjJDi3cPoOoA590eY%2FyfIt60CXnF3BT2RcLFW%2BXMAOXiq%2FqTw&X-Amz-Signature=6cf48102c5a7bec55b60945637dbbe79347428c4edf333bf18076a555b1ad4e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
