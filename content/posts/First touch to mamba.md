---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EPLDGBZ%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T123733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDn9N0fhY%2FWeDz0zBFQ3OBXYROQO%2FRVtmIzAOM5WqfWrAiAgeiNn51FePRiEIqhP7%2FfwHy5JfE1uYMrk1ubSQpusICqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM40ODPxTGz267MmqTKtwDBR0OWxYW867w%2By7GZTGxtAPY3FNukWs%2Bh9U1WWen7KwpWTPcaqO16vO81uK7Xcd9kn8OxEjVOZL62ejkifSPLyhPIHIAMTcYLRG60KdvRLh%2BMnlXHtue%2Bkh%2FgM%2Fd6uk7H%2FWW8Vy1GjKJ6LBE%2BihLo3CBKfVU2XFfHy6nm7tADBR%2FSXuDZa3OsEeMpoVsydZCYTcG%2FTuyWJ%2BG1kyu0TtcpE8lxzITLd%2By%2BSOIXQvXO64uQWv24sDsWMN83RA1QUwJHwcU0SWkkVSFm2TYVSv3Hd0bQ4SQ2yTJDGD8EK7NyGwPHx8FSL4OOJivVLNK3Fw%2BRxbB8ZONXEttYCvd4A9JkboHah6Ff3BtgwZ5FlqzbUrz3IgSVjZmzUS0cx%2FkYpE7aBFnED06cdMMFmjo1%2FStAz8j%2Bkj44Sva%2BqcNTYI6Eai0kAE2yH%2B5BPlff2ObpRyRj4gl%2BoBtcAcDrIduTLme9jHgjCCqcZUbikrZF6NtrgFcifgZmUaLlDeiu7qvuGV4zfV9Xrok35u1GQFjitBmfyPCZOh9vP1Dkbb%2Bo5cexiyT6JQJs5EY2%2FYMs2tBe%2FmJViwO8%2BLGz17AH%2B27ARxFP2PN3r77dl8jvZTQAvHSkTRHB%2BS1ukbP%2B5ICK%2B8wie370wY6pgG7RO9P9cLsFgV7ZJXA0tOIPVhCeIDipguTBjccwEbIOXy93mdd6%2BW2Y%2Bvyxas44Fv0DuaNK0T3jZSwZFsEl%2BYKzvt1%2FhW19A8N9ctHe6D%2FyuaaCCE9HQJZuc0DH9%2Bpri5qdRFWpTVtNXnWsEe%2FZuFaXUffZWnvzkFOgBD4RaolmstOdVitnjSjMbb6boFASd9a51OiHmgup25oagbUzOnaD1XDgkq8&X-Amz-Signature=0ce693b49331f172727a98154e3f9eb276b63591b9e06eb56b8f006ba2482c11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
