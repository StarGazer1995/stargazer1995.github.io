---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBUUU6L7%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T224703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJHMEUCIBbTapH23mQIDiEt3WXGNqaMYlM5w11p6NcyjHnwcAujAiEA%2FWIwNiFVVgDcGTdf39H%2F7NkU4l4L%2Fi8Xt0rQzA3GeFgqiAQI%2Fv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7RYdubFf7ZhdCV1SrcA%2BGH5to3QOXeitUvVkqk71qeiaO47zTI8K104eRJkVEXZxZcnkcCMb91ezCa737MAGM8QeaOXEpQ%2BI3G2mFwe38WE7%2BoacLCceG15WhAOERASse50u3D8biJb77DLVgZTArjtkhDiRZn53sJcJIOfkfUnmQg8xtQDx2z6lmGu1GUhum8q3QEcJ2Q%2BiS9CaK9jj%2BbpxQT4gfW6DONBUJmxMWoeakrNNjMeXeAwjzce056tR3W4ZJz0r7pVO1lpDRWk8S0ir%2BSuwxxm%2F9HLNTX4ZvwsFKDCj%2FgpbZk2GSHtD6eTwMvm4OPZn%2FPUk4ntsZV96wU7Fc5LFILwuuqZP3fHBATBM%2FzrVwg9hFHBeHj34OonN09hF2T1coAkdWYwR%2BoZRay%2FXnF9D83bdPvDj%2BCoG4DDFVvmGlAZq27aluSDoCLR466tP74itjfjMQrKg5kt5dCqAxoO5Ld4CPgKbaxp1jkFlEZE8GTtBNRCOCnDL6ZRwCsvIbKL76KdKosE1sVArLeIGW7V%2B9r2YwfkD40CRSm3jpZG1AoEjTxWF3mOIBazUU%2BodV1FCtNgYXMEGG0CW5WBJsFZoV%2BKyuED9I%2FnRqvJP5AMEJ1P4PgL%2B0lDdaStGWLNX89z8fQQlHBMM%2B38tAGOqUB0gAUyOsn6xY7cJDZKA1NldhmYHRv1pjzxf9daYQgfDPtU%2BHcR0FYjKU8q4h7RDU7WaSwsjBvTs5FcWf65RQYHyO0t7THNCMGsh9RzlSjZcN53OkzXqS2HyH8rTYD13iomc2XJH20w0UnUU2HtSorRy4EUJ7AuuyFrKn75WNNXYoDg5wKEN1GqaizmAIWoR01Vox1CFqqhxt%2F71G%2B%2FJ3SJTL%2Brh0l&X-Amz-Signature=29d49642566fa2bac805b9f81222d9279ea737e5ebb5ef1cb61e86610d4ab4b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
