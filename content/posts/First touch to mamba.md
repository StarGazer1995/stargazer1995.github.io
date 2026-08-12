---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M5VMK6F%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T070443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXB%2Fw7Gaj%2F6WkTCMN62ie%2BxmWDSf6vcUgKK%2BsZawUTtgIhAKqK6GiBHe9FojHOMCFxg6EMYd3Zy0uNfkHo1mBxTqzMKogECMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx5q4ue%2BxhhhPb2XxMq3AP5MmOtmaQn3ZuSm3BGEvXzImrc%2BNqkHJBMFSrKb1wtH3v5%2Fe0LzwuwKy51HVMOxaTObYP6bQOWJQ0dMYeBviuoLq4fZQ9putcjg6JFVGq99QNYP0W3%2B8Wbi0BcKgOTbAKcNHTxhg5J9hZEZ8n%2FSIPsEE%2B7v9TUKS5yfrSEfO64wyVjtlOV0JlwSk8ZTelqFj1eKaGk4n4oPSJUrY9IPunJSC7Ej4kJOlpDqf45QqMw4EDCgBpRaoh3Q4rGwyGMbusz9d%2Bz9CHk9M7OjWV6qMr5gKTgPuvfdKHALa3FDYTQ7lLBRVO19ynKHvTndJBMgwdWk9INCk1VXSd3noRQlq%2BmzwPNwH7Hs3pxGF0j1N%2FgyiWEop5siriP%2FiGh0%2BJD5utcRURuW9KcBeHkIu9Jlgw4fFA62GEofyqdebc55HjclGss934SzRdcUw0Qm6sP2mUvvaZ%2BW9pc%2Bnu4H9BIA28Y0LiFHp2%2FKe0AWDiPXua14Z2osrB6CXTyWVVfYnCshyuXWSX4At7GFruClzycPL2cJ5x5CsAKobI%2Byi3k2mhM7Tx0uINRb3XScCbTU8zL4RC7PZm3r0mk4%2BIFjuGt%2FcRRuLuwGIDBayMu%2BFTxCdWq%2B%2F6WnSR1sD9XHxIVXDD5qfDTBjqkAUkCfXpSVn4vTpxJ6fkUsw948mg4ANJSDIK53ud0GpBqBgmzNCn4%2B1zhWpojxcMXpIZBEXmwLj83BRtALZLqscaBp4cdcrPr8cyYFLfs9yix%2F20jyi5t1f3EhqXfbBWjXh0KTfzre3azpKXxIu26Euu5GEnw1l5kkbO3K6lswPo57YBXbrUfkZUnZFNDIDreuK0QX1xK2wgpHMPkeYbJiLFK259A&X-Amz-Signature=18ae88c517077f088feecd0850866491c18292cfaf038fd7191d5598bec8d9cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
