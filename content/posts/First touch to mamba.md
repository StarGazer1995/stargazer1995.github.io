---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UD5HNQI%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T044143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDQeVxXRrTM519TsruVxnOhaLEvZa1gkh4HaMIy9TOcAwIgDZ9vO3YUFu%2B%2B0cp4w%2BXA9j%2F3IpesWYiOfJfkkldiN4Uq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDwb4vaCE%2F%2FUM7PZsircAw7SJH%2BLDOO1sjkV8h0IoZRZ%2F3fKuiYTmdc8SzZoF3PuoxajbwLb%2FPLMlRFsX%2BVTXhAesYeru9y%2BEFm2YkIMHh7XbUhDElILqFwwjupNULK%2BJrdV3LyKRRbATBYZy7e93Fsii2RGrlN9%2BQzYq8D71n7%2B%2BtjCIzKbEV0CC3npQ97%2Fwj66%2B3QvoncdTCyPABb0Dvh54tRXm%2Bk%2BBJXtRaJMgr5qoTyaeXEzwoh8%2BJhUcZMgdY26r9pf3MdYVL3GNBVzcQHVB%2Fd2qtQkFVJRszWBDGwovFNY0Dfx4r4jfCuEZvP8Ikl2HcNy1LEZE55FoBS9UIlVdm9%2B%2BhCKcxYgR1fCoanKfVdh3IjWAL0fK1KvIfwwbGs%2BTlPwxxhCyTmGAjcXh6zfllzdl6Ieo7hHOiIHDcv7S4CFstVSlp%2BZaXXGXMFWJrSWI7evvgdM7KFofJCuSGdvgyVGHcEGU1bg71TJshXhFW82BOwOddFwyCkeSjtZRbIfGZuEzXcfnxLnYunONkNe1uevL70JXYLE8sEUkQ4doH17fTp5wwnHylze7WmLgoKFc87S1xpFhuFbxmU%2FniM4F%2FppU5BGrsLTZwQVgMXaVy3kgGBvs1XLr3zrLJ%2F35y2FMYqKIa9Qp5uhMMH%2F29IGOqUBrM9qVgjvp%2F3MqinqdAchb2qEThJA%2FtAVb7EjqnPOmTfma59EM9lxRbzWplboe%2BDzjYNuOcfJXFSSFe6%2BFEDosmxnx%2FLydP4Hb5e7DJC6c8F5ch%2BL6lsTXFe%2Fy%2FNkMRdPM8yRnU47dVPz%2FvJ6nDSItz0J%2F1fx1JCY1KrCGPjCBLFBP9TYlKAOsX%2BqhbNMnM1m0hh6CUtIpymKWu4uEGo48OcB4Eow&X-Amz-Signature=02cfc06abe09390638a876285f686c3e906064266fe8fad0be40ac1f4a0a3799&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
