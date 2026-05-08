---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EAJT3EG%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T015126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8U7r2Ljfcu1GUP27xwDKaIJ5xbx8Q29eikaAH0VpSCQIhAKuM7uxB90RJ8%2FgcwePCHtGOJbz69%2B4bjxz5s4j9OCZCKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwy4jmHAtbosCCTg78q3ANHPETvHK658aoG%2FsNVmSxa0xTn394qZiilizLiL7OBlyrgYIXyyTGG%2F7zFaqBuJistLw6jrqxzZYppOiNND3VkI4B2TvT%2B%2BeNrOTJWNf4ibxVWl7t8aODaVG9GDExWJKKnWaKueb8ljkggYTNvHDvDxJ73Xi78gEsMX02IrUO30CPy5DbJ4yuI7ramJiZdaJWwoWaDrwN1WQI8GOb3gu4ShldYDjnT52YpoXYQL0NRuGtYqYip4koOAV8SpCr6r29gT2sO0ohJWufcmTTZz%2FbRMJCYYrq0qauAMXE%2Foi3B1KOtyKsUg3NaS4qWDmtc1u8%2FOr25G3LqxVz2fTmwUvdvkFqR7aDShHQjS%2Fz3fTwKX9%2FWrFr3x%2F%2FPPmRPF9WE%2FIkWmvVX12lIN%2Fg40anYvrANnyek5OZee0pfRl9RN9rIwUHH5Tz5%2FEGawlrnIoAEA2P2leXjXSAUbUgzf4y%2FFnLhpjhvuKJz8SWTj83sdGOAWK9MfQiGBkpG89WnArsyCj0wGfqdMJdJWYaxqa3LNy0u96JLmF92EvdwnIPzKvDrTbjl71okiIzaHj%2FkvHKWhyS82W3xvHAftPdR4NkzlFAfxNHqEq64gK3EKKGoyaNU3sI8%2B7XivMKGibpPsTCb8%2FTPBjqkAZFz9RTLWX48u5HmuzRn6IZz82YQyTB5S1HdPW4zKfgESyTtV5nbfd7O%2B6pTzlgtZ8eqj9xxmM5a%2Fdgl93G32YFy2fwylqRw1KPonfW%2FwgTsUyopujqwO2ScoQXSA1IBgQs7q8Y14QDNaCIN9dmx3SvPvd2f6XjSZPryOzV4ZyAErhGyx0wDnSwboBX4pycwWVQ5JWWSEsDJUllducHG91C7H2Tj&X-Amz-Signature=310245407805be7a25af0f6ff01a4e0d0d71ae3bdfc0462cc050962f06f29aad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
