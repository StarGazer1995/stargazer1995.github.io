---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LNKV6NC%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T202016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfEdrfqhBZ6bpGvUh8fxhRxUy3nDWSqhzTjeFzHSNDFAIhANNh3Cv7LZkfZbtUe1EQFkZmK1W3UKGZpdonsas7KkgUKv8DCFUQABoMNjM3NDIzMTgzODA1IgxZHLkpbUGHi%2FeK%2BJAq3AMKsZeT3hKLbsa0y9gG7qM4susQIBdMTfGdb%2B0v41%2BsZ1WrcvJ2VHIpC30amLB12C%2BvGdQZYQrfp3gTqZMQuMdWZV4uRDBZlQql9uuT4paCLfazrJ5K0iO3yNmK6pRb5TLU2H2Poy1OkG2iYayyvtlqQ%2B8H1qlDMcYvs1moQC7MO8j3ZaxbusZg5gwc3KUb1mLFlBRecNdycrg8jgZBQFsqNa790dRz2yLdYbofpMrm4F%2BYtxwh34O%2FE%2Fwiv%2Bjr7JWvECGk0inzWQUQEyKRyRi6c3kIyx2%2BFz9Qzlju4m6dZJyn4ABdZmrm5TvoXT9FV%2B9WTf6E8z3AgsmEdWR2zAJ7ZpdmOeliiGMquhaCKWpVQzbMmLonSEGUYjlsextZgroh0dW3P1UDPu0UfBh%2BmHE5LVRkhEDviW0wPrGNVLOOjiluRBb75nNFm%2FifP5z%2B8EkCxW3PA%2FNxzzI5E%2F6REVFWM0lWRiu%2F%2FfWRM47tvTAibh0Kz6uw8nrZYDR4PzoCieZ2QBd7R9tvhkhFB9d7P8kG7vg3kfmFZDSrKPQsX2jwLuvW%2BVFL6YJOWxUZcwe1enHvWuBcLykRyUMPJ1h8S3uRcXOgleDruoGsmcJTzkaK3ZdlVZYCOvcgviN8NjCSsPDVBjqkARsyRRCnZtDF2Wl%2FO5c078UqUmpqGQ93D2abbrujijmowBdQAd1vMpi80%2B2xy9xeFqybq%2Bvj2THjzhDnnalsT0krEzxl5sxV4Xw60U0831DcE4VNdeAqtMQ%2FOrT6ilEsyo9tA2jJUpYxMtHvSHq8Rk%2Fa%2FmQXHJZREOEs6LXanlWef%2FVh3yfJ0AJm89cN%2FSggkntfLbifMZqstC7YWVraiINfodOB&X-Amz-Signature=a22c6a4c6b308eb3fdad91057c9f161baafc4abc91a71fdf261271851d0b9bf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
