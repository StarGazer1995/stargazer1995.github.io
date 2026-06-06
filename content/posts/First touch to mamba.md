---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ4WB2Z6%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T225415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLIBYqwKB1z1JYC7zIPvW0qauIQmOj%2B81qLZPxFdFFegIhAJxU%2Fry%2Fi83xqtDyRE2njU276iO1UxA9UD0zp5roPst5KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0KyUDyib2varJobkq3AOnBV9ZYt2VkkegkJ4xNx%2BvwTD0rRDGBMThF1q6Cf%2BCJMBxb45z9vJOJem8bceZ%2BgMbKH6Fa6%2F9nyj5tEmavl4P3uEcBlk5igS927L1FZMXpeSe7GnRnRmoGKkAYJZwQc%2BNpmgOiO%2F1AbDVo2LFSzpzOpOf8RHmqErZrjLgEsyzMPYLl2kmF28vPFEw%2BjmgTlZj4Zaw%2BiDe2DtFUPFsFg5ADAUrvFYxeLibD8l60lEReNQ5g0k9mf24tRokcDTXnLaclUwYfHFmejWI55OdrIUFmqBTeHX6CF9zMcPdoMjI4Ov2bNhjNO1SGpne%2ByqUmGw7M1aP%2FaCtLOw%2FouwcCrnnouyxE%2BfWRUHBAEC9mIclE12OK0v6zNsBkodXS1wulwas3dr8kPKmUmC%2BcSGxgJ4TxSPuxyDouDu3kgBbUZBxE5VSJd7qQnt99WS23KJ1v82aGgHLTVljFkzZmrogXxQAqfBSd3Gi5IALySU8jY8CGL5OnPm4R4BEEnn5jflVogu%2BMOx1AG0NxUkMeQZPXlEb%2BezOArSWC1%2BUrw4lBBgQXmDK1yxANE0hEp5NXCdvgXtVsXCPXnLuSS%2BzTeNDtAGOBRzZOXpFS2HcbxjVHmDLbqPeos33tF5GJp6esTDVq5LRBjqkAWEbDc3HOeLfgtHlpt0zvttgdJS%2FRZEj0pGe9Ku8KGSlbHr0vOZPQnTxlOKW5CLVGhTHyPPMJRHEvoRv7Kpec%2BzEtw4CdFSFCjCpAvNEgRNtmkcVqzm4IPBa0gpMrauzw9Fa%2FRHxPpNsLN3duwOfnog%2B0h6NGwTj2zaAYwcZNJBgapaG4SYG80FhdcxqeT20gEgVu82mx8wqCsMiZ%2FdctnfDIOX2&X-Amz-Signature=f63069dfc74c7837ffebe09e542e665acd64cf427c1b79df304702506527032d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
