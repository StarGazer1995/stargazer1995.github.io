---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ6QYFDY%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T122356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbmj0CFVNBK0gmr3P3OQ91KrR3baP1%2BlXXvc31K4vxfAiAAz8ozQ5bi3B5gxmslv37NNq7htG7c9klk43TZNz0NNyqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMob9uKM6brIxcAAEsKtwDhiiZvbmzyWXNXfQpg%2BNxAb2bFZ2a1%2BX91%2FD%2F49EpmW68B1M6AjOfEc7EiMinyyk7%2FDANHyvarAxjWA%2FSdexrld0INJZp8Sbn9t8qoPBherOIBI75970E58N4b6l86dUx0N%2Bo8kL1hm2an6sISLVelF3w828%2B4GzSFKFBEz8h2gZYvhzvDbqdVDax2ksjKVSQXtlOcirEJIGwyd1MvNIXoKxYqdANq%2BL9PvwSf%2F26a%2BEiy255sF1PGluSEAXIzE33%2Bc8kNL4ePaTx4nJBeTlVLELLfJm9%2BKiZkRSUqrGbfgjfvn5jUqeEBwfZdvfiU4lh8p3Z%2BI3wpmdf31PMRPHjOA3ZfVVuu4FR5HzpPrbLf7RlHUhHzaKIzsaW3s%2FVcrPnEveXbuJoavvFTGRQ1ZNc%2BA4Gi6rRYmPiUgCHvlaAb8IiYPCA9Sduj2sCp1PlDWWGIzfUD5Xg55ncQnuCdzJ2Ck1RiNTPypkuBVjQsIE8eINVRtzJmgDuEvMZAxUoaIWnXCxqsI5Mj91%2BE1fjdABPfJOAHfTFF9YiIS1%2BnKawK4fA1WxLL9th8YbZBQ3MhxBdWKNc69KASXMzXhXEvm37B70hLAP5QqCcX5F4jIN91vMSlDpnjEcM7GeXjD4wpKPh0wY6pgEOd3T7g2Xh84IVjMqoiGq5Xcn1u21GJFSQHVpCeDmHw%2FsPjdU%2F5YVzLPEY0STgBhtDQ19l3xkySRDvX0G9CjvRWiByo0iCQ8%2FEB%2FCWKbW7RT3rosukCUrhUi4RN4HeOgfzkvJmkBkoob%2BTcp%2F%2FOFOyvB2steDWRnS5bbOPcVenoH4MvRrur0tHldqI%2F%2BzHAerqul2UmSL9eiV1l%2Ffg7jMT89hdb5oF&X-Amz-Signature=45be261274a971fde2657dbcb232659c193cb91fbbb3008981762db7900f390c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
