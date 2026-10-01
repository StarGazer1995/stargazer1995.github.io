---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKS5OO4N%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T203840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkDnL0eiB2JRuOzH34zlzXsGHnpao8dM5uCdXJgyfGqgIhAN%2BnacKiOcHSfVn6jyIWxpPVYw5dHHlma6cEVlBa2ZiGKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwtyd4984RWwskPR40q3APTOgUwIPDet%2Br9%2FCDma0gCdz3gWJO88JLMlJnNkNJLqIaF9naqjYnvq1M4q0Aq79ECxdiK1DJHIF4C0A7peKZtoWSlqphOeXiGmZT2sjf%2FHphlyCLGsDEvnK9sa1r9v4w55K0jcF8KcWdCAsxYD0%2F8HRfXdG%2Bz0Vctv3OtGpFzvUQzbPa9uL4TEBQomIKIMsZNY26rjp7DuRufBj6f%2FeM2EiD79Xj%2FxxLZkwTRtSpons0%2BbCHoIrGPcEsMOQlB1T9X7HFRYGVtl9VGyIYHtkRvVQ82WeoXUgIP9oOMma6lnRyuG5HbwwDN7g4CbPUr9sEga3p7ukLmHdd8Fc3JYdSnf1Gh%2F0fmpfOFeK%2FxAz%2FQh50RMJ2YH9%2FcxNKJqBORdkrwCg94VGfaeZ6ptpA2X6IGSfOPEuR6VtyMoW81jQxpR6gKZEwAdzZokRJTzSX23EYRR3CWaOhd0E2BwY1lr2ipYQes0JXXqEc14MMyX7APSJ3GrV5Ha5D31gZNBKgrF1YdtrHFULQ7KDny2N6dhh5I2U%2BDwRGn8e5bAJm36qcX27TOxexpEaYHeiwb6NQecJZrsgkRR%2Bs0lHBWqS31fXcnWT4RLgrntHtt0gXFxVdw%2BhKRXdjfGoIGl9XGVjDdv%2FrVBjqkAcUVXCackDd4UBjV%2BOiKIffJqN46UB%2BUcZoGqaVFFqXEQ7XOes%2FMByVHWyUy9FDEl7M%2FwrNhddzUyfqzwVy8awr1exsKKpyesDb7oCkhzoiojHTL6Ovs5quIek%2BwuVii7E4FumJGrhjslOKjUDyS%2FcfT1m3Sq%2BUh6n4GrF%2BWI6%2B6EwPWcLjDRJ1cKqZ5qts%2FM73qpHmo%2BSYps%2BUbWHs9HhE67MWU&X-Amz-Signature=1703722111361a50115a039316cad88032b9f3d768c8d271370e1c79de43aad7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
