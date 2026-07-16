---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J3UQCIO%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T170127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDDggaWyELF5TVZU96n4hg4fh4Ktck6Uo9iaEjomoYt6QIhAIae1FZJtx4H0rYr36%2Fe%2B111%2FDwKwF9uTb%2B2yuh2tppWKv8DCEcQABoMNjM3NDIzMTgzODA1Igwxi7EEZPkC4eYvLUYq3APLfZ17iPZuRu2YBgq0mztfFrl4UZygMLgMEHS8Z5MjrfbRad921L6hU%2BLltvwgBlKZSGWstHvAoRbphGfN2rmx2GD4v%2FRDmgWYRBWaRO5iP%2BT%2BzYXCj91J5uRaXldmKToXoQ%2BY6m4sQMJAMVeWpOOrjqnfx3fYHmxYEub8roVuJlgHdYUN%2FQXfAEvdxP1v%2BrQYZrpsL0s4y2R3h3rDucnfWRQnc2GA3qi78%2BBBsV9ypGXaRBVXjQPiUSa%2Fb%2B4h1O8Yp9NbHks%2BiUtg5bRl0A5M3ptxDYljdcWTdsFmcWwghxahsW5cwcJ61TB0UclEJUPof2KKuQ%2FyU6Aqnu8O8a1csLmjQo9y90GHPmC57lVi%2F3SthQzExsIhR%2BRT7BWA2NdADWZqKnnbK5lT%2F%2BYiVgXSF%2BZ1YOyN%2FMhUvntZB4SFtiwMHvaXY2u%2FOzQG0%2Fv6GqmaaIGkIDjGdYweAVBf8UlNa9tKcI97lHZae%2BEoMHuG0KwCGfstUjhIoMRS8EN40BEx05BJa3OK1WsskoyskuV5nGVXjv5va8IqTgjviIhKK1QJAzFyYc2pskBftZ7QSJalKDPVrx2kQvJd6MrjvQd9ntEW%2BHW%2BwueuKKLkoN3mnkj0JfiaTgCUsN9HCTC3xOPSBjqkAdJ3EIBYb6YGMY6JjHzmZKuo2AkR5PfdqZNFK7b1OphRVMTg%2Fxvfnq0rErhdqXsdFD9vEuLAlEluTAaD5yOvAM6iipnunir33lQoWWVCDpO2C1AuW0E%2BU9racOP44xZP%2FJfx3gxLLqoadCbrf%2BIU9tVRsy%2BIzK8cw6LNeSwvU47asDi8vyzJKJVhuyDHYtHfOY58ICTlTimKLQ50vXozUIVRSLHh&X-Amz-Signature=a716205b5bbb01ccc0c1606cd7839b36efb9acea1e61ed9a638edf1a7a545ae3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
