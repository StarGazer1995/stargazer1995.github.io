---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REK5B5EW%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T074147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBCqjS0aGM23XcJvBoVlw3Kq2v03yl37kPFRL9548Q8OAiBD5hNixhNSNxyu3CIFTFO3lwtQ6Vny3UFOtLpmjJHIhyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMWFQmlATU3XigY7CwKtwDzAabTe4oBQkvEZJ%2BulC7OcrSRUADOEmgyNNqnl9SiZ1WwU5v8dpUTcBr5nVjoy2ovAXXvOX6ynFP2U9eLcbPjdwmom%2FP1ZPY1qyMWIQ2s2kalFWqNGLcfXprQ7iF9J12z0r8bX2A3DndBNkDuuQQS4XQ8XePsOCriy6C5VvExH8i%2BTnR129wD0GdzjAemCJhwS2EchXtf2NHh97zkCBQ0KrgvtPEn%2BiyeeKXQEOOprHjlB%2BtUBk4PiBIQQQVcN%2BG72rnMWHFnK1bEob3rR3ssLbim54IGMCJQuV%2Bh%2BxjLkzL9IULahDceWAsx58GnQh5926BRsyA44S3Q%2FgpKslnZE7my1W2%2FZuXoFGaXPU0dHvK5mLjX%2BgFl7XBw33lGCdjKNeBNw%2FKhEvOvPxZuuxQ0t6mPsH24u8zilNldry4tmIGxpTgWsS4cU9iliZNtyLl8sbsc2m3sLSyxF%2BOjtAo7MKkUkVGwZuhA9xzzS7q2wPXcK%2BzS8Ox54JNAyb41HneogTNXB4xFqWIDVlYV78I6WeD2tBh%2FsZFYkArpZ8m9Y2DhBREyZVkpkNkoIk3Gw1G9xlRRXzhJwhXUiXWCNupl4EUVIggrXQPfAfUFQwKRQ6NJDV3eE5pFaEi1%2BYwq8r40QY6pgFrFuxGz0%2F815YpO2dlOI293nTrH0btgCdMj1bqbG8eAxlauEEd1UIYVl4ydEHmA2F9qO%2BoZ2YgOEnFh%2FLjeSp2l5g8GQc55%2FqcZ8k%2BsStQQJNayCcha0Y2JpdsVUZmZngHAYfbsngc44Xyd9512TVMuwzvLequH%2FaWCocp4aghyg4gW%2FXDCl3fuEcTSvt4yjg3YSwhtW9rbXFzJQSpg%2BWLYmLE4XVv&X-Amz-Signature=6fba8cdc0d636b4a6c139ec39fe1e78001e07246e3ba7eac978421fb73c685ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
