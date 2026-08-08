---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTACPEUD%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T201617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEQxGiyG2GmuwgWGeylqWeSx7cqxLx7RGU25i0lFcHMAIhAOxxdr2qkq7yftHxXH5nqk%2Fhp%2FyPNA96dEqOSdeivftIKv8DCHQQABoMNjM3NDIzMTgzODA1IgzBOosudWQZr0EviEoq3ANt3xsmzRPB4jvRX2JD2brSDSx5vgjvVHuZR8MuhhnKMcjUtx%2FbOxEnfHV5K9awcIcO5lfrbt7dPJeAJwyM%2B7gp%2FXPVSLZq52XKRFB%2BpNbt18oVVmPkJje%2B7B8tQexcDZqqDY%2BqJwFOuoKycBTHCgNz%2BX4x29eez%2BKKRkX1wfrZwH77tvuOMsxj9Ec4MwQWdHnwP6MeJ%2BqPGwcVNK02liE1EXAFbpBHfikLjZ8pR5LMdVba%2FO7D%2BCYlst6fzvZztZluHT3P5OS4H8JOitwqGZa6GrkcON7kIvvCf4eA6Bdr77cfWNfAECTNhE9OEJGmGm0h4aXhv9MqITh4vg3CODwk33VDDZW0P%2FP%2FzG%2BstWu2qyvPCbwtfWgrGf5QxaTXDQtwCmd3Vwerv17v6gtBNdNANNQCP7zic4Xg8GZM3TzWscNu3%2FR5MzC1sHFvUO2RC5ScCBV9ltuo2%2BcDqegWleqnt9vlwY43ABHVRa%2B10SkxCxmea1JVeJYxwellPRdKJsZfOXrM1w8iC7AftTsoAmfVz2JIijaeEsvkRbmscjmKAWN0dq6YaqDcGjAuHn4hZhkwXLZbk2Lxp0z8V2SfRi0fd0YpBKQUKlfIrlAEQci6nJ%2Fa%2FvukOvRBa41AsTCPht7TBjqkAcGH8PezhycUtHSzhZyghlQqAjFPFQfHHoOuYoCD8dA8B6NQpIhGgyqM5l3YI%2F87oatTbk8UsJMjShVjRTJ1n5QcPn%2FBKJgPIp1eVaXVVQD7eQ4OGEP0lc9uN3OnhC8VwWTBznQwEbLpgTkeUgSh6Qd25nkgBXYTa1AolVEMzOfOqDlmK%2BYis2Dlu4sbSgarkPiQeYPgNViG2K1FZBfz9NwbTSKm&X-Amz-Signature=330c3a71428dee3162f843712e61461de345eee490ba5ddee5833213af19ac3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
