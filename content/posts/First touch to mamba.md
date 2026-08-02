---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y4U7SGC%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIGdnYDDXZLjtsTgEMJ3ad9vhIpaZwC9CoMkYFI58gA5PAiEA3Qf9%2Bqgq3cJiHk4k34reBMwsuLqLzAbA1jC%2FvsHBsvsqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGH7botplriJq8ictircA4EOqN64lUOdXWQSVieaAIc4yLqbcdjeTxIkQEKW6%2B3e4dV8EQz%2BSsW%2FTcuz9LczpQaEL1%2FCHveofRKcj9YlJmUSL1O7LrDyubFY1hr3kw0c5cXxkWkUfciJThRdJWfNK90ERwgqTaqYs5XvgGN1GaKoVkqvHPFi1KQ612v0PGanuFF8agXJwKfpaygeJUJgr4WoII5de0LVJKcKCkOuYqajgIxrM5g5Ylp5BSoB0BFRrINvhFvbPQIRv0fd3hWjjglOKQbA9nz9%2FzKF88LxqpWCZf12vpqwIvM72oL88iCwWbwxP2ep82%2FMTlncWrGujAhjdTOOU%2BShpf9oXTcbNPJVVy28k26gVpLLFLbMt%2BwUkPgN5GDS4wLY4Rc5kMfjNFJe6ax5Otk3lXDfs0t%2Bgk7kycjm2mRA1UbgIbnFKaDf2rNYWHK4bX%2F1M%2FuIlvxNzmWF7a0iP5ojzhK3rXBOTVEqy17XZdB60bX1LDwhM%2Be3sMpulc32fPxs4yN3Kklg7ccszt6GcAiAYQ6DWJ0YzqEx7rRkNrOsl%2FA2%2BWqZdGIuaun8waAmMij53Y8zRD539%2F0VLAryT7KqEOII34t333uwQYP7P4NmyfXd4Y7PGX1Hd5eCjbv%2BWjnst%2BoYMKbButMGOqUBnOEmw1yH%2BbpYCBkP79yPUxSSUYsez%2FQ4sudiKXXiRiHHfl7a2YcQCHTAEAoBlBqs%2B2eatD%2F0jszqgoPZwvpb%2FX%2Ba5x8XjRNcmhh08QQCTIblNn4qe%2FaNJRe7ynL%2BkA%2F%2B02ozrzR2C%2FdMs9iloQgZ91k68l4hK7SmuIF7YoXB7GnZVfyP8hFSu7LlP%2B1%2BmIPs0MVqDm1fiXinfEQGlG5V3yUe81JZ&X-Amz-Signature=171aac9e616ab18aa6d363b6fc83513ee4ee9a1b15a64956dab6b5f23c9b91f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
