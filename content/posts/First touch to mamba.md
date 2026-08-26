---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FUGWVVX%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T025626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDYqwpBAuP4hNEe%2BA8eA5SNFtXK62wAzZVDtAukJQLnkwIhAIA9R3dVkW%2B8HQykbP%2BHVg9mvS82YqJajKAw0nxIEiZ4Kv8DCBMQABoMNjM3NDIzMTgzODA1IgwVMrnotyQuFnFPvogq3ANaqGp%2BREAhQT1YjOd%2FepXLVFrO%2Fa2Ndh4MzXZ5FyjgAGNf0CHuBRrbG4ju6O2h2MltW9gWHurwK32XunhR4KaAqIa5mXm2nYeDSktXxAsRza5cdU1GgMfC7hN6j3dI3r2JXapcP9AcQT%2FwrEK98zJuOAOFwyqqOekBDX0frPLhYBJARWbk3H2FS9knES7ZN0sOFMFAwaDS39pSsE6MnhkRRVhHt%2Fx9AuMBmAkxd1hCao5l8Bts3ZwmeBhvn08KmFVTaW7R7Bifw9FCrhhfzRE3xj8VbDMmUlY1DO94rcK4rCIFGl5Xmd2zPBI9kkAWVtsX2P5TubGAIDNzk%2FPgUxg6%2BFp4h2rnC79MlGj5BU4WNfciiQkcxAQfAxcsrxBdCvLyg8g8OHJm%2FjRvjiqVTC19ZssuF1jRMk7p7bcKD8NKGG74mqQxJj%2BpVAt%2Bf9jal939ZVOY9RWa6BSOuGCT6qHuEN7Sbr87HG%2BDC7NEGmwVY%2Bl0icMT2NDYLhmlAwTgNc0n3uhu5tgHVXXA%2BB8aqYyME5mxVGlA7OHJkTkSNZe1F0zvjON%2BaPyzKoEtHkI40cIrd8K6zomHxk%2Ba0MCbwQL%2BdKDc9Y7vY6wOmevSQqgJcEWYjlrRWemzONeQZjCzmLnUBjqkAbnw%2F66mpdxsJbGRUtTIW8axvaytKyHxQYAw36qDBglHn7HmcYVsMNE3kdhgiwI0LzrhkybnveyBOlJbvR9hVQgMzg4tfGm9ffb0RGy%2BatO3Y%2BiCHSi72RFj02Ide5QD7knP9ndH6gtgvhlCqZNMr41Ekpu3ZyJNYmSfHGku6bshHi37dEN9TGlPCdDd914AzyWb3wGF6cWQ0wgUbMfN8TV4jHyt&X-Amz-Signature=696d460a6ecd069d86b7aeac54380e8ae27d41fa16771ea65f4b84856dcfc06c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
