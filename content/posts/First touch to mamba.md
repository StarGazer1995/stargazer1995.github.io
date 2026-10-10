---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDIAN3OP%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T230304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGW1j1ILKltsOzSn61NOnt86I21Z5ycaHQuZJ%2BuD6ZawAiEA%2B72nayBL42Iy6bk2QQEVovf4jKyYTeIMao1vqOFHJTAq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDIrw8DJPbSC8ZLHdxSrcA23N6tF5CFxO2v49%2BSjxSNuZpc6lrQQ50EXwltc3F7fVQ7avv%2F%2FYWdzo8ItDV9GMHMH0JeGWco225WhaWUtHG%2Fh4HOvEjc7dDJWJwS%2F55J%2BENpuO1OKh5VbGIZMeJ%2FcaNjrAWUe%2BBIOpSPBCq%2B8DYuhqDI6bnmmPNMuNqWrKXCz2tpjSQ5PNykKI%2BWAHdxqKQEXe7rl%2BYpDuUnEy%2FZ87KQBhdqtCv3%2B17bHhbdZLv7AhnTZ8pfXzlqGzyLpfG8fhZwP7%2B3UyU5CcrISMT0%2BQJTqJLdidMZ3iBd8vgQizHW9XbJo7Jo%2FA8qnmkh2KQMFY79cwxQNaep9mNTm%2FCldNIgwyRlQDzejr2FKt8Tjh3rrLA4OzbvVdTcFucHzOExybvbhTSk1kvIjf0o0ZlDT3xJEzhp09A9H8upBBt8FZm9XyVb%2BmxxOSUpzvqfvqRmo5s8rb%2BdmrTnSDoGw2OjmoV7pj%2FMOnX%2BvqmgY35hOjDY5ko3a282YtVb83AL0QTaA5YgLLAeFyyJOTjvZ98togSbIw%2Fp4ywkaPNz2CRtQIOgINwzpHnRMf5UCFwRlL9uJB5puHnoUCjGSNtkIfm8p0WI3dKsIQOJr1JPnh0nYIXayhZ2EDK8ZxLT7gYEHdMInbqtYGOqUBXhIRvzLR9nT990BB4DQAW9fmBZcazHul46f%2FX6pmv2j4K6lddQh6kGIuh9YW5dPs5mnFAo6nEd0oPwmQ0vAUoHkJvthmTz9spqxTAUYSszclMhHkLiyeW719USUGg8Hpcjf0paHlad39qhtbItjSqEoZ3M94fJGQ3DGqF3adtIxB0u2h14MkHC0HJZkgofPkj903JFnfm5H1dvF8ESRWaARl249x&X-Amz-Signature=cf66c06400a5552bd78365b46e398781b05a90495363a8907452f0c4f7d64ce9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
