---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2UJWRBO%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T132601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQJrp3vWmqhBNp3ADRDzHoZbUNGiHT6OWI%2Brc1yHw%2F5gIgRb8XpknTTUrJIcfMzCRimDcL2GVsMBNmJ7pLZysvaEAqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPMH4xyj7cVKPIBoACrcAylPWtBiogAhaPC4Zfd2JGERMmbAZ61TRN2AhDD0cgs7mwpp8eAdsCB2vZ9PU1ZGz%2FRVoIuPOWqOp1Csemik2rdJDv4ZvqQTtwn8wTFpH0X9lbbn9u86jAzd7CcW4FAPN4bxmDCYzQtTljbk3rAOrH5%2FuGzTQDvCyBV3dxaKZyHACJTjfHLn%2F%2BGcWzw2U24TVXjxnBt%2BQvQtRgr8HO5Y%2BlVNqWHJ%2B%2FcoXYo4hExUT7%2FAxHibcG6lmtS850u6GyxuLN49iQCW4RCrLZv%2FzTfoQz0QAFqSeyK%2F%2FOxvS7b2CA5q0znqp6%2FmjnQTojAyEcDKQvqDdCtZFtkDjY%2B2u9g%2BDWj1joR4Rx4G%2FqR6K4FXgJDteBg53Q1DhhIJo%2F1RYwFP4RhyDMYJj0mZ6ftLasynzWdiH9HzZndGMB5oGX4k7KDl5EL%2B6mML%2Fh%2BopMQnNIAf8dNUY%2FVvoBCownAkXR%2B6FncW4QEndQ%2BFOXS3h56phCAY8Jg8j%2FprFfHHFoILJNPeyClqpAH4%2FVpHSowWfKJxmOdPXta%2BGzw6qcu5XLgpGGOz8DnO3KVUsEbvcPZqp6%2BI8SRKdUFuQzIIDrxhvM2deoEbNFt0e0LZREdLqvVNp8U19jWlVCL6Sww9yeuyMP2%2BuNIGOqUB2qXuXLQKRMChthtkBjqkseol6DmJFuA1PYEzjrNL8qdngIMtbU%2BMn4KA6OuVq9bGq7wBwy2NRRUW%2FWdWd3IfUg1Xi%2FNBL4l%2BD3kjTU79h%2BkVE1Np3KpH5l6vxSwoifXuAkJvwaYDdoSjrf7l1rJ2p0yC0O%2Bhr%2FHdjansBl9FqzwvS9FKPYepIzKChZPq2MS%2FDMdrixZqRM1MAUQbnTQPw3HGWvAd&X-Amz-Signature=604ae10734a2d8262fbf126321e8f011b5c2c64e964c969d13a51c26f5d2f245&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
