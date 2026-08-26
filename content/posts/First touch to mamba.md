---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OHBA6NN%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T082914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCENIaAccTmKp28Hlo%2Fv2w1l%2BHDH31faMRb7GReZSnigAIhAPeZQuuiG82EtPfumQpJ%2FnV6K8n0q%2FEwJUkqDgUXSBwxKv8DCBkQABoMNjM3NDIzMTgzODA1IgzS0KscmeMKP2zVZfQq3AN013W79hXUCYESs6ultdOLhtFDkfAFBsraWKo7BQ6sM3kuEYGduUUyfQpr9446Jl%2BK696GeFT%2B2lYRv0dv%2BgGwNrgxz%2BTl7TbXkaBRp%2Bql2m28fLAbX%2B3dQHS7x8oBWBFwoqS0kvTnzd%2B1rNcMh4FwIBCwf6bQLi6E6GfuRzvQfEHVdECJD%2F%2BKvgqQOqLvGL6V6IcjvO3vI8HtJdVYpT8dBCdz%2BrQdCMrn5gl5USrdraNHCLrmexeYdCEEGasfUnRWIzPvTN4X5cfiH04yVX4%2Fj1JPPPIWuoSOl6LF2d%2FclK6Vr8aXfzRn4qyTFt03q65PXhz%2FXzN3M7MGNRFRnu8XlpuHZixfJtbD5cIcvKcPoPrzjjkEuDDOfLZK9EcmJE9jwKalQxqlFPFCKCN6QX6mqdudJgGBWS3hH1DkW2HG4V%2BS8pwjAqqXmZa4B7wZU3ImmHzwzaQyGEqfypFAJf8d%2Bg32jrP%2FLgxI9ZUJBdCNJe63ObmNo8kjI75zx%2B7TR9AOHJDYZezGJiyDSiI1mRjFo5Kjy%2FN3hzHazYKkSe9q98itEp50j4184PxfSyPKCyaJbRsKDU258%2Bpw0DBvnjcHlQtaukqj99n3IkiKmXLjI977TA%2F61jyxNFYluTD6uLrUBjqkAR7zirql%2FmCoHF3Gqmo5hCDtF4j%2B79W2g3%2BpADGTyCw%2BkltNPcsv7U9E%2FYezUFs5vzXoLaZZKOCfF3jy8Dx%2BCLBO9Uah7veSj2il6E37nHbXtqUxAVflmaFCGNRn6Pk9bBiirkk9%2BS6I0PoyNXHLvlIrxzZWKo1zmn1EzC6jWMr%2FG2MjTK6Gh4jGqGaAYn2rYDRyg61PphpbD3HLsVaE4qSofe%2Fs&X-Amz-Signature=894781a53baa9ccc7e911ba09f582f7393164041f9a699fb918aa49e1f7c8904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
