---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDFPBQZC%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T072458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA75se0WOSHIbNJmguWNaYht2nsjEtoo7PrQmrNT8M2XAiBPzWA81jZbBXnWCXgo92y33Wvo1XMdVbSXHiqtDjh%2BTir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMZXs606GxIXQjQJZ2KtwDqlyR728HOtTCH78bzqn2VEsdvYYVuVuD8bYEvQ6maB5anrCHGH4%2B26uDrY42vifpghK1jCzH1%2FBrBHmoM4OAmJtuewUYU9IPzCc%2Fhj7OM54J50uadY45SJiNN9NVcjvSiw2DWFqEabAZsOib%2Bcm8P%2FQ5M1XBSlbU0Ddi6XhsGRRL%2FrJBZtkul0RUyxCOr9mxxOxNUFLD8BDrWr16m%2Fm7AYnVV6VZfnVo0tmA%2BdqNOfRnTnX1xyHvpbWjUo%2BZbXPzMTDq8ad9eEvigdSF4dL2GbjThazdmSxmWSLExRnRr0lhECm%2F0fitWRSpVFULQo1Ze9FM6VvOJyXzTiuq9gzBg9yMsUWsLnxufznOvE12tpaS%2BBsMmXxXTHlFIH4qOHBPD4H%2Bmv0Z6nytoEU%2BCBwMHwFV8YCnRyo9kMFYZyzS0guAkLXzDZ4K0ghrdT3qUwztgDljnU2qfl8QK7nn5TPI8%2FiucpgdeavgORSzwPBzhLmqI1maapnK8mYQxmOYPq6CUNhqbrjPEDRFoYVfsQHxXjMsk5ZdiOof3ffTCEJ5SPZTj2l%2FByH7DksDTsTdbAxJjRt9u3daXBhARquzoqNvb2NjbnfVF1C3JAcIoCmJvHr7GQgqem%2FAb4QJw8Yw3sTs0gY6pgE4jUs9SSbElsVY3qibjEiUZ0uF3vTKmW%2Fcv3%2Fsse1MlFs4lMixf6DO%2Baq7yrtuKanD9QoJH5W6tFVEC6P0h8cDJg%2F08cbZDmOuM%2F6LwMVrl5B87RUdV0KlpglLcblfZjIWWC6ABGgATnLrXhy0Mgmh0UFhOpMaUcYExvhqj75UMz6et9opOdfikhpvwiXHYh3s9WdiG7YUrmGJTEgBOwE2Zfb7Pr%2F%2B&X-Amz-Signature=70a1c843d63ae89e84a515f9bd09adfa4f8d931b39cec32ce268f27988f104f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
