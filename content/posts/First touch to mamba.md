---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BCWIRED%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcJTt0OLDsRlRC%2B%2B39asVfz36wEb8kaPv1d5oLncg%2FvAiAZw0PAv9zp73eDauCxhNZX%2Be9fX93HT3o%2Bi9OhAvf6OCr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMPrni7C6ESEcAbHJYKtwDHBGfRHwSRbdrb%2BXVbsc374dkS0zfckzF0DrxBa%2FyaKMvs1CFsr907tf7CrQY9aqv0583%2B0cRZBtCk6ykN1cIPKT%2F8ro4w3OUZnoU3vYLzdWEnK4oe%2FAWK6OOP2ANhtZLCYK2d9H3vejy44pjIRVUv6rWx01gU0l2%2Bu7kPf6ehyxcwM7Ox1w2fDQDwRmywacYMR%2FaIo0wh6SOWyf6SxVoLfuZGkANs7wHBp0CxR3h9U5F%2F%2FfdWjdKJcRNsHw%2Fd%2FHw%2F3kVogniPH0ktWQ5CqVHVBzG6%2B3Fz0Or6FiyMvrQXRaPzRFepvSAWNEdkDR3cpMxSW%2FMjUM3k26YImsJM9DkTiHf61ueVhJyDAYg%2FznsYMcGdgqwlJEIkBXxjlCkeP16%2FnOrPkyVte8XIz8W9sILx0esrPeIMkO3fw4sIcMMqMKXPZCirAltlF4pMzqodzKZdmgBt0RlkqIu7o1C0sMPe0vQqqsb%2BYgxz0OHMrl1wO5%2Bl5jyFXlt1YrmC8DwNY6t6Pa9kFfGJLrnbdOxDqFZ0DPTB6xjg2qwN4314Q2mPPV5w%2FnVkirOfT%2BGaqzP%2FuxhAZC%2FgsGTxWIR6WZD79xeDD0hHboPcsN85nQKnds4XnXD6vmhcfxqKRmN6igwkpvI1AY6pgEuLb9pT0t9OtEBh3idnKg4CGuucQpsIFtAZIWqFC5Xlt%2FG%2FksakTmY8%2FLEnxFRX7DhGy7nw9xgn7xXvFlM3Fnl3G5uaz2NRoWiYN%2Bqk%2FwSyneTHKrHdlgIv4uAQABKDlfZH4j1fGpLG1ZsGZnJVeFZwoTgCr7xairYwYpBUOhV8rGSVZItb%2B31pKpagjVNfYPml1yHyUlR9jWYWiwa5gl7WBqXUM3P&X-Amz-Signature=89e9520fa0e8ab12a0d6d7142f69376801273429f1ecfe9f3e631fb9fe26761c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
