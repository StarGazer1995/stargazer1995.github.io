---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZMMLDC%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T001224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCu76L5Nvf5MewNZnV24%2BexrisJbPYu%2BosSvFRBB%2BjMRwIgXt5XjKEGKJ8yJjbEpIkWL0Eld%2B%2FHtrb19TZTvicBeQQqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBNz90trtXP33V%2BuSrcA4YWpfsGO9hLgDn6ArGPZA4hMdCO7Zsql1f8EFf1GU%2BpvXiWlfJLQNHgUwrKIiisULLdWGZWd8m0RI8POULSLEZT5Fp9IItSnzpnEmYVHZxupHVFeAfFLZtJLt%2FnU067SIutO9pDwDEZeB6OoYL056JmlNviUZB9s130X0vpu0tMQu497ONYsLup4oUreQoCI6SfIfs2MjtqTiWBArq87FONkYkF%2BZj2X%2FAi%2FaQirtleXK%2F1BCGnljwPdqF%2BTwtcAAz7FsyYI2XJlHqohcYViPVs6HFg9ZmeqR3GvwxAcYWP3MA1089KxoOCSf%2BpW6QVy0Kn5KII4WEB52%2FWRHZ%2BwNIcZ%2BrVguZOXUDuapjLY%2FMaBFHRTc1yFuU9NFKMm5Qw2D0rxVCU87XE9td9sjXaYT6FwMsEK0gQSMVdY8uEI5qxf4iHoaYPghQwBpbeuU4ZYcYgiEGxaj%2BFFX85F2YvQXvejsxJUfuHsMmZP1mWrEwBgxK7GMzfr2oij5WGY1T%2FkUwvBHnPqc24N8fGgxYqB38WjdO0Fv9s%2BvTxqiFYZ8ACuNTkIwJeTv3X%2FaQBJ0kZ1WNtAPQ8O6IFOB9NTGGoobmYCLe%2FPwbmGSnpOSQZZNNH9jy5mCzUkvw%2B%2FoH%2FMOSohtYGOqUBbseuXTtISzmds8oc9pJq2qjfQb63qxjyXjYnhU%2F5LYQOVGBUTLST%2FEKD5nSc9ZphyMWGrN9dig7NMoczDIl9KDnFgDy9rBXZDrnT8DQm09LQC6wxYa2e6E6UmBhSyn0B%2B0A59dCCLYFR2CC8l2VDeDWbQQaOzeLWKwV5S%2FEcodtkKrLhPnrdXonf4dPGTAYBZGjWXUwlS59id55ARBA5%2FN%2B0Q0IA&X-Amz-Signature=0ae8b5ccb1f53cf83212324901c32693136fdd11c0175c3337bfa19efa23a532&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
