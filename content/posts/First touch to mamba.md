---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEHERFYR%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T134148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJGMEQCIDGcb%2F3ILzodqLy1jCkjWxgKv0Z9ON5BLxor%2BALvaNZqAiBL7Kga9R%2Bl9j1kCa5Zf%2FnHHZ5%2F4xCHfQsqCRcYCcEPmir%2FAwgOEAAaDDYzNzQyMzE4MzgwNSIMre%2FbMdI1UlXHFE1HKtwDYEscMTXKh0D9%2FJfKFWhKVbXaX6jTAZjKatB0IrxtyBe%2FaLUP7wesCcAhOC4mAjmqYTKQ38bZFEIrojGQ3O94E3jhu3kMv2w9p00lhQPEq3ElzvWNiY%2FbCQMtB4oRvv2KQr%2BrVH6zjtD4g5Oxm9niJR1Ji1C3zKVgF58x5JdDDGMxeNtGMVnJlQhwopb5MkGv3T7YDLqWYtz3a%2Bnx0P%2B5cOu8zhOYLaOh4FxkdtGqtq%2By%2FPgtu41BfS%2BUk%2BYqHRksgJD2tBZ4gRIrxtQsvhKG8rqRNQN6f4s3fnYCBj2VQGtUlhmGR2mQ%2B8bejjG1%2BfBuAm4wQSVIgvYA7K6FpTxjga0ybLuZ%2F4cV7fek9ClDPw%2BxEA%2B3Ft9rihqgtByh2FmXo13CveRH5liEF0PmLSakD%2FEueJbZAbqVdKa76fdzx462pWbo9Nw6l7nmWTYyvVLqdvOVwQCEdw%2FwFDMuRJDwwhWrRQ8Sa64j%2FhqUKTDS2ye44buDrguz2icTDh4hzIahAbTb7cYpU6iHtpS5CsqyaJd1bJkGsZkWeElzGDCNbByi5bRgWuRrffO3CsupL3rJg%2BYwJtkyVBTFoOl0gpBx6wrguvBWFumzxOz0Mewwdsn%2BVDvOSkUE7HlTM1MwhMHH0wY6pgH8aA99jSbAZ279q5SZnNn849PeeS1pq66%2Bqu5iBKJnPWW%2Fhso263JrrI7ZLgOX3hPcfSC10AUqavYpEpyrbuki312y7X1BsXcrMdCMRw2udxlRd%2BftUBgrOEdfs7UWpqvn78FoNyCGO%2Fs6NNa0wUtzeUjXO0BcsktuT0ClJv1mVFTpQybL43fHs%2F8F6Y5RMps%2Bm9m0GUZIpsEgHJMtaZa%2BY20NM64e&X-Amz-Signature=2a8204d7d131902a633a8722216a77ba8393a798dc6c2478d15196d827f3e147&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
