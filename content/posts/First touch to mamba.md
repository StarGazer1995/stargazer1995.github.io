---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGQEJJIL%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T125741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJGMEQCIBqpfxEyjbUawhzqyqK31%2FQ27VNkuLXo0tnGvOigNb3nAiAagJWI9LUd4bNW3GpOK29RDeGKTX3ves3PZt6b9QDCJCqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq0ro%2FUZiAYLJH%2BYbKtwDXXN5s1DFQHYEXiwYGYRHZehyUpIMT9l4BaSl4E%2Fm2mYrqZFVrRQsvTVXeZ362nNIn7QQo3oqf%2BE09LmK4voDOi7PERm2dfqlarzCALDDx3hY4ox2%2FQjUFIUZpQeTqQCXaGnOJRmhXR%2BlEwvwe0Z6YetBLCIKVJLh6nkirXFLc%2B1K8nLg%2B4xcWgPcWKvFkBkF76xH1q%2F7d3Bv67EycgcKlLz3PRVXc5sPLwPrROb78bg9%2B5Zr8iVQXULI2GHkLxNLFaWCRmlg%2Bti5AZ6WbbJu1GaB4vZrwEuXHZdvExa%2BrboArwfj25D81pog3WyijDbAFh6BwZeaSkF0sFlcH0ZXkEKuk%2FgH3Ey41R%2BCkVlamqxBRWXAzdBmr2hRaGXNUzQLAQqQEruP26QIIRXzjOM8Z33ZvuegYu3R2cojNbkx%2BlV%2FGpVPHoFF%2BjxjkaCRNDN15SLSwl3%2Fn1trGGXqKq4xOULvma5GmSsi%2FMjsCEpC6Wq8cAmve45bQBNO1j0NCjDNVUh03jrZKsA7A7inS6wJwnWIIhWf1fXXQWwhw9Vft0oBDDpPAcP36TrIU68qfERAkS%2FNRW9VcawGFxTC0wKxBmqmPIVv8eAup5Y6J5ISVEFQjOJFbXVwWROAqUQw0N2k1QY6pgHGKOAbuX5NBLBmHJMVZ1cUZ2n5N9zbjEl8RntK%2FPFw3BTWHNq%2BNh5G92IPFacs%2Fv8P9wgEOqnCuJR3r8uu1eQo0T7VyT3tSXAVAshzwSqfVdQDIYVfVgt5iQVbdiBv2MgU5MXOqmun1eHMDGEdElZaJ18QqSO27%2BYvzMjJY4XjzzkC2gs15L3FzASJRe08hoC97LVutseu6IAQ6Y2iKhU8dIHtpL7%2B&X-Amz-Signature=1fdd51faaade3756c0b7c16d08fb873137cbafec65dd03f0d3915d15a3c71e59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
