---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUZYTRAH%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T003259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHELd0dXka67XDcehy10P8U6gG%2B4JedXUwf5WGle1wPgIhAK49Lywsqr2tGmD2mnMbas0Y1uCZnWf1siZcO0ChaTgaKv8DCGkQABoMNjM3NDIzMTgzODA1IgzwHNM16FGWZGycvPYq3AOpmHluQkvRlANA%2FkiM1UyXycFjT75Y2CgBsL8GdjQLszlhgC3YxMpcda8NN373QRmSF9T82tcl%2BbxJ%2FlQq2XdswpdRhMY4HFxrC9sirG5PNcSJZvzgwsIkwZ2pDZI6yLiuG80eTiwo0PXmmeK2pr3VExB%2B4Bnwo9fg2uNTAw%2BRftOEMfT9Lhir0eec%2FsYGPq9265cJ0aWE%2F%2FwFwDpy7S%2B5cJbZ0Nli7NNhkzstT1Yf5SJnZsyhyzp580eTSSDK6IiBsny6ReK3eap%2F6AretPHbiE2XNzjcZu%2B4Q9Rj5jjU2BvXwxjqBRKDChE%2BjH76NZB5Z%2F11eHZ0wWzkJjnSzp9MIuW0xuSxV8Uw%2BEe4sqVzfGm7%2Fo3O4hfFp%2FQuuHJdeR59p5I6CWHtnk8N5nvLRbB5260ImccP1jjhqRZC1wg2WLNlCjLLwZ5fiLq5oISQ2ooAKu0sJDSK1SRh0x8RNZmNA1QYAAHkDGNZzEZCudqOwuv6QgEAziavO8yxsyFNypI8IGuSFl7iMmcxNyLW7uXIS1syBKdkrcXysIw2iyx%2BkNILZgx4nCJBBYJsQQ73iujexIWYO6TxMDLavS8oDnd%2Fq1%2FCaFlzuXnX3cfMx4YTi8r5W0qRE57mxN639DDY3ZPUBjqkAR53VluOVqJ3PGWb7Oy8b2e2HljptZ0jqILcLj0829X6I%2BGPgrI1tIIY1L%2B9II7PA59eURA9J15W%2Fe8KpnFM9qGgYcw8bC6%2FHxarfbA2e9y4KPk%2Bb1Bqwl6w0reHSfGSJ0TF%2FpmXH8%2F9SqBnKkFh4nCtbk707BGLUG8jBPE%2F2Gj9FKoDQBLAL0NI2R62853SlJNQ47FFyjAHHvyrKJ5Y2HyAk%2BtA&X-Amz-Signature=4e9eee2b4666af92e81de8417c60eaafcbfd511838b4f22dee8d9c0b86692832&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
