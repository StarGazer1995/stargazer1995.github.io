---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BOK5N4G%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T151312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCICNG8GnJtRSSxzHPXF9d7BJ479%2FO1IS%2BWPEqnp42D6LOAiAOEfCjLaPWZ4XgqYUpdIG1BlF1xXFnAQ3mavwSHPhpyyr%2FAwgIEAAaDDYzNzQyMzE4MzgwNSIMFed7uekH7eUox2nBKtwDHo1RdpL3VS%2Faf0TqhnOnKYZcwjAFFORhtLk3MJsgxCccYS2VLMp%2FYnj14suPiy9vVWYMQ1Tu4fKcI8Ru5wVAaQFs6l9o2R%2BbxUboqYQW63MddvEA0e%2Ft%2Bsomg6%2BugyfB2y%2FU8P1kFFBGl2xTJmmSZfz%2FCTftwCbWm6Xm8YkZmFifqM1HcmMIKqernaeNQ%2Fy%2BJPWW8ew9xnt6ILt9FQpL1QakMuL4KmFVBkp%2BB%2Bv6r6MMQEe%2BuZQnaBpR8D3aKaJwNpzyOnrDCvg449SHPgbG3Ir6gKieQ%2BiWcJVieE%2Fff2WqqckMc3IKLDzY6GkTM3RJfnonHUI9PNpbjhIK%2F%2Bjosng10dVRj1HEfljZYnztYp7fnsAYM%2Bj1myoKtUxKNUrcAF0gwInQZr05b8iTQN1DIiN8XO9lOqsdEA8r5V1jZoy6ikCjmnns5TlBChOGIPubb1mNwAX0S7CW45i1MprYcBG9i8lAwkeVg0553%2B35jydztDHrTTwA5YsvYU1%2BHOyMhaiNlxLQhqFwTCBECI3EUmYIyd9CApW%2BKF%2Fd7kdRCs%2BWkaD%2FLuF3EQkh5gsf8QKvsTPeMC4ttRvsGt9baBY7HCap8bqIoKqPYY9X2Tg8d4qaEmNooE4fnpCVlYYwnI7l0QY6pgHolRTTVpzmgYZsXEg0XjxNJCMSHrNn%2B1CkAx%2Fm4rCURqAHPpZR7JuMOvncNuAzX4AGbnWbKukfjKIJRywTULHXLqYa1yxj1Lje6vU3PzTrGLeeAAtIoD1bRtbEFmYam6rqIbSTazejW8Mtnq4GgISVA%2FrFjD9T0dBxSjLXSaQ2Fhzti7z4K2VSDNhg3rTo98tOc%2F8mM59T8%2Fxy6RfdYTCMtZ1Ba%2B7S&X-Amz-Signature=2119dd18aaf9923c29070b52a868670aded42ba066f20cd7a9920025699bd9f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
