---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ANEWFKD%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T223006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQCQ92WLVKOmqcmxnCwQlH%2BmMYThNQV%2BipmqbycWGHh6YQIhAJdMsEYo6BGxJrmDp4mDZhWEtNXUuEMy1V3107eLRXW2KogECO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BqNKSC2pQvAco2v8q3ANxZ4URrPF4Pw28EYeTnUf%2FQnl5vrwKbKJxHbvae1EEhQuji1mYsgrS8ANEZAXwl2qxGjdaskvboQ2SMZs3Vsh9KXqujITUH4WtgU%2FEAgbevys9VhrydLSsKGToAkjzZOgQ%2FC5aLH7bVi5Hv5A86%2FzzkJM6i8w%2Bw2hZMB0UZt04ck4goK23TyLTJkiGKF%2BiRjYVERMRFzOv%2FJt14hNr1YpXRxR8OZsVxOyZz31Ih14jiIZZiUDkfi8mBOROJtEaiOK%2BpRQNU50AeE%2FQ55mIxOi2pMca61XUKI9hPcs5nQ8i8qtZq08bXymVDv3Qp%2FT9URqJ3jJj8vmJIn8QJzKtU1eNWayYEb0AzYSNh94UIanTa%2BiJV%2FJbx2k4XFCcFHwYR9qrZw1u8fd0%2BxgWQIQqQ%2BBlj4%2Bf4eJEvteasSRlp3M9rmk95SqkU84hMRBv6aimkeoqKnVG%2F%2Bdh72fWfFzrqTWdUv2RL%2FoeO2Y3u0vPRbMdXJ0ykVBHl676GqC%2FkwbQKZqBjYwkfdI0p4bictR2%2BuhWKfNOAWHGiAeebaQB4aIZ71I1fTk49hdPe04CZTWh3MkgY7L3lnvnBqRg6aGaCAdKTzs71WbhOnv7CEM4m3U9ff0rGPj%2Ba5WszH41HzD93%2FjTBjqkAUvO76tsoQpARe9sItrlsfhXm62MBpxH10rGaSRsuG2%2B0sH1xtwPjQWP%2FGtC0uce5zBU1tM8mQdo7FyFwH9aU59R4HtJQqqqAgB5NCWCEAS5n2acf%2BLHqeDKCvbobV%2Fd45Pgw0oHGM0rMoLE%2F4S4h%2FxpW8HZNlvdwlkfEOIgi5yeKgkI14YcFKgIop4NqPUVRZa0cXMNHyd%2Bfu1pyqHdCiRrnLCU&X-Amz-Signature=652d7c60a117f5e3e8c9f6d2909649c19c2bb5078fbffe09c4d583cbc42e3c78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
