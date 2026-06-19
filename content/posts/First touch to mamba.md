---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPQT5JPH%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T132714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLEEfC%2Bvst7s7myiPkAPI3BTEAx4YnEAJuaWeWyvfoZAIhAJrJGnWAjCtrO7Ncfx5bADDKbBQjsVDZHsUvJoduwLS4KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxL%2FBo9WhLlgAalngsq3AOoNbGJCBXVGEPL7hJOJ6RUs8n3N48UhXVv8bUM8NXuCc8CODyAP941%2FnIysKlPtyw8NjPpfJXmRXgypAjr1nyt4bbsX66eb84ir8NgQWTGcBo%2FopjKvKWbGO1UFufsmsG525QH297%2FQZwn0ZweS8LA7Wl8FYHFDlZJwvSIkMAH0bcJ2JcstC%2FegEosC5n2HyhHI6shn7WyYBIPoqHg%2Bqu5X4f3%2F3tiuhqsJHNCqFvCJ0BVtHFhT9glm%2FFApxDpFZ9N2Ga2JQZmjrq6szuNfKxWDSmr%2BzHiqIocuhmkqY%2F8ytnnjFHrh7Z8bd%2F2ZDENCUo5aMZlwcxsUH8V0tR4vZbPdFegbmFdeiVY2%2FPZAG8%2Fcw4ehQVXATVoYR01TgC1qr%2FwZTvrFFpvtK1J1dydOEayUOMZq409%2Bj7aLt%2BSUW5cQDCBKK7CLfG7xy%2F5AzRb336stDEmmzj2FASnJz34mXqziV4t%2FRDNGa3Y364%2Bc%2F8wSjIaqf0drff8hvQysnKrnuYazBpEHF4rBd%2FzO7vGyfExEsKBq%2BgaWKGuU9ckjvQ3Q%2BhLkeBG%2BUXTq2WpMeT54b1mRMtIRPYZ2jjnWYuw5jGUfGMmQzlb6VfHEolLxJU%2Fi9PyNfCJoHrJDeUd0DC95tTRBjqkAX9c1RgBLr%2F5%2F22dzqv1kaLoHVbd6EKEMDc29E%2BoSitLJ1IksWR5%2BzKVAUArt2daodUE8E1Mz0mYpaa%2BV7Z51AeHfhlatKO549xCFePPc9KbV5BeAWnF1RLWKu6uE0ObxKT52OtBNH2xnJIglWB56M6lsWk9DVmFO0o5UL3XeiVdr6tAPw244HYUrjEUFnlgXR1DzTbgAE6ULA2lgyjgKPqeOHQC&X-Amz-Signature=775be653931d35df3d956a4ab2aa800a0757c10d9ecf39885e36e710b40d6517&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
