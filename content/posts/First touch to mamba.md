---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUBPGLO4%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T035441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChpl8PJx0qqL6%2F4XL%2B9yWraiKa5Yxru2KHkXmyVOaPPAIgdt%2B2CYixqv1WPwuIdc3%2BWs%2BNQ%2Bq8YrPwzUWDZ5rK6U4qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhdq9BwPFVisb8%2BLCrcA245FGuSo7PrVFQ9QvJh5E%2BrTDxHSW80lphtJ7h0PvXu73E3ZgaZL252cUBUt7h6Dco8xRPbvqSCDVg3RzN5%2FXVig%2F94JPPdsYlkGZLmqQsTw%2FHlIuARtK3Gu0rKru9GN61eAn7w7sb7hbZqKXMRq08mit6IJLO1DyjlKzdy4Y8%2FinyxlObdSbe5yyzfyvx1dIRmo%2Bvn0QJsJHiqQg8NMX1X6kYd2ySM8dAdjUGZlTyJYxvY9DdEV4mhmtTOLuXAemvvCM68eJMlPSmTNxvvs7kJFBoa0MLgWOBK5bUXQ7oiuFu3hjJCrGW59HlUT2gyAkIkv5Nrjz6ChNGeJXcrHhgDkB6nh1LRiMkoqaO2NlMHoAUoa7gZmAUDG%2FOKOv0p7wuF0N5RUEWW5m1V72Z9%2FFwu8s7AVd%2FpX4wskSXhjWKJrT7iuHA0qzPfb1MNAdsmYYK7H0Iv2in9TOvqnp3ECQDzB0QabDsLXIz7G13dydf2d4ba5q9OJj2GaCQ7EhXO5K%2Bm5dJOhR25z4q2A8TNBCGaqRszNRyWaZlf14hQA3mLDkYZWGfyhJCAcYz1lMKDKgvXcK9milqBpCJTauT3hmTSTJ12y1FxaSnP4wOFlGicJrTXY73vTzLqm7hvMIyu79MGOqUBhKksu5EsGgabwNV3knkKXs3TKGkqk8qRa2zjTGE4iGT%2FIxBjN77mfOkvDg2sFBCR2yW9Cx%2FtDLd54IRzUSaRYfVvp4b6milDEpDtoZD5GW8ruesmjye7%2FG%2BiDEdEi6dCW6p2oc3NxuZi2yhUDTE3SAYnWTXah8LW7D%2Ftny0SxJq9R2ainLw5utep9dWttVTgan37hVfkAaALNRRhEhk5vnodoIV2&X-Amz-Signature=177b3c18dcb9c2662501f7af37b81e799c9719bd7c51945c5c7a8181bd66c198&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
