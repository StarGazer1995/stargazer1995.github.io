---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RLB3DB3%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T025152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCjCjTG2%2F6BEr4BWwxX36kmGP4RyDU8ctF83ZWwHNbJmQIhAPTxsN%2FOS%2FXJK69X9lJ7sVxD5HSC4m%2Bxmgh0leh1%2BK04Kv8DCCEQABoMNjM3NDIzMTgzODA1IgzIh1y9fg%2FMbsVXxywq3ANgzKPlSd5cLZOf8wjtqDs4MXzSItv9G4NBKr2BDlyo3I2EultC9ORR3RGQLjDlOmFzoKNNxNeBPv8TTZBidMi70LduwW7hhJYmuvlh9VvwnZ6dam%2FoYdyNqz%2BbuBsz7EttjJFf%2B8Y%2FsO1IgJQTENkjIOT%2FL88l2M8%2B2JwGhjBS7uDGRoAejSjqa8uqvFGJrWIiVoPvTnKLspgE2h6P7FYAZ4%2F4e63XO7IrakDuW8U0RKcqcJGinJ1okkw%2BmG63KLDuAyyV1kr3n6HTXQROWCPbAczeS%2Bgb8MlYuXWX2PUlmMqzTDGYyf1hl999xlCYErDe42cl9GSl9W6TMiOFGrKmtDKhg4D8Et4dCW2qDu92mfbY1USrGtwPZstrVAHBHOmIajfCME2G09MVxcMFxIZOaDd7XsgflkS5JNmBzahPXqJobihOlfjcl8Z4ZApAJfpM%2By8JjSRtpO9BkNbf0275AdJRRPGGHFxNi0mZSgxhojaW8Mzl8yhi4M3Qd%2Fs%2BZnlgzirR5SfqU%2FN94TSXZdoIG%2ByBapW2Lx1R0y66YsxEkmhGxdpCymsNehqUtuh5SabLuMQjkZgChkPr%2BUl1OIfTZdsS%2BlAVensYyzDCzVgD8FGIIV3DsLGOjGYhfTDY64PUBjqkAVjk0UIGnjDXu0MNIabeGCgJv6oTv7D0w67vH8GPskJjXZwQ41yMwU6U%2FnNn%2FjdouuXvuqWVwBSMCrbtsCZbCdTQ8NiOnWT4qweq6MuIatE2mRsCBH5YSAPwGPkF7jY2HPfTdDe53qtuSl%2FpGeEPYl6xX5xNnjHwf0TLUlVSBIrOgDpRd5hsja1DKtPiZhUrfeoShj4ZZpORgdJqA2RiEm8ZuJiO&X-Amz-Signature=fb2056eb4f4be97d596b0c07e36f5a2510746b1c5b5515ff10ab39a3aa1341a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
