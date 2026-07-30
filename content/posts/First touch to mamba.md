---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E5ADILU%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T225511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9SKpdLDRQ%2BlmC8XzOkPJ5GIRd5p24Ebeo3c9wexpuPAiEA%2F0a%2BZTwg9c8R55CHUkI6yuxHhuo0XM%2B%2FJghajHXDgTsqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxPOoXtRP92E9s8kyrcA5SUODXhOaltIPw18El2aS1y8VIhFvESw71yXYfqpG%2BryfU%2BrrcilN%2F%2B30C8xRq%2FyNNf59heuIzWbgYZzh0QyNsPDOcLh7j8LFx%2FjsN%2FRKqHSAlZSzwlC6CmchZr%2FYpvziZHJUhZUvhHKHHnaolv6mILDuB3p6occSrnqFF%2FW%2FZHjE2LxgnpNECB9QPLlhbCYPkVvT9z0hPL8q8uEn6WR0IMA4GjDwE7ZN6u9qB4FeM9oY21G9C%2BG2AQL3cMUIoAdOyG5myg43hVhq8ka800V7hFNVj%2FiAhUz%2B4I29eDICuBr6%2FBlfNkKxgbf6kLOkIWPmJh5Y6MDoj1pz7YH1wKOvQ9SqCw7vPLAJ0PyagW6QUY7VBGHTiNvz9b5PUMlwZILnet%2BvxHCTPikv%2FzKXTuiPa68%2FsowLLgEhqRJSmsZ8QlMnWPfWaZOYS7X45ij%2FhWuZuo%2Bj7tFUAdzqCEsoUXNR26olIg0N%2BwwTk6YUU6CU9ibYKnsXJlcP91m8soKI7WZuP72vu3kGV3kGj5FJSRDlQVfge6SG4RxjllXWwin4kR9MNQCGfgMOjheFHLUATNpFkw9E3Q5leHbQxsZdVl1UAREN1L6LUMwTVGmYdREqE6jb9Zx6bpYQqOtGeRMICkr9MGOqUBBmM%2FmeIc3nwrwlrBjeRWKxhGi7XfH0Uj%2BzarjlPdGE1ts8rTnFNL%2B0%2By2Sbn0uWOdrOnHmw8IpGjRGnKr7zga1SxPvaiJYZGTLBNM1RVS0lB8tFDIpSsKcP1cBVoZgDhJ%2F2l4xkNQETyKkzW9qak1%2Fs7sTc22qpTo8o9RnQleOpHNr%2FY8Jkkooz6pqfxrLwM%2F5%2BrjN6ZmCC63yw04UdQCch2kz5r&X-Amz-Signature=0b105f3a0d3fcfdccffefbcfbd344110cbec27deb40cbe9248672881e951a2eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
