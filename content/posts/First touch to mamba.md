---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDY3WMNM%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T024910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgCJqYbRMnybWfflg6mMhNfPe%2BhHbm%2FOVC0xCiY3v9EgIgejqanu9lLuaJsHPvos8AGQ%2BtJO4AQ6oUc3CMjnV18tIq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDMRPDQ78YXc7j%2FKIHCrcA9UpLu%2Fn2iDQTp8K%2FyPJGbNt3OfmvmbhhE33wFqyXIpr%2B6QmwxKhfJkpX1Uk2TXUGcu%2BA5ekzBeZi%2FvK0d0N%2FcpiDbhxRsZrJ00wZgNUIvYUUVr%2F%2B3OF9UPHNITvLhGOKTb3b95lDtnGgljTOsmfAV4EhZN%2B6dCUK5nf5IJGzINgWC8Q5%2Fe2J8DjqZb3vte20T3KFX6wSzm886H3aaq1wTekS5dBAbSyTCnCocVhoztyvePpDe6xs%2B9lE%2FN7aRB%2FX6OGTNXKGd4jmZnG2i%2FIFkSTHi6YGoc1vU6AnTgno5pcBxQkA1MDWbJuVHi0opxbOvwzrRRzeyRKoQ1kfkO%2FgE89wJzrBMjG%2BmxVzYN9gTqZ3YsPSA6VTl0MJqBOfMWxU%2BX%2BemOZeEtcgKgwm0Oi4BxzvFioBZew65MWiHSQWTMvVmEEIRw1a%2BUex0%2FPz0SJ7ZhuSfPy99OFmBIhtKf5vIV8H12wiwNpbHVeGCfr23TCEvYAxpmU3xpnFxVTmjz1xxpV01xd56QFWpG7MPy%2F1md5W6CIfby2VXUzSi7DmO%2Fv7GvEWFaLHcyBSm77Ughm1akfFESc64rSRvCou9%2FUX05THT00slraBKiiKNjRfwSUncA8z%2F%2Fi8URDPNTyMJKZlNQGOqUBda7gUAZtH7CinMnhcEFLqMiGc%2FrCl8wNuz9GUGrDT1oFXJdj4w6dhfexJO4kXqBYIi4Dc4SfNh9lvsWhPXmJte%2BpNnbzbpz%2BCcbel9rqO1hlOKvQvrhQAMUN12qDM4H7lfva2Z1wXm7Xd3OxDkHH9En6IMGTjKUjUoPEZtMDyQ4Tuh%2Fm%2BK1Kt%2FHyAzlzamANwJS%2FtKfjGHiezPCMa7QDU5gMF5DO&X-Amz-Signature=88901d684ae5327595ffed542b46954673b2771835d8f2d388af8e38204baac4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
