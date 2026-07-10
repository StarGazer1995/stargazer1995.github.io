---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646A5X5AK%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T224855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGxzR8i5lO8pkKRfPPUtVOfBH4RT6xaN%2FJ5ScyuITeg5AiAlTNOpKW2nBPrjz42J%2BngcTMuUF%2BqKkrGnFGOVqzw%2BWSqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4i0c6WFYBAIfrLn6KtwDCUCDOURrSCKZ8r4vKoDuDdsGaINwQWSwa%2BZ6K1A7UnXvKjh0JJ80trY93CHtYg1giVMKtAuKltjXN%2FTfbQnN1bFrp%2BLJPwo2I24X79Swrz%2BF%2Bu5yhtDOnlOzaDsML8xP%2FCDbQijvlLRHi5m%2BXggiPdpJFlB59WSire7wXtiWIyQm1CcCZnL3c4n0Fp9t0nPCON9C7FW9m60%2Fo2VkEU7DnKyDoit7HxCjdmQFUSY63kuZDE%2BJzq2JzvS8Tfe3iYAMjL9e3nfUH8pS1n0Byk2BtqNsGGQJN%2BAFNM6qIheS%2BUo%2BLwx%2BW4oc0mucEkhMQH5%2FjzbWte0DUzweIBICmH3a%2FPWy0wRHfcm3yoOR8cOg2UaNPUzM%2FD3znJGloK13EQS8egZ9LgkB0BSgCv%2FtG4ccG4drthQvt%2Bn3XlCphw2EzsJk7U8GPK2GxOnDZ8DQhh8IZVBZVFc5d%2FXQmU8PPUmz3M%2BqiPST8sP8wgRbezD1bsnSJJvtOq9y9aNg5568xioHeIKW5LtcvM0igyYpSVM9qByZN0RqsSzFgB1wKxzCTOmSY%2FWOCbCnqVF0BCrnm9%2FPqs6pUeZgau42toRwEJcbimnqU2hAT%2FJ%2FSN5MKrCEqKwsjTjxTEKf%2BSSqRkIwoNTF0gY6pgHxfVRciC3zgn%2FsEmsUw2G6ghz9hmkJvyqB%2BMzMt9nXQKVuqePSSAgYXRivnFfA%2FHokgroe6Lz5ZhK3%2Fx4g9rjRZJgtnPBGjm0gmPCRjTEwXhhYl6YnObaG%2FPchndZEFOP3uN4TumRV%2FzymOy4dBNenUBwqWAXIcypE1lPgvB4dibchT4%2FEDjLMrYVb%2FouEGvgJDYX5ZuTcNSL4yuJgkHzoNpzhXKeH&X-Amz-Signature=2979749b9cf24cae1e069a3403c72ef6a93d70c628ef762e5fb9fb3aeaec083c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
