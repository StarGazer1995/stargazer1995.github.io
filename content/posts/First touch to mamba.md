---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6AV3XBM%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T114533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIF43vwB7XGRVmyFD5TXfLeKyV3UP03yQlLfRqwl7erwOAiBwoKTN0nx1UrCaAsWLGysPotIyvvlN7Xy7l2m6KGrSEiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSQQ0Cwsj2ujKLLSQKtwD5jc9VDFzHVuX92bDc6Jkc%2FunPaV8EQgYtrKKuEEbOhUXLDCDbZ6rGhUXGHHZ7h1%2BbIoepXc9gvqOG7taLC%2BkFD2P5WKVgwSgFRuMOjrhDweuhahKI9rRaNGTWsO47V6JLl99XVpuNbD20FNX%2BbHLtWakF2FnyHXhLMwuU0XmVF83vvxDb94eEEOGyYgBwPGybm1yqIW%2F88H%2FX7eZXRxm7wIkP3pPF5wRyhhiTZ9dMnKAz7sbur1zgbYuOgKrfSDLsVsLF%2B0Lygj4bh8haoWc6Abah260%2F2T23gXVoAS4wx4997aRTEMXjtnmxQG%2B9pckDTcHDNeIXVyslR9cmO%2FmuUU%2FC%2Bcebk0qixobE0pLcSqcIjtw%2BJFJ52C0icVELtsEksdVqUBvqqgSWUj2PD1ck0yZDv4ZAN1tZVTthKhYU02L2hS%2FQCSb0whtDbTMPIwVrosg8xnQVtVBqc1ApMvVuvKhyu%2FQhS%2BA9e0dooPPk59pL84Nt5OiKCxQA3i0LteQ0nbc23KGWzkwsx0OJ7suq1omV4SktCtREK%2FNm4waXURV4j%2FLoXW5dvlj5NH%2BAhOklRgpCo8nG5odPi%2BMD62vOechoFwg58B%2FhDzTr4cBEXWEQ2NaujPUedPWWvYw9fiH0wY6pgG0wzybtmbpJSpMc8TP2Vw1XdqyOqVcKXaogO3H87%2F0%2BbU4Y4UAYmKmwB3mHY%2BKnqgzsVswMAooxm5oCpSexpuKhwRyIHQlqD5QTBmQ3YrYfIAKmMhDc2CTNHwoxz9x0XNQX3A1MfJ2ZTKGXDaKNVQuw25Wcw9IhrFZhBs%2B%2B18kQ3raL4TN4L8g%2BqdcTFP4JZmBHQYCXOkcsyORZsBWI29KRXEOKzPi&X-Amz-Signature=3dd0c0059c2905c96f298b24418b11fa5b2c581e02f9b7995c5859983c7e56b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
