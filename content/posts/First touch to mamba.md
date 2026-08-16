---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5Q5QU4X%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T081535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCKLj0t1V2cBMGMFk8d3xEqp7sCuTnye0rcqCnIjdhnpAIgQw99x7LaVKNNFdvvu%2Bcxv%2FfbwEI9MFDLzlfwZMgtm6Mq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFoVfpjXVCjCMA2EyircAwlh6jMJDwZGc6MpQzEJ7rveZrxdVDmtaFaUONnaOogMLpqK582Hm9%2BkRsGO4NfZlZ10%2FpxkjCodEZZZs3pZ6SyaKoNAGyFoTxTZymPXC4NNZW3V4F9zOAuMJBu5zDPS5RjSrTrd18e8k9H1CEPCfqN8Oouk34Ovr7MM7AEaSlbEN6NCsj%2BgnrLpzIWLnYDOB1HNW4E9n5y%2Fjv7m5Ad%2BEWDhIEI19SFFcF7knYssAmY6qbXFEYJ%2Bld8XNMpTjpFZ4%2BBhuu6ujLpNTfTHIbam0A2SvcbzL36IuWo4etXQQJ97xF9MHI17cb4CXhAy0cyWpovsgUMr6Bq%2BJV5RVCA9z7eGehC14V5IAnv3Dsesjj9N%2BU40X4OW%2BIOjDMghO%2FMTlEysMmkIJJHzkXqeufdZS45piNZssOMOg182RlekuecRZ0LxLe7XumjfpsL21LSEyQfVLvMp8UvMUDBAP%2BAhopPlqtkQ6XVCbUUznp7o3HYxBpsauUhOxukkFdvJVEtX9Ug5fokVpPzuKVtQwAW0sLJmfSW%2F%2BBpd1AtkVYsU6a6iVd6AHd58JdPPzl61ClDoUJTx9KLCjyB%2F7tp1ft61kEo1NxlCxnr%2FP8ifEAk4lBAKoq2H2xiTABraWNqgMP2AhdQGOqUBTPrOv7EaAyMkNYlJmB4o%2Bkkc0IR0lIAd7pelCbeH1gGuKOyY%2FY9p7CbaNRlMUoASsE5Fim1vhOM9A3CQfPuoEYGwCN2ssvsjShCh1GGxkKEqzt2nOl%2FePA%2BGRSTWMp4oFiqfp%2F0tlPZ5fb6HV0FBItmWplOS9S86hORxuFg%2BZlZ2QvqdJhy7Fz8h7ituhTblgqiwJH8CAUI4aDl4nCmDZATxuP0Q&X-Amz-Signature=fa0459036a8538372631d0acd5bf8bdb1f5e2962ccfc4b96e42c97ad3e5f13fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
