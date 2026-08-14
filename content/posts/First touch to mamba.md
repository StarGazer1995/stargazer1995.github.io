---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST7E4IUP%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T070511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEcE35R5qOccTjva54Hqp%2B7vN%2B998y6lVNvHx%2B9dpjfjAiBfxVEioMVnH0QACvp5QDiaBHZM64I0UduUJdiVN6VZbiqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVb93%2FMJeuD5a0VyZKtwDG890SAK70ZoZhAQkz%2B6rMmlSraZPbbsByHXNoMP58nMyXoqP%2Bd1I2KW5ZQLZE%2BDZm91Zn7vBETPN6bKX5m90E0eRf%2B1VAcDzcdlsM%2Fug7k7retVmGtrD%2BJI65laaz7QdxTWDobYRS8rzN0BctJEfB4UvmCvOQVmGQaA5KFLHvw5up1U111HEFHc9JnewCElLjq1Ul2g19UlPz3PdDW8Jt2Z0z4GZI9EE696KICZq65jHXzVarZoDvZss%2BoXFZ6lft2dc3HGZ%2FGPUaL1EOm2E2uBKVpHqEeQ1IUSXbQzbSkpjUQJJuhiR0mF8KcIOwTxNoTtJEwwWp26%2F5UhOssOf1JU%2BxtZoSVRx%2FjwAvhZEtj0QrcpwuH%2BuSjLpbcPSVIJUqUO3SZrDpMAyYBEwxgLEZ2UIe%2FmvsuTQdtsyJeZHfjVH2UbyP1jcRSZrafnLPImFrFyxXmwMORRBSmFwdrJoZDRdNPszLJXBc5%2FlAJVQbC7jyx%2FAseZIQbAYiyRYzo00pOOawcoFZV3R9BhH9mJMCY3vzIarf4utwHAfX3HI3K7fAt6IX%2FubQir2%2B0GMtp9XuVqY%2Bh7X%2B%2B4jWnX6cZZBc%2BcJxQ5%2BfSOKcaAzUEMT%2BzN1HC2u31FCpNZV%2BMQwm9v60wY6pgH22EpZTNThmNoZubjOBxt3BtjcUG4B%2FhetN0fPSxCaml9ZNhtYw6CTrTtY8E5P4kISNLnKn2awdz1FxEM1XEdMBjJO9JQ4cKrKu%2BFDJPMN5B4Vm9ZD3DR2qR3AQiBONCMiDFW83Bm6V2GvnChelo2fe8L4P5TW7vr5zCSK%2FF8nidkxvMn%2F3LUfGdOSega3VeYfGYx3cHpEKgDnhwG5fRSZLkklGddp&X-Amz-Signature=283a3c80c8f5b49223eb98ff54922f6e09dcb3c671cbb095504a8052c7b3fb48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
