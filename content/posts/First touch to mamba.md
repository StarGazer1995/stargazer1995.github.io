---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLZ3B5XA%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T124906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDw%2Biy6c0DGyVJXQbuxU3ELkO3Rmcx19N3tDKD9tfaM%2FQIhALDLivi1TyI3C7Z0hji4Q3k6E1iHHCubs8p8SPrIvBg0Kv8DCE0QABoMNjM3NDIzMTgzODA1IgxkfRiyJLe7N9H8YZkq3AOQ8JzsMbpqwQuOcp6cxC9vi30I1wexxjKMyj5dtGrh5Rm6q47dWFQTWsu4oYbJR1f%2BLSLO4UF1ZfwNSDH8rvz%2FRMfolQ%2FO9OHSYWxmybgProoXrrNSBEm7kIJzKS1fyVCN6v2MUpK50dZQ%2FT69ubVbHWPK5S3Oz9UvGNuzOv2fY3V3iLj6iPpjWCKkoSHe91uC2nEGqqA0QlPLmsxVqIZU%2BBGqobY0dwI4ep%2Fti7JP%2F8JfoLerepER0wSJhjkhX6QsaVZMm2qKlF34kpovBXJG5pO%2F6dFac6IwsLM9cf0Q0YgktBhmIPB3vI6ncJcrR3WNZjA2fnWsjPDUutd%2BPS1AApqZlENgPGbeB4QR9zTfpAhz5wrgbFABv1OnqptCMKTl7r83Ll5XiYI%2FhCCe0SOWpCxthBpdlmsDESp05CZrT7XC9Bgnx5w2eyIpxUcQBP12e4Y0SW29sTnAYY4IVfs9LJvSgB%2BkGyjIbQC1P5jEkKjuugAYZj9AdmLGrOBHTVgfeX5iWEdhcrBNr6ZoYsbSOeglaUVjCLUS6Wdk%2B%2ByLr9A76pr2l%2Fmyme53bjvNPDcTgchM3xdAY4FK1NKvwn9KEs8ztqFcRfWYIROPrBqKBJev2RVIUZvQDKWYDzCbl53TBjqkAaO80%2BnJmN%2B6dgUG9SVXhIX7Tkqh%2BmlkNeWx23uxp4FKo3OYf%2BoAnALW1rwtc1%2F8uFE3EU4yh936goJjj6mpi%2FOTe%2BPUth0SyKwphMrmSBpj8SJDDtTNJklVZbp70ToKI0kE%2F0nY42pwTQxCuXzhga2W2OWzoV3FtWfDRLPdyTkSaXA0SXlqti0NwTFWoWGCC5y6DFruz5KUIiUBfeDVwP56OhIX&X-Amz-Signature=16a28bd3b93632fd4fd1247662953183f0bc478810a7e58c3261d40a2aeb43b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
