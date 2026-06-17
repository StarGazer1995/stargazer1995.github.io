---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664SGYC4Y%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T023221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQIJQf4IRexmfo1D2uP8B5y0qG4zQ%2BWS4LkrYiwrA1eAiBoR640ctoMFy%2BI2cmkswh4sWqWtURsJb9i1mfrGdtz8iqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMh%2B88L7PiChop3j8DKtwDBUkHr2IshDdfhFBWENt8aYhGzfg0Z9J%2BEOoBQzjHsC9Ku%2BA958Q9TfpknFnkPbFPXy02UklSXK2ezR8ASKC2lzXG%2FO3D%2FG%2BSzSEBqrvZQQ3%2FqtDqdf3gtGwnia4hk%2FdyYro%2BxgUWVZxQV8kjXfosWMBsbP0PDaS2wLenZ%2FwXSH%2BSAIL3kZOxJrlTr98PMDFWe6r4A5XgppycqX1pxO%2FDZnr3DelAhf4x1vAU9p%2BlG3qrbiU6FWXlSXrYv%2BXqWhWTdYK37757rrVKhwD7sfcPIlotMS7%2BD6hEEG3H%2BC%2FA%2BNIruxba98ato6%2BFRssjY6kckB1qgztDG0Jw0min8GdIOatBEP3vhl%2BdpQfnMz%2FcCCylls45DTi8UpeK8efDOYO7mNh99PqThnjc2JyI6tHTQx0I%2Bq8CyAULVQmI8t%2BEQvlcTjF7lGI%2BvGDCAYaEaTcVCnbSg49wYdUoL2Ui%2F0Jy5C5bjdnu7P5IhQfMBmVMQoZNh7RXG5A5NhuM9RkOKJOo8%2FQjnZX3THppU9V6nPK28ax7N5FeokZkGKYZPeuXN30ur0PH7TZR4s%2BRNRvTDy2Syx6BSaxqR4lUkbiozcxMGGJWvC%2BHnWLFWySWzdRU2spstn0l9saedKk94DAwvbbH0QY6pgEvCwizTpk9VWYzfUTsfcHsTQV5CoyZVEKUW5UyWWFGWBb4ByTI9i36Svau9QqHiiDz4KKwDt94cA%2FVGyVFzpEBV7ZzYIuheCzFHNRulvZqirLSUQAdxHEXqPFgsa3zruo37GDyhGKtwvRTmoizDZ70CUl7aQsCmn%2FjrTeSTgKYDnvL%2FDozq82P%2BLOxyNf3JCsvVwl2d2qy%2FuudCnmJL%2BGAYDm3rjmF&X-Amz-Signature=a284144fdfaf0b5e7f145d2cc2e3e275559eb500e7574a7c4d8d8ec52e3269e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
