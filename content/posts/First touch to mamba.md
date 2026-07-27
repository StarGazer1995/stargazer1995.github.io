---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUPACMXG%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T210102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyjPGgoq5bGQmyR0opZl3YaWdm%2FFI7%2FNxOzDN4xINC%2FgIhANtN094efbQM6Sn1zkgtHZyZSUGogxRyZt3rj6J0mUaVKv8DCFUQABoMNjM3NDIzMTgzODA1IgyExwKXtKV%2Fx1%2BHi0cq3APOtx0wS6JUN0AyOl8B%2Fth%2FlVPreRZn2yZSUV%2F78Yil0ZjnfdvFb6bTYIoGW%2FBjhDmyNt8GF%2Ba5brfv45RDjIlGnPOm%2BD%2FZKdSth7GQxfpuiyfjnOVsbArSlQrzrYGGPuvCy4TWfdObMOAGVQdDICgFoFdQ%2BPZcGophPZPH1jW9%2BHaNhBex6TsXDtovqVYf6DOqQu40FUbhWPeMl1nJgst4E0gNbaQj8tpT19DAHoM%2BHYOOoDyhOjhmPtrrohvbBxuyaDMsXqs2rpQ4q9Ei%2BirxZp0kV3lHcRnEl7R06jctvZvJ0C5WQXWg1R7A854Exv4g1ehSqf3FdoLI5K7U3zhuCBIR5DJ5RspI7cVq%2BssQNceQvoX4Fa%2FWsTpUOklh2adYSDYjEA9dq%2F0NhfPRG25qVZ1b0IBguAHuMYRbWoj1DTMLboglEdoE5qe5Mw2B6Oxd3%2Fw5%2BUzyN9XaebuF%2F%2FZq2zDFfv50GIn00WJRe2PIBUeJwNSeyIfXk1Csx1Wic3WDR1CImmbKQoQK0%2FEA0m6g4LjZV4C8tG5gAY7OMJNVTLHvgALQdexmIkWcyjSeRManeiXwiSmseEhql7XskzTIRo9NccL%2FQKQhMZYQk3DHsW2Y83dXcKa%2BLhL%2BozD57J7TBjqkAeagya0%2Bj5XAQBKd6OKsYvIp9Cvs49z2k7fkeujZEgC63seDmM0Jkj9N7e5AyxgW5Kw4gMK54H56H6gjVEiYprRhzABzQgsgJCt0IxJarZbTbvs7b7MwW87VjT6jutBAFnoh1agMlf4zL2iWuedghLj6Cy8ARbTmJ0G5S2ZVwl5MG8ZUiIqhauGsU%2Bxawt%2BaCU29CdWpsCxor8r2hiYnkgScX8C4&X-Amz-Signature=80b41d545a4343dba5a5a050ae59795ebc66f4e21d329cfe252151b585f3b0e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
