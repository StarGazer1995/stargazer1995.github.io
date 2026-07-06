---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ODMVWT3%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T015648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElcZ6vW6AhjNOHgeFvrfZmgHzkZzAY9%2B%2BgkbBsytcyTAiEA62DjOFfPn%2BwDmkjUCnS6xDdGFrmt%2FulQYvkEiowGpAkq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDLtkF3gvp24raaK9MSrcA%2FyV0%2FJMzXfJ5kWLot4pahLQkURemSlETJddq3kvZQIhZ%2BJHwtFsIjduRAQb7gpLPqYgGSCgljYg6mEHfXsKMalROfkRReuVoar9DZca6fR%2BCR77rg6NOeb8kUZeTNwy7ipGji1vE0mP7gv2XvYnldA2vVZVxGtvR9Xpl6rrYxC%2F%2FXwvo8Id5a%2FTR1N25TxVYt9paoqR79pxMaBgPso2367eurw1CyM6MPMBFW2VRPp9CSJ3iKkji%2BMZBrpvOiLRaVBV6FbK05icHuinw8Q4q0iMvjEwEoUZtNkOX4ROSGq1eE6nKK%2Bpwe3sjROxajCMwScao14sBqDRUV%2BniPfP3eb20z%2Ftyu7%2FljIhJj3DNx1Gbfzmnk2fpdMBIK%2BA1MDcW%2BSi5otq7vYHU7lqzqa8379EufmVxyf2U5r1ReKtxDNYuD7Oy3p7%2B0Tdimdx4fHnbiaPtg%2F0Ickf0HdiW2tyKI%2FxxUxxNwJoqNjPvRrkGfbDm4nrbXwLJYJJnaV309GCKq5Dewe4pa2ZWtxIFMf%2Fluv14SMkgZ5zyOOza57D18FMLtxOderCiKz0v6D9VpoU2Vp1IjN5Uub0bk%2BgihXxhvOFP86E1%2FILiNKWRUUsrbwY7nTO5r0xW%2B0OPxk6MI%2BPrNIGOqUBU0lXU85fzBc9K2s%2BevxD0tXfSPqUY6m99v1%2BmUqIEsRJwbJLc9BPsvOOsn0mjJn1TEhSXllmSOc3OWMxVRobkYeoickziCE8zx9Hwu4hzHB31rU%2B0rEGOFhYhb24%2FLoZP1vl6%2FpCFQOgHOfLRStO8fGoHeN19fn3LiUaka%2F2n%2BLDv%2FGpx%2BL4ZUXb73G0Ed%2BXqoM4fshJb8klXuSyejehumqBsQUC&X-Amz-Signature=225e7b35c293e7d67fbac7f4ff1721456995028132050d5c4cab4e688556a95b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
