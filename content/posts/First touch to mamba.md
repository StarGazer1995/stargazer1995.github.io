---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CI3Y2V2%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T161301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBj%2FJjoiRxzK1JZN7ut%2Fd6V8AolaeD%2B%2FimAG0oXWbqVIAiA%2BL1SPsFGx9D5o2sHuI3TEjzrLHgwg%2FBGv51EhjdMgBCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlSM6DmrQcl%2FznhJcKtwDFz1p9NiEAsxsBDi68j7Ic75g57kIKUcCK9RoQdVEORg4YF08%2Bk6N%2Fnh%2BeMO7lbX5nlhA7Rky2%2BxxhFrGLQhB5jtp6Xt4lr5Ux0kfLid7zNiypW%2FxplPOM0WCb1SXrT82STt8%2B1X4LKd7q2%2FXDXu7mSAaCiK0qWUPiZOc4ythQdusG0DyRt7VSEmqf3NIWlO3Wktoqd8na%2FIYHIEpNPXVPPbQpJbHQRqGRQCbpmw%2FYTCp3yzr6aLDSaQ7LEFNjCGeqgMBDr8VJiyb7d%2BOzr39LuDofz4yrVflm1ewaSCkGI%2B0eWSsS3Bly0bP%2BHqlA8LaEGwj19LK9hQUix6HaaAwNceaMFGPCXziIdwcSGqbUhAQa8LznDBiHq9mHvLIff5Pf11tTeQl9D6mWsXxZ0iGjHKLbfbfCcO3OJvMFIvclLkfqBzvFDxztCLnFr3MEKCwERoyoba%2BBTWaFIUj8t38EwXJ%2FMathQrjQYxcKz6z4jT4Q1jLp5GeGgR2bJGyK5uyCfEgbbUwhIYP0ZalUYi4QjLNkw5juc2VgQJz2MKGvjA%2Bw398hOiPEkF809Bc4BuvO8UhbEPeapnY2KRvbswoExgYTR7TdI4zsRtBEr7V4kM5Zm5FBPbgu249PfEwo%2FGy0wY6pgGU02NTxiyEaTVHyUTdxOkKuy9ivmzHhm1rmiTRY8QFOLf33CaDs14KupZ7fhbFTTMGWq3489b7CXhFI60gNSPw%2BY8iVdIXMSsyDeyd%2FIwXoBZb4Lizm3WmMjvkFwbiWh9%2BL%2F9qejOcyFG8tO1qBAKi7Xwa8KGlFjXgpjAUxbHnonPRW9zRXtNZMQVQLpo44ccUjWWHsm4MdvXOWQFnYz7RV4%2Fkoe2W&X-Amz-Signature=ade2ba05e203704ee8a6e9eb8cbcb894c958ab150f38e9dbd1a4691b6efdf25c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
