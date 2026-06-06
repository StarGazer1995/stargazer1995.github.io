---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633BKAVNR%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T054856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpL5ALbVSDguvcucE0inErdJgs%2F7RboLxWDQgw3INzgAIhAPc%2BqiF7QtwRK%2F1jR91xVUmzuFC8WINDbwJtW27xYlLnKv8DCHwQABoMNjM3NDIzMTgzODA1IgyJhXjO3xmNKHPxi9Mq3APWgZxOrlHRL7A1Sb%2FJngwW5Vfi9Wt%2FXCx%2B0DiZ9zs1k2RfBOwUQUefNbQ05oH8YGcUDYbJ3h7xAtDVItdRMdhFL6SXoT9wsJRoJ9XNl1V2mXcrnJJMHaXPnpWGBqJXqsVb5Q%2FtWCiVGVsI64FWROr3OSOGkyuozOcSGDfuOAv3EuOEIEHXDF4nSN3Stsv9NWuo9rozekbmGdPI4OFBdG1bN9389%2Bsnc0YXy0K1%2BHZqQXdRaHCQqNuMbZf1NAamJPKeEAbTA3KraCvERvQjkOZmRsQ%2BoeKai0dYZbZ0h1OPj6m5WS1oTJn6sPvHaXdoQmw%2BqYiXVEJDsqq%2BIV1R%2FoQz2Uj%2FdsXtPJoucA1Vz%2F33r7dUf%2FBmrtQ9UY9F7I2s9dHHoM7wz0uqj1fTZY9uyJLPOFu9Qzk3kOTY%2Fk0ZuGbzWFB8Nz0BsjHbatn%2F9sfwjKQ0cKSwN6PbvTfLrR1Lcitf3XBbc%2BlVhiW7qPOxKUoIk2m7H1LNvhmtXIZ6lUPAJ73ss5lkUaQ0AZJp%2Bx4xzC3DzJuYJNYcVDbPTZVHnUczS%2B%2FzO04jWwVX0ts3g3jD%2FOgttxQrRf83E2l7iAgXLHS%2BgCNHk2F9VbHA9eRU3iUOHmBsakWeYY8reAwhYDDco47RBjqkAes1oeHjy5IULX9wE%2BK0FhE6lzpURmRAxnPoGzbMxGuDZA7XklFxll%2FrcjjgIOOgBy45cVZyRjSr8cROC1jN%2Fw6Y5t0149npk7sm9CjME9yDGvdjQkJcwGO9cLoCGo92M8GuQOcnvFpb377nSmZOgW4%2FlD4nb5UfhJcVrJ53G0xjZqsuRHVRq0weny6QBaAsXZvO3ixHmwc1PJ7m68TyWexkTwI9&X-Amz-Signature=aba58be1afea0943a472b6929a30da9dd60a4e6703c956c63184103a0daf8929&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
