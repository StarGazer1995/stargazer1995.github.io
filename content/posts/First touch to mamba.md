---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDDUQ475%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDeoFygoGh5qrpdTuhsQCxCW6dLmqrqWBX4jmVa3JtJzAIgaxGSJ%2Ft1vFOzqjEQ5Dd6emTxjISEivPDgSOec3rFebMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOmpIUx4KKnpKpkOmSrcA8FboywLhgYRntNmh76J71aPfEUORkb6Ccv04TD8qOSB90rkwLAkAgbxDMXB93cVEIgnpkTNNn6sKLVbd42bshradvOKeeM9oi4pdoxyJ1BUNMvu0BerPewrAS7yYtraTNnP3M4GLoZUJIKL8wsdWj7pIK5Hg69iYeqTck76x2eNIRCy%2F%2FfNVDupDWfex9KBl8ItNECz5va14tAr%2Fg9%2FL%2B4MOTL960Dh%2FLc%2F3uAZalpA08JWu9vNYy%2FuOd2lVc0wFHZKYZLlgRVKI1p3PDhBBUyqxIMIVbSCP17H1WyO0C0Jr15UQPAqUvl4sFfTWPJ24mkKQAom4M3cIBPv4ZMSelnwtCNaZ2%2Fr0B0QJw8oDkA2C9pGV78E2TTSivmsv2Rn0CUVDUUS%2FkwmNdGQ0Fu1V2Ch7m%2BI9LzIyx%2FgQoAuHAhVMxeuTqm%2B3XCd5x0H1ljpotlcT0owHyHJKIyqPtIUuw1E0WTX4XkGmBvkCmpp1%2FJy5ao8pI%2FVqnS7ehvXae%2BMNtJSGGCymYRkrPL83GcoZbkqxVxs9LauqYxs3qmrQobXlVd%2BfhaRZs7EA5EMtTzawaZQAQOh62%2Ba6lHeW8%2BJamGV56diaxMfDUy1HeKJQ68%2FZ2Wazmq6uPXe9kAhMKvNu9YGOqUBusmaxWJE9%2Ft4VQ9s1GV7SmqN40GtnZ9%2BUPVvNNJjvL9s9tXSWNGmSy65HJKZvJCKYfJTH5GtoQziRuyNcsqll8PBHNxZdY7CKohOoaeruCtXuzgA2oeuxeMQj9ZNsr38TFet3PpQW1j1vlZZO%2Bsh99QC%2Fx1wljhR075vTAxpsjOUxftwJIreCdFjY331Zh5%2FI%2BzDI5ajHIkeH%2BGjcTiM52y971wm&X-Amz-Signature=8526042f3e0dd634e94c692843e7f79afda09a9476043b9f75d38fb8f4d216dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
