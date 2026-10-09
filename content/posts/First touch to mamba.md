---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626AFZVKH%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T215747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJIMEYCIQCScY9lpYfkWpk3TsfQdL5eSGsSbMV1pZxhVtNiHw5tbgIhAKRgEm8c7nE8c%2FbXMhdpFclmq8JxmHSUOHWJG6D9qsCdKv8DCEYQABoMNjM3NDIzMTgzODA1IgxCltDeP7Ri8tk6Ox4q3AO8CxxK%2Fth9l3w95vQo9qJKHi%2F%2FN1q660tSv6DeuJSHv8JhKBaSc4fIwHgtYR%2FschLBM4nbjUaPeVPBLzOzYOGsb5JUqIcRNjfd%2FFjXoPS5Q31ZS8iuJnbOXh597BLRS7qWvB%2BAQKh4PqRWaS08HK8DwBl%2BaLFW8vpis%2Bqd7JU0NXa9uwKeu9IDQKBp7Ly6FYOpfOh2Hh6jKm722OiSuBAeDlMyLQizT%2Fl0tenLsqv9kY3kymcP5wujNC2f%2BnJEBcMCe9v3tHFOAkSxX%2BlNqbb8kjGOJRi9P2iZvBcd2MvvKw0kmI7OZEBkcNv3DPfDuF%2BLA2%2B55wBUPtDHBMxsFgbLb5KlCnjRE20%2F2RPJTHg%2BVOpUInRqnQ92W0RCdJls085xsIjm%2F%2Fx1V4bZtvTvyuOESuxXK7YOZFoCJJnaZInIgy2yRpI3saKa0Pb45nx1VF3hT4FNq%2BmsyALhSmj12N40UCk%2B%2F75vR3CWLI4KWGodurJih9ORpZSnQkOpwM%2FHOa8b15FpUpozK2c8iznztSyEp5q0907wRURm%2FZu2VvksBKhxMg34W5ui6qWiylcOxf1Xwe42nn8es0g21aejFbGQspJ9txeMvEA%2BpTXW9jz2gVFSMyclwp0NnzBCPjDBqqXWBjqkAeUQTUyT6UuGxHHI%2B2jEHdAV3rWRAWrHOuyRTgDNWyFsaBYF9KbO1CPXIJZHuOuc7lzyORb0X30oS1Wl%2BCTeKis2nSe72Ezb0vUfcASd7OVrbBHO3IT1kVA8Wb57e6qhq6KRNnszZ1MVH4l3rdgze218Sa5G%2F8K30SiwgUfgYru2AnZnZ%2F4IEYfyenqPmbJ79VrPTVDRft%2Bt616AMBdIJic%2BggpF&X-Amz-Signature=fa0464347b6fda491b5c3e02a8f86d741f6f996b09a85b7728a3b405dc7a06e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
