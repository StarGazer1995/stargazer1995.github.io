---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJHX7LVU%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T231949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIDLyjD4FtqxZ%2FGcutLVJBUKMNJJdXnndVI0QW3yaShmWAiBHE2YUpFzG%2BkQHFO%2FCUk3iYnTdlfikpof3JWshRvDUsir%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMBTGUoWPUf6h%2BiiwUKtwDIz1X4JxlKFLfx1r15s0rXeuekF3YuvY%2FXjduWgfp14YDb2fcP%2FctcR3XPMNcNoMDuk4CQlFUAe7nshl2490TL9kGfxueB8AF3BLcdvUtj%2FiQY56GubiYz0OVySZVVMidFUml9AnjQHGYcgQjrZ44tGWQuq6uPe%2Bo6WF1HZYi5B7sxi1gk1PpvXgd%2F648wZvzgh1RLA5179GBVJkssZ4T8MlS90qVPkKhHYyCiQt49OBS1L%2Fc8WzihiW9KVgumwLlkxv%2B2GDwRas7heIFTcV6dm0XlXwFFu4sUhSnB3jyaB8%2FVjM%2BwPmX%2B4FQ7NTe1AXNJ9GeoUU7HlD7e8VBQbD3eYJYH%2BgkrpexbD%2FTr8ZzFeBt1DMVlJfds0fN1epeUTdfLnK%2Ba68wzxy1UXj1hN9xpt0XC8mKfZK4ejzD2p3EUFXsFJfY0HYtCZCoLcGQSEnu94zGX%2F7wGW0pHEbckzncudyWE%2FFYKkp%2BE8x51mlrygJBK2tOXoQULP3a9zchaKwBETf7Lpuj7M7WTnv%2FuzrfTmN%2BcWqu3azTu7jeMeW4MofqN9rWH0RthmgLKDfVMNm31qrvWetMPHOkyHZ5Sfz2uhgBOOm3ts5D9%2BEKMs6J1unDUIlBL9cq1G15aLgwm9j31AY6pgGT4sV8%2FxQ9p4EgqGHmnhE5f0y%2B%2FU9mEknO1WHwajkIGqzycLuTWRWftw%2FhUE9a%2FbD1V2l7cE8OPE1bc7xC3m%2FnbMaE5aRWxDueEV9UKnIA9N5T2n7ilK8PRG%2FWI%2FszZRRLDJ7sLZzF89Ier%2Fv0vlt0ZbvS%2FeAe9%2F3yY%2BACWoZ8ZuT2IeYE36dM3Fa%2B%2FHAKS7t6p6evXT%2BwNT8UoUjxNWbsjHs1lEfC&X-Amz-Signature=39476424fe874798c3639b6d35357dacf73185655f193d06f97884765d2f8abd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
