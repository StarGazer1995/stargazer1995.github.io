---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIEUPG6%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T020156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIHRg8IcWofDjQwBAQr3Gn63WBEP%2BaojnXD1osGrBwkBzAiEA5mvXSBIGFs0UcmqtGIL6gFfeNi%2BEPYkiCuBeYcCluKYqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHAQj%2FpYqAsFFoYhwircAzj67fJPrQAABVypYpo5Vcc6WyjS8mTKch%2BKO0m2WRvB%2FQFpz7U7nhCqYnUgWcWkKnnzz9TJLy0wf7hhtDoArpsIZGQrrSjp3JWoEAkjwKpbYqH8vsEppw2yZrEBR8btpGPwkvlMB4cugZHa9JuaNHynNYciawoFKwwcJDvSW0%2FtI0VKhqMFsaN9Z5tapjjXXgvNa9559172YKwyOjQ6rSEaISFql%2B2hQ8Cnuig9Zyop4kVmYBZ3WmZalNAY6j2uLRMyhMz10bUmOwYT99dCnJ%2FNEOSE7WGn8jUdxhneVvwvJJThZ%2F%2FPiCPs8oZf%2FJ%2BEiGvwpBoLPGr6UTkuLWcoR9snxDYJIq9lcB5oov55xg8YfKKNhwYhjk46lIZ52m5DzkR6qMQ%2BghrPDEkX2oiscQhPPQuHBIyo0B4CqFC5lwd%2BHakwiMjJnJINZq1OsiBRzrHbJqciZq5Ub15KWsPaYhsMh%2BuS%2FezKa7wZtHFg6NMgYW1f%2Ftpg70L7wGX1OK9z%2FqLHgOabPA8QonZXbbPmg8%2Bokwn9YJjjW502shHrJvA8VJkADvLlcGVDurwHX3LVX9ILsQYKXUIptPhwWeOWBi7lCASm2S0p%2FZIP1eDlkHkozSVNzEDB%2BYUL3Gc3MNScndUGOqUB95D%2F%2Bo3wUU6pfQ7zSYNPGZ3ukmbrRIpOA%2Bogt1su%2FE8SxQ7J8Pf%2FlQaHX5bMsCC4v5LOenXWXecqvcOjINQqTV8iyUhiBeNaSh7Zbax3le2n2Ry60X7di5vJP3OlBOj5Z%2FG2SrvipNLUKbikH9ubuNkkwb0jzu5oBBaHImzI6Tn%2FE3JHHeKp9OI1zQ0ciPyy6TYAt9YUOUHfSyPp3TD%2BxWLdCe1E&X-Amz-Signature=e00188baee9a6fcf93e6764bd34f3db6b064a4bac3aa7b8ea6794665b3492f9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
