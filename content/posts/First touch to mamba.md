---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXTSUFAL%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T104249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHVxzqDnKCSFOJBUi2D7OIP4kDoNYsYRfN2ES8NBM9xAAiEA6C2lu1S19clIbcNbjmZzO7Z4GSyRFU5JS16hN08pbjMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDEy0y00%2FpDHjkVFJ0SrcA1jHSosxb4Hg%2BaiOKNXGMW9uBTX%2FnWUan9sv5BQj7JzwGwu%2BspWucFE0MlrplezzHzn3IoyFzhMayP0QvrPyrTqK%2FQqFdAWFiAqNNSVmOGa6daBEUL8bNjrdYPuMSUBPmJslT8bK7cYQVruP6%2BsAOteZj4Ht63fq8r0u0%2F9NlpENoKsLy78ZIMFGGog1pOoYQb76mE2EdPYMupSFegWHJ3PpZfJ4M9gyDhP%2BTm2P4Kw0EurtgAkaGgksKN7urJ4DmavPUkVMObVXWLoxT1ITQOPuBAodpdLC2VllEW0VjUFIBCYJUsBNmv6XfbuIwxwDLqLc7yckQJfG%2FASlevzCugYcxG2xTc6eWMDkumXm0FiewApFmqhqa16Xe8Bf3FMQgf4XgEhxVIXHGlmuH8tDMkVJwE2paxXwWjs5BThqzRIRrljPTTRuocjIjJ%2B9r%2B1gyKOSOxcfRC17jkmQi60kokEbxHpFLRcHz9fRm0VH8cR0JUmxNJyniUZttlTthN3g06qy4uCjb7tZmrHp3Aup94TJUEye4sseEmjSlr1mhdJjzL3eRKCWRtlEcW%2B%2BKfzVvtSJHJcnM%2BaSJmdikZbca2Gv72uzQAZOdTXixbFSo8rNGCtm0KkRpJBF2pG0MNjG1tMGOqUBzIxVY8yA%2F9GYLnLg5kCo3F0la0wWNfQlrZCurHbKfAcjCzHt9IrvSvQm72Leuws%2Ffa9ekD4DCNnJBMpfz%2FEhUkh7AfEs48vk57oCFdebgDy2YE2%2FDd20gq6Jdv%2Bx0i8KisOwp4zCMGpy%2FzWlUov%2F6b2ov7mL4ukTZn1ayzFMHPCujcO%2BGRJe3qFJxLtMywoFwlrQ6dNaOXIqFrmAWjmFW2%2FRC2UM&X-Amz-Signature=c2f82a0ff6de2d98057e7ef633ce53e4b6345a62768f173050ab58a5b1a0efb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
