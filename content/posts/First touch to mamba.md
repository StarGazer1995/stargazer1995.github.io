---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C3UK4TM%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T225847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIGYcP9KebOJCscLjGuHgxhCOLU2Wmo0C4XFzzrVLl2%2BLAiBk%2F3EOlsDFkNJ6qwYcAerovLi%2Fpb%2BEcF1LU7JhcMlXISr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMT3F6h6Iisi9BAAIdKtwDBwNkjq%2BJgqOXClMMped60HYzRpyAdsI4HjaC784F7uAB89UoW0gJ%2F4sD4yoKceS1VcIimz9LQj9cntrqVIk19oUU7YnWJdEKFxonsL5Yz0kyOEyZXECfg9UaIgfKmALkIy9KW7iqG6fqkHS%2FpFbL%2F9Xs%2F3ahURyxSgJ90RvNA7FaMoyigslI0N%2FKiaTMLiY8S8vGRfPMVu%2FoLUOpytedaij8BG7m4fN2eugeFvCdrzATkE9GVWArkZ1YRNk%2FbdwqsUjKz1QTb7aINQ16yuPVUgzJ4qwAdTpHnh4x%2F8tVxOC3YFepcOL5Lj6rbrui%2FSVwlUwGhALSGkLdx01oeXSnEVnbTEuyQXvTG6SxmbxUExAcmHQwqITHlESYpmXwiCiIY3pml0WYY4WVpSjGWdImJGyFRs%2BIFDbIIcPN1zxTdUotd9r3FjsPevVMSrvvTZnJkSr6yaF05yRGSI2%2BFHOw%2B%2B8MohIjl5mhZJWDmZTRnrTc5ZPXPHfKoKJ3%2BshI4I03EhhMjftHuPWGdypt1OdqGSX%2B41E%2FFt43Jr9TVmudT%2Fkp%2F%2Fg48GY1dzV3y0OiTf%2F5jwgCmKVQQp7mWdkqwDtflCRGMIIXUZZE%2FDImsiToE0OTcyv2uoWBQdRw1Ikwk7fr0QY6pgEKooP%2FWyekEQOsJI3Yt85afa2TDmKGQr2urVJRaPg9F6TkrvLYRndwVK99mUavBVgMzD0cPu9H%2FvoO1o8dT9Zb7OrtPWykToqOMQaw7oUhhbfKNaSGNztEjrd%2FIn%2F44gYP8JRL4PWviz%2BMhYorq0BXCAeYJTDVlrJwOuhH6ykAYpwWCGE%2BD0A7fLGQ82y4nbqatF%2FxoJmeRru9Z3wHFNt7eNtJBzvO&X-Amz-Signature=0bfb171f23d48d0f0786a34e0fa0c3dd11902542555a47ce6196b99f2ceeb2d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
