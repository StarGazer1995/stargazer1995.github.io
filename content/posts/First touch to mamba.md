---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY7SVZ4Y%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T091015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDPJWH710NUShH7jIFznyHuyXQ5OhaGqBgdcOam0rVkCgIhAKJbBHe76syOzBCIZr9GV%2BKPQjrdYkTDxuccGRZL2fG%2BKv8DCAcQABoMNjM3NDIzMTgzODA1Igx0ElKwf8gWw%2By7zxQq3APPX9y71JypGCNCXDSkjLQcxVWfIBU0H0BzMHcief37mJ7Il1ciPFBsqmBOva46q0LJnYwPBOcnTsFo1DNKXeINgswdIGNAfYn9RwwIWkYAqT8XmpjTSZjarw7vDWubscYOV7Pd%2FFkROYnboWB6P2f5AwW3LFv9vohpp126XoRlv7Wh9DLyPCaaB8HHzefSglp6q3hF9iEAxmaroBHON6KxEYGbB5g5mEoJKR5enJpd1BLdHYQOw0UzqlR%2FaMsmqi6OZQavAvDvm%2FCsGQgmywaldZwfNKx5H41IvK9ruzRoEprXN%2BjtCMfcL3wsBkCECxhOoGGWASViQJhhz9kij5Umhu4pvZ3d3az79nkvr8HD9%2ByLL2qruC9dhch4vNV7lBNXKJSWjlIvpfVIcSpWAxwcUBWqnuf5cRD4D%2BjyBE44vQT9lcNorvEs%2Fp3qx%2FOb91GHiZCU3jiTDX1ZqxUOeYTZ%2FqcpKSv1eSHySeFd5evm0mRnYQ7Rc%2B2WET3JlOJzHpfRWLW79kWHgm96sAzf3q%2FQGnvRhZ38A%2BMgvv2iHnsVqphwJeC9MmDpWOoB5wKrjVnFxTaTJ7jCA9p0LauqoOfoaj54kE7GW384YQpjdT6IN721yERN9Vdbdjbm%2FjDYyPTQBjqkAeyTPsJnsVkGj38RiA22N4pyw2FSe9noiyxBLV3EzU9%2Fg79RxEYYwr7kymfGEldQqa5c6bNAEeOvWjobY1yAxmJHLec%2BN9wWOaiguSyCuXhquulmHXhJKXzBfVZhGdwGn2f7UqT1rYX5tiR9BxZaqnkkEiUxQ9K7HDjF4mxjLXFQLzLUW08WKdGjrvwG7fk8j1WBhf4Rmxi%2B7z09jPO67mrPkQ0N&X-Amz-Signature=27fcd4a97b9cddc8899eb670eeb451091e18809c6c7f681be3616499dac7d5bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
