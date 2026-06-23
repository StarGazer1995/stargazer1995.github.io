---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI4RZWSH%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T174501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJGMEQCIBDocvFrIZ9mQoAkjkiRelDMWDPtqicykA6el7EnFRKDAiBSA0H2SqY8hR329GE65kq0hfAFQiX4zQS7%2BeiVVt0oGyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMB3462GHLr3%2F5okvJKtwDLd%2FZFIXoQ8KTcBhhJPtXXPOLllQYY3xkbhK7mRXRqgLMJukc334oooJxl91E7lcaHQexfij%2F%2B86uv%2BLbLbd8YpaaeMeckHT0%2BLag5ijo4XJqtOh3%2FlRHL2KABnvahLNUVgcs3burZI4HDEA642QFxz1UsaJl%2B5g4%2F2zdWBesh%2BVbVYBHTEVAK9WZerTcqrcnQTwpVUajjYspMHEmlirc6U0jKHdkUlMtaJ%2FQ76poT1fs611Pm8KPX0Fc9%2FP%2FdkOA4aR%2F83NQIkGIaqBMXpWJpfXwJJ1BN44oybgkUy0wEKDe8vb%2Bx3R1SPBJszgmunO2hHuFIJodIjditjHg67MuwEvPpmFGy8epRUzrepSQY8eUuNha5EchLUV3uEnY6jcBERTLw4tZWHP6joAvVN5m1naV%2B4cS%2BYr6AEZz%2BtSVZ%2B5QGuf%2BpyteD5yqz8KxXT0XMCfccOplxIsUNakoiqhqiDKupaTaVf%2BzlbHdNJnbzq%2BqSvCIFlgIDgjxE%2FX%2FwiBg9zW0S8nvQymTJutbRlM9mgRTG%2FJWbAZlaAhjyOnkISPciKEh4Aj6DBuHQGOZolr3rg9l2lLVYIZ560nqscOqqziYhpUxzl1s4uuSG59nrj3A%2FBiOHEjxMexnP6ow1%2F%2Fq0QY6pgEIV%2BhUc%2FkWCXG1IbA2EWsB9VWD9XFwvzcQ8UtKZj%2BBmkmk9fE4aLiFN1JHHhBSA6LOlkCNaTZpJ%2FZVYH8h6hDgCA9qtHGWpQBoCQrGOYJFIaKMu0KMcAvDN10atT6oQ4ltoPMIxwHmhzN6HcGFrwWsrBOUe4kt4HjoAV8doXGrMAv%2BTBvbvDGDJ%2BPvgzEzDbnx9rGTi8AuvHti0phZZ6qeAd%2F9xkME&X-Amz-Signature=3ccf3986b2c93f4b9b087952e444ef9a46fbdd5df1098605d1f973dace48b063&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
