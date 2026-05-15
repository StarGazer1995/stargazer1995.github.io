---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPF5EQM2%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T172107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9ZtaWqh%2BDXsmzQM4UiHDQjrnCvSW6vnt3534RjmzfQAiB5901yXdVqpjDU8IRrvolwlcu6OHY9GM64YPV68%2Bxt4ir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMRlPcUl4u5%2BaDgvPkKtwDL28rLAhLt2svydpeh8l6Dl8WkypcrkPwQ38GnN3BsU33I7o4Ml%2FvkhmoNUbe7JzDQuvuG98JYUai2gGxfHGzT%2FJabldd%2FImx%2BBBBpmFNynai8EH8jrof00ahnu%2FKMbtHoad8%2Bzbo%2Bno%2B2vOyhqzlByKwt3QSbK1ySCBh6EmC0gSDyl40pJr6ZmaNxvZKH%2B377A1GCx8cyAUzyrORTtKqbGpcQIjz8gLXu991jgYbYtSSfkaBBqBX%2FsB7JlJkYQUAUeN3vaWvpcILQC5o2GQH2i3px%2BzjxwCjsENWPjPOmaKEumJqJMWECDc%2BReSHUb3RdWHO3Q1VXbxyrC%2FZ263OtJt8uIRDO%2Fx5LoAvzHO4PYwz9DnEPLp1HvOrjJT9EBZrgoMB0KpGBP%2BKPF1Id0NpUNqqSpsKIRTUxDZ8TQl%2BEZeENxDCcWqnk9QPKGj%2FEoNsrsbITgVFDy2OEbNCATYdO4JBrqYnNCX4YJkYrM6CAEgg5hw3WMgSg4t8vRh3BpAPrh3Fl8hpqgySHzAChbdy73ZUQMXRzmLXvDFzqq0eatWZD8IN1Yg5XF7PkjgsDlZAS1Ib47wQd3gt8ZZvliDUaAJTi5IjmFVYuiqVosTtKovaWd3AKmEx3z5iRWwwgvqc0AY6pgGiHw83yIdq5yQVMlV7OdiGcY489RLn%2BDY8rGwh0T5O32Nj1Jp29Z85vrBkII3Fqb2X%2FHKklSBL%2FeBu71I45IEhrExzK%2FccGTQIA8EOG%2F3C9Yi69JrgmmR8eXdN5VL8gVL5jLK1FEBYzSrHG0TsZlGpi%2BlXXxcsbMHehBL3MZV%2BE39LaEOcdU6muKhr7h2MWZHpoQN3P%2FLIxz6njXuFgBth%2FZN2Qs8I&X-Amz-Signature=c654b08b023dd0cc09284d0122e593ea0e53ad9c1125d4dc33799bfe6cfcd3e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
