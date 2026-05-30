---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPHZTCDE%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T145908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQD0nl5ryDSHI82O0eKDfaV%2FK%2FfEtgywKycLH40lOtUMNAIhAOjpN7BErRmRxJbh38Fr05tyBhgMSywZ0eSMtpF8Bzk5KogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgywlbZM0XQe2ywaJgcq3AP%2F2hVJmVhRaHNGsUgWDvy9%2BmAN6nySkzCcYThM%2FOjUlkJvIDcww7nrFkQKpNj8lrdNjoq%2BgnNJPwaTDtyVJ0dS4zNK6GpZ3jYistuuTN8KpcmjO6HHb2601eTEWp6pfQ5KLROgmLLYatvhijXtvIGzO9tPcD%2B%2BQrp4BEfUoQGcyJnC94UTjuHo07LSEUlN0ywjGKw76om9sU0rhAESMD%2Bk0KiaJtpN6voRrHU8tHshNMwSDsA2mvg4%2BzOPdNUjHRGtnN25icYBBrBaaw9%2FfKDyVnKS5OWkWWh3YfeBdHoaHh693I8D6KZYppuBYS2xCT%2FbWxfTQyJJOjfzUgMKoyT%2FQ%2F%2F8TP4OwZtQrFTlZJ2afn6YbUolMlI7wasFnJmdcnA0yLwnCkVk370f2H7fHTn3Ygq3FV1UtNWHSH1aKXD4WwNiWhWLEGpvAX24lBJ8dNvj2HkiOhUoMGJXP9kzRplDC%2BgqabgglwFZQWsKTloK1p98%2BFro3e%2FOdT8kCbFx81a6kHf58cyIsIgkiA52X14mcK3sad%2BpKcC5M7KTEx9PAd7THBvSxEARsa7ZwEwBRUrKMiaB1w8R9f453HML%2B%2F2PH3n59QA1Qvkh%2BwfeXwwuyQ21vr%2BCpzQ9nnFKNjCd1%2BvQBjqkAWM4sbXW2PvdiFMR7xC84cyd46r1gwOMqCrfUi4Gb6zq4rXVet0L9YuZOuQGHY2PYeBkMiXEFBbLDsiwl2B9kNkSr4SiMhz5KLz01007qhIvNn97TGPP2Qc1i3mN1h%2Bisvr7vcllFCFgsuSN2N%2FLzJLLVtbNm3h%2B2ZvobcZjx5WMr%2Bx9vTsqCk7CaZ5BqiZS2JlmLqsQui7gsyRmIiMwFKRdUqyb&X-Amz-Signature=a723ea15da37fea8c7e57fadccc5506165f89539f8d6dac9288e17b6158b0823&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
