---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX3YIBLW%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T222236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJGMEQCIENKZNSbGoV8q4oOm3S0pdRma3ncECP6TR%2FkKM8S7bXfAiB31Lk69Tfr37LXaSBuGBzUMLhvwjj9CjQ%2BPZj6JMjOSyr%2FAwhFEAAaDDYzNzQyMzE4MzgwNSIMGIYOuVcgJzAKWOyCKtwDAAqa%2FMiFr2nOmud2VklmKs4zt2hP7w%2FUB%2FRD9%2B7O4X%2Fi1MDP9LT0lBKCDCJGYXhdFDSGRQuFyBLS7O6Ra6w9WrIynYHn5mlfXkKEaJacGBFfLs1cnz5PH6afwTX1bsApFl9aCo4201W26fHMCnSudrmRGJguAGFcSv9QbDErrOwRH9VccsuEls4x7gfn7QSMEKcB9i7PHNCFrUg5kku4gNKmQ11U0jNR8bG4fmDoTYmGkZDeIE29Dl%2B5V41gP9rmd26acr70JxOEo6fMlHIXZMsvFa6JLUseu8Z1cWVxM25opmVQMQthhd7dMkluRePwfp56DKgAQcarB4KrMQcXgvkDFmX87oiLwaW%2Fg7Xyn5ScYQbkNkkMSMHRy9Fj9xUDIpj5Mh1k%2F208UAhIuNnhAZFrrwNDThXIKxvbWPDTZxgCBZQv5Cvpqo0cVe0PFKlYakcVeG7XvF2lTDmL2TNdFpndwobwV1Y1xuenWhaCslgOcGLsBy4dCHxFy97k8T%2BIfMaK00f9Hrew3zRigdWKuJ4luhejUIv2QSx7CkrjBNqc0cFSKy39E7XJe6HLvV%2BTHH4YhYKraLoAnOL4k3N2PV6EjtFCTX2ZbUalDS29gCaOqF89W0d%2FK1jiODowkb%2F81AY6pgHHxW4yHKjyNI95fpd8SNjQoI66xi%2FMkMowPbqJ%2BGCu4J8zpH5%2B%2BGx1ZgpGnumYJ65CCnQHO%2Bh316n7KRqRuGd8yc5%2BkocYXVgGEIqXtLstbrtgWRlQTCJ1%2Fav48dMuBp1wMp%2BcnDqjjwKrHQc%2BjQn%2BA2k1I8FasGSsTcRXosfgsRIiWJy26OwBb0AXLYhOi087rOn2ngNcMrwjJ5AJw2A%2Fvva8CDpJ&X-Amz-Signature=d6bc463b2bdb4778f58e67e68ca3636a72dbb715d63afa1c04093bd144b4372b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
