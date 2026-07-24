---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKO2XECE%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T131424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDodS72xG2Cv4CTc%2FAqi0vfzPi8cbjKK99xAJy9JzrRSgIhAJRL3lYu0PXCaeK5uyQa%2FDpaDrw%2FmH3ZwPXC6hI0tkCoKv8DCAMQABoMNjM3NDIzMTgzODA1IgwqD5rUaPaahQXWOfEq3APe5KtSE7yBoJAoEYUJa%2BlBc2T4ybCTh3dSIr5Vtbiz2TmMF0vfKY5rqXVcpO%2F3l63OEbrTSz%2Bqasj%2BSfJl1arfMLXCdPCr%2FQPAPnrwh10xetjAMGjonP6245%2BZj%2BERW1YTzc5g7bUsjaU%2BPhVXMPApPcoauUMYH4cITpMiocbour6WkQPq6jl4f1YSCQHDT2U7Mutct2Hx6CePl23qkhdUtBePDFFpz8K2B8U75pyiR6CuVEBvIzd7YvW6JGOZX4%2BocTViMkf6Pox7FjavQpthJv1mYXWxlJ%2FKAHdYV4iRQamWS9xjTIySTN5b4ExEBTdPyptJPzOvOdNixqAwTROAq8Y7ChTPffqMjziaGiape4LhZjaB%2FtPJlmHyC6GzR6uKsFOd7SqG3Rc1vwQu2hn2HcuYGYiCNSezi%2Fc3P969qM3ZFSoEAEIVMx7%2FRW%2BaKf8Lf5OmHGGOzhi5UQqVOnfzXqDvOoOiWXI2AbserO5pRHoeCOE4nzIpnj%2FFwDaU0dw16UBVD7CHzhVYo8GXooIyIOZAVaJf6p34LdL54dsvD56bPBE7CLdW8pbXQdlRR%2FmcBa%2F2sn8WZOfSxV3ufjbs6Q0niUXlIQuWFf3rsqRU8GdS2lfGkxJ6Blm5wDCz5IzTBjqkAUBizjrbrx4Tuq4f7MgDdpzFHiLq8qkE%2FaP4Si%2FNK%2F6H8%2FwhbmZ26QZxMspGF4xUwrUvw3wdrWYbH%2B67ktNxgIw294VHHaI9fpM4WRgtWkticVs5jp%2FVPSVl1fpJDUitV59G%2FKUmdA4OZ6MXspBg0BX7hIs24gW9QYl5Hp5h%2FLIQOI57KNhbNquDicRL6oOS5TsUsSfHrnrMsq%2FrhZNE%2Fhu9d7AV&X-Amz-Signature=80e2a934c80ca4ec7443d1a95195c171ad608d6576dcd119b650bb90c2725c95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
