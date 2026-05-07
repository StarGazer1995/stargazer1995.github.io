---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV2EYEZU%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T155911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH08%2FuC7FP14KbmKLznLNz52I%2Fm%2F7%2BEAQqprw%2F4DL25gIga0VzD0e7P8PqmJ2fBPqz3tWtgdbWnFhjPTVjdShhcAEqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQmJmNKHqs0r3SRYCrcA8aWpm1mgSFzq4kaEaLGs2zhRiztk1U%2BfJgvfyh1BPwTcaWC9GIOHP6Kf69D0JTFOS5vp5bQOI9BWai%2Bu167r5iUJPPMVBGLrkqlMYjbtlJxPUb7HL8gySIQkqwA8%2BgazKVX2uQ1MqcruKNB5n00GkOMIDfUa2L8AE9bRRCz8kJVwToZmKqyNF00ella%2Bib1JUkMoqUnsVyrbePX3PzAVAF8%2BShT2rqXoFj8FadmpEJ9z4rek70fqQM4N2qq62Jm7xYJFhWKVcxfXRcw9KEs70ud94aL8wIAtMqOTMWTHkCS2eJD4iDC2xiAdI0aCC6ldTEuOxsf8kEgYkJNVfZZaY3oUfF2xLI6XY8rgFzHn1Stm0egsvX3WO%2FvkXO3OGeQ87%2FKh9uyU2ZdfOgkpqzrb8s050j3uBZvJN3eRTec1EvkgHOGG8Cz%2BXZ22jKQfistjgmKZ8KHRP%2FlPKL%2B%2B6bWKipw4EVCwRYsGTo4VbtYan9r%2BHi8egx%2B9Y3KIiNZaDtiZVcsPWiGbBMo9fNVKh9oqNvRol8R%2FXEJMEs69I2Dd38IWBXx8WifzUGVoRko0gASgy9UAQQWlHt7dWkKN8kbpQRzCjFDVwt0CuMboVKV4xJ03ZooA7p3R0u0AYuZMPfg8s8GOqUB5isVh2tNuwejmZCC82l2JKXoC81vfl5YPzP%2BT6dqneENlGrNSAf5rosyWnJRYUfnQeGfdhjFGhpjvlmqS6BHaWAAthy2K57xvOz%2F27FU6pEV53fBiks97%2BXBZkN5z6NEY3EYVseQgYdglEnlJeiIXImv%2Fl6vV6ZUIUxHTIFJ7p3OXRT%2BNQNkJLZsjKYuvC2qJV%2FfQqeP6HpLXAldQB%2B2mIvzBUBn&X-Amz-Signature=2155afb4f0dc2ae02f75904601d8a579cc38e2e4e8c18f6fab015d72aae59c31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
