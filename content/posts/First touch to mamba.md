---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWGXAXDC%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T184633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F0pnNsyfVdeYDC1GFTZXG7DyGK1l27o%2B9Xnsv9tgXJQIhAIEWJGnLGbeEJLgmGtQ3HdcYfaQ860kdomxYWaYZiimEKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy84%2F374z5VfAvH25cq3APE414ZnMO8MlA6m35QzerjW%2FiOEKmXBjBk66xTRl9roJB0cJzdRRV7YPI5o%2Fk84XD6erjWFF2YayL6yONj9jnUpz7cQYacKlryQlm84Spp8YxzLfyfFT8FYrE%2FTmVg8MvkMJLfb1gLebDzXgmSPqkoK46Ss2UUyIObnC3IzhQQwLSfsyme4%2FnmHamow3FV7RR0jL4o8Vsz7C%2Fj75NRewXJRZB5N9lI8E7CvyPPIfsNhTbLkqhDSHiNMQcRKUExE7iX910bf6Cvb91oCRkBfYvNtCWx4MFC46Pc1ZeipbWaN5GnCpdMuky%2BrwI83hmggw5TVrL4IjkdiKBbceYwomRZkrXzqnX7hrXgdXr4TqXjkvLC1%2Bs%2FhBjblyRqImVoF927a1hZIoP8bakmSE5cQnfGTuuvqI6YgAufVhNMJ1V03p4j2CivDoQT9Tqfa8SO%2FZZfkeAe3msv3TH8LTkspRU25QjBSyzzGrhq4HNE4Q1QYJwqvTXrMum6M7qKN1%2BOB2gWko%2F%2BSIP4rEofdoXbIz2FA6SDp7dJ%2BnkUTqaW6Fz90yzH%2FCfUwztCtRuz%2FOTdnMo%2FcCbb26ybiuAKZgy2JT649UHRn%2BkBRsRBN2r%2Fl1oNTFOopbBbopuN1HpcXDD5iPTSBjqkAWr0EDJB9ZOVaOAHyYHdGLkQodfYcPZgSQYBEhOdl0BGZCGI4XO48%2Famw4mT4TDWd1B06k3By0ZTd25CApllbppdt%2FRMw91XhX5PkChkjYLbWbkJvc0C13CSoC7oNA9yhURQVuQrZlhf61xl1G9WvHYrSxuIY%2BLLc8QBy5I0FsnorFTSDNjkXyXuqvyZU4EpOnshaigpov34Z0nTrVHxfiY8zo7k&X-Amz-Signature=3ee66c19e19874ca0b59a729d0f77fcdbe4d96b853e5ff126f1ce60d6948a939&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
