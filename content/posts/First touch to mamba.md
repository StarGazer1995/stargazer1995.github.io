---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W23YE3RP%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T203922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIG8BNd1Zzbp5C9bPLQ%2FOLgfI4025POa0vkrk552pwtSRAiAkkdk757pPmiCcwmM%2BJEmSOIhG4ECBokXaOC2VcNakHCr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMLt4GGg1zSFZAgNvRKtwDOAY3tBm7BTyZyza1%2B%2F7OZErxpg1nsfRu3ipEsumWTD0CfFhM2nNXXyOV47ST%2BQlMcRo0jwp%2BlgYQWanmaOwUFFLWfL6P8%2FOlhr6DQL7DGDKz3KjcPuz9sWs%2Bw3yoG5kcu0ShTpehY4%2Bmjr252k%2FF%2BrVuIA5Aa5cIXWKb5%2FzJls8tme4NL9HNdONC5LY3a%2FKQ1FbbwkAQPytSazFKuZcy0KawPurP%2FlomakcX9uXaUKKF9f%2BUuaQFvKmKRnBfateLKslDarXPjnNZZt5ioLfJaBJDz8op0RyRnxAkyIeQorsvGqomDZub%2F8qh1ablOBI5ICBK6%2Bicm1cfyJA%2BiYRvawiSKiWalleMYgVjbKejJgA3DpnFXp6nBd%2FGgjO93iYPBbVHfTh7uCmvj8XzSzU69ChwYotZz%2FrPWzxDpcWiMS3cC2viwV6lz2CHbyektebi%2FG6szwNC3q8N5z8XjfIwFy4%2FF3OYIRS2b1p5pyJP%2FnTr0zCENe73EQP2n73WEXcbJxeZLIz6avAZ4BHlu6mNkIdDTFYRTQB06QHyxyD%2FzHe%2F5NkWzOIdC7HTifDkPaYjN8DwTUaucxKb19i8Ing8o1%2FawcIvPgjbICDoKbcu96S6f4zCj%2FX5sK2r6f8w67fH0AY6pgHhpDTrlw%2B9psrFo89jBxLCs9kMMkgY5drwemq2kW7PcbbLBkEOVHpg3%2BYGF9eA41AXDPC4KmpjlWXG8Ti8fv6%2BRT3ZzADq6tYa%2FCtkKbM%2BJdIswknMTketpc0GuzbbgkfjBJpJBEB2FjPD3pZ7EtrwBdTfVP2ZDQ2cVPeK%2B5IC6CO5%2B4VKyYoEquGKrR6RF7KjgSaWhiYWwUlXbedxCfTosFd7KKrV&X-Amz-Signature=ddcb718d4eb7ae2af7d3c32f4a43715ba7ea5302c938792dd56d6289db85cdf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
