---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6RKMYPS%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T215323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNC%2BlXRMgItbECNEaszHtwFEZPPYiiHIsqK57e5N3YJAiAL4as6%2BvKYWmWzQwfIe9EPhuh9vb%2Be6KbMvqTzeejpNSqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqt8uQtBc67RaYRPFKtwD6QE56ETtXiUlXgFJgkUImT86arW%2Bn5n958hfRGQvxJ2FAFe%2BMWs0sxUl1MUqwBNVvDqwaC6Tn7l8xDMPWu59waufs13IU2GPsTekz0wD253RtTtBa9WHYsbY3Oru3AJoSIIoezJbC3lJlw8JpcVbHAlIqO9iTz44YrneH5Lt3w7CjZWz7HK%2B1q56n6LSdaiUM4dSO8QH4wzTlus78a4qkfkV%2B1ivVGRl2PIyaHXwPIegbK1GuG86S%2BMfGwzYWmjTWLX6GeN7jEDsn8WhcWNlgmfzZZE8AIMKTGxHkngScmfiNyF0mqKmM1tBpRW5lBwcVC33MZTwmL8WMYOaAbpF%2B3Oz3mFXzkCqf13RVsL60I4j1yYH8JmkMRP%2FgbPUCzWhnU%2F89NisuXHYh4JIubLRM1RYis6X9qktYidBf%2BJFIoModHjkVp%2FaUihEyLSiVaeplco1APCcNmo7fy2D2CgZcgNWnSkhNVw2l3fOEOgY%2BSv%2F3rvpBMM46XIA9Ux7MXQXH0n5JIatFk0rpKSY0XNfKzv%2FU4ibxkBzHgerUeZryvFR8rTIRphjiRPzFViHlQHG%2F4YDj0BACZg8IkijnQGWY316yMr81Jc1WA2P%2FLouDOO2ceJ2bo7l6joVPLkwmIDM0QY6pgEDq1fvALgGiRCtAloWzKyPzyDJS2FG1PEpfd4nCUsHmaSUkvovyQ2pViiM%2FMi84cD6owUl0o7iiK2llV0Ezgn8aFF5ASIzIen92ww2cuvlG0cfy1KBU%2BP0bUXSgeuvSkej7w0Wn1BBU4CMlWep00PlDYtwq%2BkFQf4SQfqIhaDD8RDoSsRJB7WBiZSQK555fYY7LrS8PS5GegH5grjczhKfc68AhKPd&X-Amz-Signature=8be9cfd36bfe509136a1980be04b2aeb11d21d83943039063f3ed4ef6e86b8d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
