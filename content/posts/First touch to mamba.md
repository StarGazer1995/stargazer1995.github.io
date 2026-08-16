---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JV3RZPB%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T101202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIDp4Uvacb%2Fza4Ric7Oc1VxXV5H34bBMdfzohdpywJE2sAiB94UDz%2FEGiQQMRSy2sA2ysOhRGAr%2FlfN8Z6grY3HE03Cr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMgnrkEOUXbvI%2F%2BIJcKtwDttyqR0kGu1v4ej5nWQqrb8mpgGR3%2Bc64aiQVrdQ1j%2BhD%2FSAg%2BRs9ylRywChIcAMAlDfdY535AxGo%2Fs%2Bfa3f%2BI%2BhtAOKmkdwmGoxLxXkkg6oFUAWAPDxzaY5Ztp%2F8h%2B%2BhQ9L8uAM19qefYqaTCN0nDI7lzeCiYF0w3ubmeP2O%2F326dD7Ba7IJFEjWIV%2BJ7nyd0cp3pTiYIZBYGPS2TvItJrbjD48YUSA2qVer9%2BQn0N9M2JeqYlnOvu5aAn4VmAK06fBu8K3O%2FJULrGhhiUjsYQl4qsMvGYIJ6QUqAEBhf9bI6IHXzN9SFMzhNWCDWWpBC3GwcbX7ct9%2F4aRko0MdZOeGPeSq5Liw7rkiN7iI8U21Y4BtBqV2HwLNRLOtIIvJkfG5brTJOZ%2BkjtxBXrtqXO6U8%2FEIAvibIaGbiISW%2FiVYQb0ianvtytYvitvQ%2FR4nNJ6BHxv5r9eztKJjdO0mERqR0eRgnt9hUrWaaddtNLxbX%2F%2Fzhbi3IiUcpnLvioYGN7%2FE9qNEfRAhltaq1nYZvQamEQ5Pgw2hIhi9sVAlMI0YSu2dPXQOaW%2FZaJvy9mS0GDWWbYdvDfD5hWM6%2FNU01eigrlhNPNoufn%2FGGp3tW5o0k%2FeNwS7fchY49l8wzoOF1AY6pgH8GBXALs%2FDT6n4cIlJD%2FHHFv1%2FV4dwr43HixQEMQTJAEHw3teuyb8kWlyvb5FcEoB1P5VBPM4ksm%2B3W9iZmbxFXZ%2Bb4UW4gHa3l8ljoI%2BNDH1BY6YdUiUmEVAr2Qk4t3T7IFUtrTVYFXHtpRgVy0fkcxwYGFeu7MfVjMjLD7bYsOU2pP%2Bp54y%2FiH46Y3Dz8n%2FqAx4TqQ4beR%2FGZ0o%2FuoQGrPZJ7B3m&X-Amz-Signature=68dfde1fd425c3507437b1d7fd100aef6fed5afe5a25afac0f323a0c5827c597&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
