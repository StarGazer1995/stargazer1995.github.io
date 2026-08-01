---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UB3FZJB%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T224343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQD3kDCA0dBtPnbsN9j1%2F02oaph0kUlcC%2F81kntvN4QEbAIgS7tUEsqNiATiAX%2F%2FjPDVBAdIx%2Be%2FFjcBXizAl%2FwS6cAqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCuXXa8TaTbMb%2BnNaCrcAyRJJgER8MOaPnOggQWw58G5XmBt%2FlLIfDY3rOzOCf0%2F31Jzjo%2BVsI1a3XBCbvnJvEL0PpZUtiqzlK1zoSGybSnghkNZJrhr1StO4i%2FHYXyd%2FPpZzeBdkHLWJqj9WXPeOVwuB3ZasypYkgOg7ZtQy1yR%2FoKiAbrlnjCVgIQhCRJeKIMAwEF1j8vw06TYn6VLQPsGVuwJYoGEw6OAo2fm%2Fj4gx2Z2xYIQokf6B7wzujCZdPmcVyMO%2F1dfVJwbHXiUaOjtkBLRgTEllSP4Pe78uFIHH5m4JTq1aGaaqrE0QoFcaWJMoeiMBpvyyUw7ymxKLQdRepZmXiv5NRlODT9c2ItL25tzYa5mReMOk4n5KgRJp4FgPaUsKWfIWQ8AiAYRubYEZCN5CICNh%2BVZiMxdP4G3DpQZv1J%2FRAddkTj%2FDbjf%2BdYWbsWgudrxII5aYgBAL2NTvnl91mmNtVDSDAtiiGDsdT7fPoiqo1vzv1%2F%2Bs76xLHHmlcU8pJ7OieZNCCVpGFFjv%2F%2Fw5qHJpqIEMiCONVBf9kgyaiXTKB74d8VlduUCXV80%2F%2BwPwsBOhYodkerNB%2FL89KCyfbF7RrmkcqqkyoZvQFfTGux5juVwWYfRqd%2FG5oJ0n8NFF2loJxc0MOfSudMGOqUByEJ8EcTkSKiGOvo6F606lP506RwnVW9XeIJ2o%2F%2BhMd4s6MTsgd9CKNO1ITczKUD3%2FC9%2F5sd4EgtN6w9kW5XdIaNT9wltz5Aya4oCbux9OlWcdtJM3ALWv%2BXyptpQEEQi8hfi3G1k3VBDJIfLYKXaC%2F%2FNRvKbxKeG9jmf5NPZANQhL2A05OUhbky7k21U%2B%2FJ8ePOjwGk%2BxSTiJZnNy81X8QKCDkhO&X-Amz-Signature=d418b484d7d5fc57fe432a01b7b9842738a64740de47609ce065f8d167640b8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
