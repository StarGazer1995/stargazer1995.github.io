---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGU7U3SP%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T201421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi8L%2BJBG0UXLtWkd9iCkFEo1Net6R3x4iJ1YpjVRQEJgIgEKcEHeGA0yru%2FsK9D3%2BAdDl2jYLzLkHmKVrdrNa5RYkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXu09GQCB1fjq5r7yrcA9JOAXcOSXAB%2F4B6QPePKW8ZfWhsn9cWIWrzey6KPfegP3d9Hqu1HPUEle09KY8%2Frun5Ty8L8e6b9C6Ql8X3xHZUgDF%2FbYzerItvAZRjuFVHkEZJne3oMLbssN8QsD9a6rtMj4iMfMyLPzPBVflDHf9DsceX5l5UBrwQcNf8xdSj%2BOIX4MNGVTvz5ZRvFeKrkPL1V1XG5ecW1%2FoS%2FKxzEy%2Bgq5GSk0amNMLtI1tA65gDvZLv43naBn0P%2BZBu5nObIQhy5Hafi1JdDu4YrnZEIFvlXUUHb0lK07sebh%2BlIxpCqCNR0Nuuscu4dHal3gWtuvTqrCMsBxNdJGsIAj2yEBcOmhgP9TC%2FeTXgLDTA6%2BDoTUuYmh%2BO7jt%2Fz%2Fk2ZPCSY8LSfJk6wDam5YAom7Fa3Dzi5dCsqd0NsB5b4HhHfoXlO5ab8YEJlPvd9MWLeSXAAhYc%2FpOAVSLUR9lwGbMtm%2F5Rhz6lBOlMYFDPAuYPZUMnGozt%2FQU4WGIwW89SsDd%2B4RDNSTg1LdKzPSGuhKVzN2O3WCIUZXAoySOmyIQMasrgkVuzzlRR97ak2qtXjRAm5f33oeVQdRJYXGfZTrZ0vl5QNbbfE%2Fvd4zwHaDPS6zST7qR0wSVXd6Qr7BF3MLv%2B%2F9UGOqUBFUR7qSrB2FsXD0fcpTBRbTWU1pgU3aXzkc5G7RLvRsqdyFhv6KtqwogP7dp88iYBhN%2B1HB%2FDoSzvTCnAisnVrbhB2bysYE6IDgLvfYtfa4X5682jfz6NTR9m1%2BhIM4T8nziNxCouOJnknUy9%2B1LwK3fFJt1hMTkOFuu8H2XT1iSF7byBOIMHZeTIuOLGCR8m%2FdxEoMp%2F8nx3JqolNgpar%2FOwuXuR&X-Amz-Signature=27cdad75f2e94040b9bf2f2f8f892e1e324912263559eb1d9490c831252754fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
