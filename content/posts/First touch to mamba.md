---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TREV7W43%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T205719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLxCO3UEf3jw6qwr7iwqRKyFnWBfx9yGKWAPu8fHiy5AiAb1wMrGgar757YeQSwbQxcOP9eIOCFq9%2BCKvXpVjlCRiqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLSW%2BbHV1Rr2hnL0VKtwD86qbIqZFQl78vlfNx546KjAhas55zGFGmgxDhRvvyacv3QJ%2FdevhzcEhm1%2FzhdO3lHdkOa54G1OLqzSxq2Sc5VnJBNZTCq6W6XxJQXh4%2FIde10mFx94d2ZpAXvU8F0aZT4XMFPof35xIRXgPQIpIhJX4yylUH3hDQ%2BG3R%2FeBzKRZTXIC0IEe%2BI8yFBDFZ2Fq0cIsUuPpOsGXE6nXjyOAqnw2h4dtAvnP9AVm0NT5VIsU48XdZcM9Op5ksZUoWC3NzjuIzifkKmgdrvJhc4Q2GCWiwfzxlRP4oYZY9ln2zH3L9NgySBnQRXO2l4PUNcRaV58%2FN7%2BHCFVapKi9oBBVemcnEyKrFpLhHYfsRib84gXsJk13m65%2BMexaEBKwYgckGnDuhQS89oJ7f4QaNAHPRGoVoF2On6UFS0GSG3WULp83K9nqBuv3C%2B6qTDEjV3SZ0sBH7ddvqc3EVR8m7MoPEpDUriYm4LMhjAwna40Z0e10i%2BmRdisw08dsgFF0W3rcYiwjbDsCLUR0UuRvzzFby60K2reEpLPXT6A1s6SRGzphsTjexlve3BKUUoj007AlLGjQ3LqUGR7yEsjwPxkuhf5yhafmDLHDWropalIjR2j3yC6uapveBjNMdYMwmNzzzwY6pgGSRkk7FL04ZRD6rGTPWvXgSWuJzcGHEDuEygDdXQ78wYuEyO%2FYS57AakPUjALL7JyDDqrLY9Jro62Cs6ELAZmcOFdONKAL4s49C2IgcTG07A8fyPfdQy3uN0LD6kbOJGHlZOK5qVeKeemzHs%2B5pK6WiDNITkg5A3K3OJpJ%2FfD9M%2BOOradYGvglqy%2BUD7Ru3CE3OWHzzO%2F5712ZODrDeopL8GFD%2FLlW&X-Amz-Signature=46140bad0856a69b2d7f23dbb47d441fa3d693a35e00e9a2f64f1eedef9f0c85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
