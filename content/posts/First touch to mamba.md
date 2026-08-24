---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTD4EWOM%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T025515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIG1Zu5hZb0tB7%2B7Phm1OIQzstU4GWnMGUsN05GMhi9D8AiEAuD5WP1eB7hcmFCkqYG4SBMFPgNQ0zVVpucpvaD%2BN5HAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUofT0bI1tow8X%2B6yrcA0GW6xn6JM%2BvXO69b37atr%2Bcw3HvvkU%2FHfzhhhBmoTIMgkgppDnN7OPay3SQE2ezhwLKDKF1apGBJqNOy4KR9YCFGqoKO9WcJsNFvrolsj7hHlbBgz51%2F%2FjiOrkGrhUaKrS7IXiyDB89tKFuTC9djtLNqeNn5ELQi5xTuFpaVUp6OQgtUyhncMiQIwi6jEtU1N6bGzc4KuhTMWtpWBLye0x3yMo1DxLhVfHG15Bv01ebIsvjHaCDFcHC%2B0PXZkD89SfEgOGvZCdD7iBvr78UzVnqEvYvzziubnEG%2BbUzo%2FvUpObAwYafx1EsjVUBbkSiPglhAMQml4Ez%2BDJvvBa1%2FZDo7iSyj%2FVOAcmyzWlA%2F24a7j1BccRzreFiyfFNMBpGuwD%2F1qQD2VhxkKxXubXslcU6AcadHpw8AvYqhiTI6xNExlUn4NkK3CdwxLXnoK2i7iFJBKiUlApsCI71AgyKZfPx1pU%2FvoWNdEJu55Wz6UvB66rHFdobpeCEQGwEa3SR6sdN2%2F86lttmGTAmjfF2kUiBrFGoVLS3QSsC0FDr77aQbPcQMsSiUoCo6SnzWfQwHem0OQOwkaPgx2529j41hL0Xl5v84ksFR%2FQNo6uzZlkaAzbiGauDSB2Qnp5yMNO4rtQGOqUBUj%2BX3K0sLTCMaDjhZl6VNm%2BQGzzieW%2BdJuvnTtvfvHtu4BW%2FCXaf3KuIFMTrge%2BHQTl572cCjJkYZ8t4lECWjFAiKJcYPH8OsfkaGgnwphVEJ816nduYR9K8QNGiSO8XM4wZEpuvCECDw3iGwnlhx8GMLhYeT8arV5qwjfYymsxpW63IdwzUXwIqKSHFEQj79azCJE14U4du%2F72mhDGwKQxuq5W%2B&X-Amz-Signature=2ac0892c7cf18367250c33c110f79acfe72cb0d7fe57b27b450b10374b3d5f3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
