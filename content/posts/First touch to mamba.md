---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PXDGZCD%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T011747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5XgwEY30qqe5vNC5ru%2Bc0kjSzZ8m7AkOIo1HC%2FQy8UAiEAhO8uSKvYHeGtSvJSLOrrBhTXTGreYTMmPiEkI4GFIYkq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDNkl1naqB2fWrygOFCrcA0NdBhCztNtUqFxaHGqATzX5Ss7nUJxWrdJDwPlbdZqHImrMQpKBowCy6rrntA44nzHsC7mgZ4QsFH%2BI7JREJVCE7MPQukqETNcWlMYxGyVXGRJxsvyskJ%2FVywPnSLtJynZgsw0Aqh8YqfJjQC0UJdE2j%2B5o2NU26Pa3oEXTFWiT9tAKDYjQWfxWZlxsLVhvKyfAT7gQ2M8mme0TpGNlTCpNiDvJwO%2F6OYjjsuakOjDgIj3Ip9z6%2BZq8xdgnFFmPNThhoOW2gnCKTvoDrFA5K4xF35XV1G8Kj2qXPlO%2BYHIc3pXFs%2FhonzXOyInmr2GB%2BQyNe5gQwxr7eLBW9Yr3DfDUAHMPl1r2PNj3vbPrVAQDl1ZVpMYozXeQzS7SrE4h9Z8d7uHQi1wTTjeAvQYcT8eh9LWKKhLVx93IqCw%2FZ0aryKJCt7550pXuXDrHS%2B9SGvhmkI3OZtKwOHzvguKU7z8lV9cPtFWs26WShugb2RYBQGnLHzUB%2FNI%2Fpdk5NHVZd%2FQAsVD67UZGYtaCjUB%2FTC2x5ruKyPYwZs96JwazA5uwG6glbilmnXw%2FeqXAZuezLnQdYXYdHaEgbXN8RkAycX8xqLMDttwVuiDzVMSvbKBFaL3e%2FeZEIq2lNc6tMMum69IGOqUB9r8ETRM5QkObzW0hq26Gk0WPBanzMl2lkfLaj6SX4nhv7GoNBuuEzQ3k1aS3eIhzTa1pSiqdL0AKHPlw4%2BTQPLfJT35LWRlabE57mUz%2F4EW53d4Y4HFKg2yBUKUlTVqbjFnilBcqqvNwm4zYhmGZ4ucZi0qCMHNFcKhttbiftYbyhFvhQEVaTbQ6%2FwRrkdwkqkq611Buzv%2F6gBVz3fk7XHtB8PZW&X-Amz-Signature=829df6607c6389b289888f631a2a5c5e2817d83976962e672c91a5de858f8a65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
