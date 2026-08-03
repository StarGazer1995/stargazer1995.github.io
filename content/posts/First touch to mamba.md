---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S77ZIXSU%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T052847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICIpvpHE%2B0l78V%2FQLWvvPDXGkVW2p8C%2Byfq0uu0uo2W%2FAiB7c4ZW8XX7Nbx7n8gxvrt39mts6uGGzN6j57CVN2jrqSqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXGNLsgyK%2BkCEJ5R0KtwD6nTiUGvM%2FL0WESgqwQ3M6MwkgnjTcCGnmT%2FBpPg41BhfMhfis6u2u%2Fl5Cr46KCvhvF8h2v8DhxOT5%2BlqtGRmrInv9j3JpCjG2snBN%2BcsiNpkI5uLKjLm7Ig3qD2yw3tuQ%2FxHDIXk3esu2%2BUOwqGntP22LvJU4IN%2FGeCBDJIsTQxKbb60SiEcLrD8kUXfYjFKS7bE7ZnqCe0gAylDxKxna1MqSLvM8JpIoypx36T%2FLO%2FwYpS3gz%2FrlT9VR%2F9b7ZX6LhOc4w8pxR%2FYtkAETqn1CY3fF791T642c%2BatM7YJ6s%2F1L0MNMtvaVf74T40MxB%2BEs72%2F07z8nxxqEIYB2%2BIB%2FPAkuMf8tsOyuOhFEu3Js3PddFD8Mdl5wwVtpMnTisv67GoF9iJ73UAEwIZw6NPGv70TZyS%2FR%2F6rYc4JTlgihaCBhFVE1GKq4NuKbsxFpAwr0lofntVxpK3Mz4zloyC8z6B93NEBJE%2Bb8%2BtEuj4D2y86AiLRLzfx2jBPH4HU1%2F8Chb89P0PvXEJTEWxW73c7ERdB45YvB47dfVZkEEVb8GkX7K25QlceJ6AYwPop%2F9dRsqd9Au9pGfiSZX9tmF1Tpkit%2F2fa6qkwFmiDky2%2B4MvGBGy%2F6rRbJYMzW0gw7L7A0wY6pgFoLYY1m4B8nywKa%2FA5deE%2FRooNFZOvX3u1DsorfkJtKR7endChqeTf9V32n0wfCE8cJdyhl6u%2BW%2B%2FKlxCl7Eg4dtj2yE%2FreaNRmxFr%2BUzfA0jq4JyU0O7TmVBZOJp%2F81ImKjPfXGRbf6nb3J5hK%2F81tesviqazDx4q5h2%2BqVeXKNi2REUBEDfGCinIYw2OsA4QhYiubG1%2Bk2zCklU7YiF9b651eRg5&X-Amz-Signature=0563947065f51a3d6af68c4f1718feaee35ac1bc142c84d030957bb16b275f26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
