---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBHP5CUB%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T152527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIBDM5SNLaHri%2FIuTb4OMSaNTpFFvTngxxXEVJq08CgBmAiEAqFKv05rzgDu3VAgrvP5r27Almkmn3gbAxIqg69C%2BvSkq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDFmS1Ms5ye03WV08pircA9Dpe7m4Aqby7cahMHrr1hpXJ3eAICmescaZzMNjNocgP0AwcVG8xcWsbpNRPmozb590xKiviP2TIvwwrCSf4DOgQbOcBj8pKgjpCs1g7T3YkvVq%2F8%2Bc%2FWqZY%2BFtecs%2BrUMG%2Bp2RUDFfyXV3MOF58dLWLC4I7kPrcQF6U0a%2BysfmkFYzLiYbsuXui7rW8pN882JqAP%2BwFVQt8ngmZGXe9r2SuzU6R0PP6jzgnDv91%2FW9OXgA59G5R%2BKzdzPIROskyvxKqEo5aDue7zji40YshXr3YU6%2BS2QAFo%2BIOFy3uQy%2FXjms6MTf670aG0np3mAUPRA7oWGTP07Kk5ZnUCJsRA1fcxEWRIK381RW9E3AF8C%2FbU%2FnQQY3uAy%2BDMDimP%2B47P3xjgYAuAr1%2BcZHSxPwESg09Auoxr4%2BlFdZ3SZIllqB95UssC5kxtCf3Y4XKFCGX6la%2Bs91bWk%2Fs9qoEjD7kTpYnmvpf0Sj23bYgt%2BeHZJ%2BU1h7VswVFe8Q9GETyse2PANBEL1IHKQwqdfCUoMkAarGTXLTJXrOfrfFKq6APtWVhPVJoKJbUKnwSOaZ9xea6Zp3XXsFhTE2KhdxCdfcT7h6fvHsLY0DtmGX5QoTyUCSq3eGNkpOiN6XmGSwMI7HtNEGOqUBaPBm6ivSu1LB2S5mYlZR2N8UILclkeZag3CjJbs%2FohLbJtI1XCXKlxWncx1dwZ%2BLUWVl6Jmr%2FV99jimGuaEAySeDornacBu3geimLRCPNCvdd5bJjfmjBIDnT7w04XxwRuigXOecS%2Bu%2BLyaMOuRhG7%2FV9jRJaDzZHucFi%2FInkrjL59eGbK45529YSlJVJUpQC0CIDAdknF3%2BwV8Yf5fL1vKc1J3c&X-Amz-Signature=8d1e6b9057cbbd5c1410ac27ff453090a4b155ddbc71a5a85220c1b52a162d05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
