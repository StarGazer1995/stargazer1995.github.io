---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXATPK5%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T164100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDS40kPuAOnE95Hj8DJ9utOGPpUyRbBZyNMhjUvsMKkowIhAOqAETU6ngyJC%2BTKilcbnDuaLYY4ZWquKZnpDzlPFcGWKogECOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BlvdUtWbopcxqx4Iq3AOgvFbjjrlyN5CYnFcZ%2FCeZmLPOrEIbP678hYBRiSnsCUBzl7uCFXecMOClfpxQhIcQCVnkAW6Zp7IqPUiIttq0kBJxTDDIeMND7qHf%2FIPp%2BsyhUmJo0d4nnrHL8r3SQK2dZ1NpMOziRSWigl127fQ32CqaX9aslllMTS3Zh1aZPwyczz8%2BvERcQfzqNoAqDKwv4mLwDGL7Byn0IXIOZ%2Br84LRfUSj4LZMfmHKZ7exexs2ef3MpgHpMOW1BvJ2O8rqTqmw2rmtAb%2BBm6j10m2ZVReQNHDBSNoQ6QCFOumNl%2FezSFOqne5bbPRdO4MypcShENntPUe4fsFMVdY%2FNqW40dKarjTNur7QkVqcnZeHRiIqOLg%2B3UsBsidJV4VBI9XZ9HhfX1WkycyhIVKTNt4vMs41hg241jfKnYzqYOMDaEwnKG8hB5OmpE2sdEtKlzwMZHCEb9ThlOEyLDpoUVy8zredo1ULq5ieqmYGBJjqT1E3RKsS8XOcOpxA%2BGdfiGJM3Gdv8sgTlEVT4qc65P1iO4TC5eGUjssEQMt5k3j2nwMQt8XGczhfMc0wWUOTNN6nQ%2FOOeQaIUq0cFuIg6K%2Ftk%2FF3mcgNY85ruKnFO0lUlN4AWVmVUjtmwzTY2RTCru%2F3PBjqkAXaJDmmHjRNpNQTWNjq4dFix8SWdUQqZnaS12QXL5Jni8Xebt4psa6ZYYDqDT%2BbHlDbHLGjS8WU2UyUyVBA9ygC7Eh8431ww4ncauaEUC0KAX9r2WVWgc%2BxupQr3oHdJfp%2ByQb%2BiX0yBASbnNBNOJigN595SN%2BXO%2FUSf0w5eexjYRwpov0kBOIRruGRiRmY%2BIW8cC%2FAXMXulkVOSzSZuL96G2%2FBB&X-Amz-Signature=a3f52a2832665b8511488a8a3d6ab3af92c90e6e24fd3cc79eac486a4822a228&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
