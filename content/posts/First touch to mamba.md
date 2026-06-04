---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TIJOC5C%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T195335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxyZnaXtOwNYbF3jYzptgxA4B%2FHW9kzh9K7lUpmc5jrAIgYz1TVEd9kXdDQ%2BrsKX5kozqsLzrSHVwE50BO6lXw%2FPEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDG%2BOw905OoAgeqXUgyrcA%2Bkwj7hou4cYVGLWrMkZ%2ByfE7l9mT8UMMxPhNRgtSO6LMG8n72c9OKYma86InUgCDULi%2BQpK5Vvj0LMe%2FyiF6wBvHS9iIitoWao8FQiZ5IeuX10OzgVv5riqrBmWBlW4a0LMLNYQSyG6V1%2B7XEa7nGXtrb2uIV4tw%2Fwkm8F7n14paI4M4M9clJrqHHrG01SBAd29lWX7MLCCt1wNEfXft92EjDAq6SnxkmKR%2FL4AZvIwdpHzYqCKNTb8Ga1B%2Fm7vaIt%2Ff4fP2BHYvYaWycOSuqMT5iY1PIO0gkpQ2szYsNave5a3z79YSPnPgdxmDRMRjoPI19kaL2lautmN5T44WF9pTjKbkW5B1PaBWESQBHouJkFnLXh1V%2BVe6Mq9d11fDaHx3NxDfP2uBmQ0ei6poNvd0F76FfBu6Dzcxf%2BeL2vni2DIMOJPH%2FEIxn6tWdDry4MBThps2ZGEbrTi5cXY%2F6SybPsLr7PiE3tJ4FMUGcA03ByR15eVin5TpEzMop4Xqvjrx7kWEGfXuHXOYWkrmxiCvh0lXwQjSw1y7wtDVaFSAWPUTja2J7imcDONvlVmsvIBOg6s9qJgxIOZ3R%2FanB1W02FaM5rycfZgvPZJVoMByP%2B3tnRP1Vjz9NB4MN%2BphtEGOqUBOsmXCb97FuLmbqjO%2BrGXw9BUVMi3saWHZTFCKOCC%2FFvej99o6jCLzmJmXZTTDwcmxsOOqzumkyYBFFRJC2KNnUuWvNepXME9PwcQ8maRVlBMkPcTLaPHbei9F6xI5i4rYY718md05Tdy7ky8trYRP2ElWp4pLfB%2FgYS7fk7knzaz7H%2BBUi7keE05GCUdrA2l8ios5203tlk8hTZMg17nzKXFYcOx&X-Amz-Signature=23c75aede5996b7b4ff7c94359ce9e23158cfa670bbc5adc34ca6757149387e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
