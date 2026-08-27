---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFR6PLUI%2F20260827%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260827T052559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIGJ2U5z%2F4ZtFhhELzPP5QfpfVMMret3S2QVdWVKBB294AiEAyL0VZEYhru4GY3gkK%2B7M%2FiTzXmJIvLPn5MVuyS2NgN0q%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNSxSB8lBh8Adk4kOSrcA1DihDX%2BDxriiob6UU343iqgeW7bIF1tJfehm0voZEsb4%2BaVbH8BZa1S6MB83fTlsYL%2BB83iF5XJA8Vru2F8hdRKZoiMXXUxhJXB5Nf%2FBrdnstu5mlszcD63OhVaVZ9T0EmpZh%2BJsnq0ktqSQGvbm5yoqjARnNHcUOwLPQR9zuW6pMn7aq0g5SbwsUN0NWZGQGET5GGtoU3YYra6W8gsG8z0kIhjGKzOAejpA6pMPw%2B%2BHQd0YjjOUWIuWdHXdNJ1AyvDWwUgwyE74rU7qif7LFJo5QNfoHKmlCTd7UJQrc6UfJ4hyRCcf2AJnOsakSWuDbFvGmDRZq8Sxp9G07AWS4OPBkJl8RaSKThw7z1fk79X3JKHV5rH6ZCswWPFcpopK39%2B7uLDP8TrJAaPLFgb%2B1hOVS1voWulaIsQcu56Ekoov%2FkQBnwUsL9byXMxCYtxk3yrBnyreVNYQjtuFdnGgvQFULoUv0VkIu18L9rRXaSd6U1enEdhrftWP1z3LHHjqXjYsVN8e0C9%2B%2FwahdXbVDAszNv7ehO9ivC5ury0a07%2FuhSuyTg3p55FZc8OEr7D3ER5YE7nOkfMNruexL3E7OhBYB7xVeKGFsBNC7nglTWjRNITCslXcv5D6WKnMI2Fv9QGOqUBa%2FCuQSeKCoHPJLNZabEsmyJMP9L6KilniHqkt4KvPKjTaAtFRH8V5nXXcvXs1K3vSXJT0MDkj9StHpph5O6s0TRUw%2FLuGhWaFjNA3vLOsDupdKSn68mFydOSkqZm88uKySvK5isK2xPxeXUnO%2FtBXjNK%2BtF7IT%2Bs%2FHodwq%2FOTUIQ5um7iGwPBXo8KdoJ27nAusKkHwNKoOye1sIyll87ujyvrk17&X-Amz-Signature=8aedc92cb3f0dea18ae2a77e3f586c6760c801abc1570f407379d45d72fe25c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
