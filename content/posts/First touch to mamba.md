---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC44AOP%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T130007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFEg%2FMSF9Nn4%2FPjoXvhojji2ESiXXdfAYVtH%2BjT6gNL5AiBLamcIRGWkptm%2FLnhsRZrhxY9slEd8y4zOh9UhxAyTfCqIBAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8FdCVhYuNsqfh%2B2RKtwD%2BL7X55J%2FnDgcx3sslWD7qUUMkiwmOHXrwSbqtTZygr1IhkjOLyVZiE4nUI4qEWFTnLI2qgpPqKKs3mXRlm0c2kDmC7bT91Pd0qvjBOYJp3dHAaDru76D4BvnECza0CouXQDIpF41t4jnijzf3Qeq7XpDEqAGgRyGpR4qXQXxQrLOL1dqMD37VTKnbMLTOEnD6s2r86ICTB2dt9dzWotdeHYiijRgqHfe3tpJBPrkBJQ%2BzzUUH9U%2FWJIytvEG%2Bt%2F8GDuwfWuK%2FT%2FAivAUCftk5o%2FF7zuQaoWynQVITHRYouT2QpYgBtRepj1tYRbZ6fjfn5OGrZ20J32u%2BABQ9F5Hu%2BmonYlt%2BXoPYCmzhsR%2Bz0f53h5RWkDMs58yfKhO4iTQkG4BPkk6oDIS7gB6XUvF%2FqkXn%2FwTCvdkOfsT3%2FWM5wqkikq5bE%2FYFGtyz9hVXgQhu5qGOkTmo0SlQGg7G%2FrhEV88NpA%2FPtOkr2Trb1tAgqL7LVcpREufiTy643kyXC7Kem8nFuuj4GqdIyd90ewE5JHKiDgMSQf1F4HofQGDwJONz91wnADm9BDShYEvcE39iG5SM4Brh9r4FUNclHLX%2FtW0Ar%2BjasyV%2BYhm5seKItHhK4VVaSYq4Y7Xjy4w1Ivr0AY6pgGWLvormaf4SzX4ssvKK43I2nMbtqmoECFGg1BFoelFub%2BBOr6phMSNkOsHUdAKn65QUTTnkVmyvGKZLyzu%2BL0ix%2FgfFaVA3pCM6ghCWVwePjwH53qP54OvKFq6JzDKmTjsyk%2FUjNKZRmJoJcH6v06Se7hZBj60YwKDffsLlX2Ff0FUmgGVqA7B1cNWOgUdaDmxjPWjua7TX8w%2BBZ2nyIdn5D3JEwnl&X-Amz-Signature=431b5cae495b1effa137e43023d8e7337a9b4eb828dbaef457b0756960faf040&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
