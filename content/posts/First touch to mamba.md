---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEOKXI25%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T164056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE8xfOzxdvna85DMX0zq%2Foqp%2B91ymmpGDTZioARXjbgRAiEAhZTmYSYCjs0nVwnqs43qJudNNVigSzZordRNResHyD8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDMRikhB0kNk%2FbDsYQircA6U2JlWX%2BcNpNqkX7UTAB6rZNF8Ivomc6%2F%2FGaWkrP%2FxqB%2FdqSHbTiubdxZFG%2B3Kp8H%2Ft%2BCFWybB0M6nT5qwu%2FyPzr1EzZCn%2B9dRGZJ2fNkZPL3gf5Wevf%2B1vecOpOF%2FES9Xx3Eo%2BYBKm4CtkCfB94pyoUKYEU05Ze7zkAuhp7GL%2FRgW1arFjUSOmaSDfmwzY%2BrZtS6ZiNcfv1MhbOpxWs6ShcqDxdRSsLYfQF8G%2BJgGpXZxY79QRScdgzGjCfXedhbgCIWayqUHSAj%2BxJKwVTVvT%2FwEm%2BWdkwxw8vVGmT94BsQzltwiVPraLjlv2Aoo7N5usmYkFoMrSY%2BqQzSkUT3AdBCbrMnfc9WONyXsE%2FYIQzlsBPDs9LX8JwtUM%2BK9dT%2BCRFzj1cwER2hQNRJnv8Y5bUl6jLpP3h2LUKZJCpRU0sAefNevXPp7WS8vfUDCD%2F9hOE8vA%2BUJDdlCJBU7%2FDUSVWXBuwiD8kI0FBpATwUhQZTsEgXiSS%2FaG2uJee3r91MpB%2BJPWCer0dKEjVrTjFekQKQsfOKv9ST9G%2Bdv9BeSjnuxak%2FvrdSK2QZpHFGEBXxNB8WHsXXkcg8YAd5BY6pZvtiqoHftglHY35EPPyBmkff6kwhExXQvZdJZUMJHl19MGOqUBGpII7v7PZrxvJbjCfsNtNe5mNGDXDv7mpRG1HgZs0SIgzn%2FKtQkRfipCR2aD14a44S3EkwdPLbST54eQkqD1AlGdRW%2FyiCsz06e3bBzmMc0bRVAV9JBb8Hthjuy%2FhO45J8EFeC%2FLXY%2B9bGil31faZvAemupmgaGnUIhhuDOIwNvhb7klCMJVz5ulAZv7Urdb4D9GCFxe44R%2FMvMxu%2F1yw1u5v5%2Fz&X-Amz-Signature=7b13986e903cd81dd60501511df9314b459a53bd345e37654dfd9ea8dabd0411&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
