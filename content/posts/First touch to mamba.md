---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZOU3TBY%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T023200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkyZ04%2BmiQNN19ddOFaR9acHR1n5YAwmStr6qNBvZUpAIhALS2xURGTjhzoAzuBaKVxXqFPKznkWQrtvHqCV0btaOwKv8DCFMQABoMNjM3NDIzMTgzODA1IgzQeS%2B9TSBsPF7JMz0q3AOcsMgp9vHUfEAB4GQAUnyquYPDapNvfJ2Q8C6AX7iAJi%2F%2BZUv38QXvflCLjSZi0Rpf7IKH0UzuH04tkoXRUZkC%2F8dKMz4f%2F8VMYOlk8bzMfuO91G1s1PbsolCyejsCjhM0Sr0yxb4TmhDwk%2B5WvA2yfu%2FYJN6BG%2BB3zRbOQbk%2BkRhq3bs72PuCBSre3eurSgqb15d1AB%2FdwGpJsfuEDRbWUDNUccLJZkDuDROKjYXGKxSUjiIgtMANEzSODW24od1cFMJmMG5BcNwf9EIrA0AHv8QyXzexw3OguVBRBUHZhhodame0gerqDqaZsHcFwbmDR%2BdxTudUAEWrObe0fkUc%2FepjulEqqAK88Atlq%2B1FlSvJmyQW3WmcnSm0fmgTY3Wk0QGs7smRKHJicRSY%2BFwP1Ve7%2BS4AGqzjek1Q3uiHxmkzQExm5mvem%2Fr4afzlZ2PyM2oI2Kg3kXjdGUGBPhXGM7CIPSg%2Bft8jT7B0faWvYGO6W%2B%2BiBmbNmSWfrjspxtn%2FGmrnuYW6HXFkVR%2Bl90QGSkXa5uWsEVMk8q7LRbJDY1rC4OgwYFi8n41W2S5qFyJ9tq%2Bgkk2jgZzCi4peIF9%2BAGMb0RleQ0GJagm9G%2BOzyl1Xh7EBWcRkRYNv0DD1tb3RBjqkAe0vue%2BBsesJpWj9v9Vz2CJpfgj97cpF6Lxf%2B21isVEUchlD6FEnT%2B5JHFN%2BLLYE%2FJ3nPtBh5k9AxdNSJOSIYcyr8b4Oqan4OemZq%2BZtwAW5IZRAJYvuEQEQmKWI3QOBihCEdSb1VNT1RPOnLOPJJxP4Q27AHkvLQXpBtbJcBqMauQHSQznh5QNK6SHyHkJ13Tq1NjZPTQaHNvW8u57nxzvp%2BclO&X-Amz-Signature=537df52f225c56d367c42ae1b97b938d5a5e83d129675dcbdc68150ce16734ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
